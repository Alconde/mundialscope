from django.db.models import Q
from django.utils import timezone
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tournament, Match, MatchEvent
from .serializers import TournamentSerializer, MatchSerializer
from teams.models import Team
from players.models import Player
from django.views.generic import TemplateView
from .services import build_group_standings
from .analytics_services import (
    get_top_scorers,
    get_top_carded_players,
    get_most_eventful_matches,
    get_events_summary,
)
from .report_services import generate_match_report




class TournamentListAPIView(generics.ListAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    filterset_fields = ["year", "tournament_type", "is_active"]
    search_fields = ["name", "host_country"]
    ordering_fields = ["year", "name", "start_date"]
    ordering = ["-year"]


class TournamentDetailAPIView(generics.RetrieveAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchListAPIView(generics.ListAPIView):
    queryset = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).all()
    serializer_class = MatchSerializer
    filterset_fields = ["tournament", "stage", "group", "status", "home_team", "away_team"]
    search_fields = ["home_team__name", "away_team__name", "stadium", "city"]
    ordering_fields = ["match_date", "home_score", "away_score"]
    ordering = ["match_date"]


class MatchDetailAPIView(generics.RetrieveAPIView):
    queryset = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).all()
    serializer_class = MatchSerializer


class DashboardOverviewAPIView(APIView):
    def get(self, request):
        now = timezone.now()

        next_matches = Match.objects.select_related(
            "tournament",
            "home_team",
            "away_team",
        ).filter(
            match_date__gte=now
        ).order_by("match_date")[:5]

        live_matches = Match.objects.select_related(
            "tournament",
            "home_team",
            "away_team",
        ).filter(
            status="live"
        ).order_by("match_date")

        active_tournament = Tournament.objects.filter(is_active=True).order_by("-year").first()

        data = {
            "summary": {
                "active_tournament": active_tournament.name if active_tournament else None,
                "total_teams": Team.objects.filter(is_active=True).count(),
                "total_players": Player.objects.filter(is_called_up=True).count(),
                "total_matches": Match.objects.count(),
                "live_matches": live_matches.count(),
            },
            "next_matches": MatchSerializer(next_matches, many=True).data,
            "live_matches_detail": MatchSerializer(live_matches, many=True).data,
        }

        return Response(data)
    
class MatchListPageView(ListView):
    model = Match
    template_name = "matches/match_list.html"
    context_object_name = "matches"
    paginate_by = 10

    def get_queryset(self):
        queryset = Match.objects.select_related(
            "tournament",
            "home_team",
            "away_team",
        ).order_by("match_date")

        stage = self.request.GET.get("stage")
        status = self.request.GET.get("status")
        team = self.request.GET.get("team")

        if stage:
            queryset = queryset.filter(stage=stage)

        if status:
            queryset = queryset.filter(status=status)

        if team:
            queryset = queryset.filter(
                Q(home_team__id=team) | Q(away_team__id=team)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_stage"] = self.request.GET.get("stage", "")
        context["selected_status"] = self.request.GET.get("status", "")
        context["selected_team"] = self.request.GET.get("team", "")
        context["teams"] = Team.objects.filter(is_active=True).order_by("name")
        context["stage_choices"] = Match.Stage.choices
        context["status_choices"] = Match.Status.choices
        return context


class MatchDetailPageView(DetailView):
    model = Match
    template_name = "matches/match_detail.html"
    context_object_name = "match"

    def get_queryset(self):
        return Match.objects.select_related(
            "tournament",
            "home_team",
            "away_team",
        ).prefetch_related(
            "events",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = self.object.events.all()

        goal_types = [
            MatchEvent.EventType.GOAL,
            MatchEvent.EventType.PENALTY_GOAL,
            MatchEvent.EventType.OWN_GOAL,
        ]
        card_types = [
            MatchEvent.EventType.YELLOW_CARD,
            MatchEvent.EventType.RED_CARD,
            MatchEvent.EventType.SECOND_YELLOW_RED,
        ]

        context["event_stats"] = {
            "total_events": events.count(),
            "goals": events.filter(event_type__in=goal_types).count(),
            "cards": events.filter(event_type__in=card_types).count(),
            "key_events": events.filter(is_key_event=True).count(),
            "substitutions": events.filter(event_type=MatchEvent.EventType.SUBSTITUTION).count(),
        }

        if self.object.status == Match.Status.FINISHED:
            context["match_report"] = generate_match_report(self.object)
        else:
            context["match_report"] = None

        return context
class GroupStandingsPageView(TemplateView):
    template_name = "matches/group_standings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group_standings"] = build_group_standings()
        return context