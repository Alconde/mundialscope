from django.db.models import Count, Q
from django.shortcuts import render
from django.utils import timezone
from players.models import Player
from teams.models import Team
from matches.services import build_group_standings
from matches.analytics_services import (
    get_top_scorers,
    get_top_carded_players,
    get_most_eventful_matches,
    get_events_summary,
)

from django.views.generic import TemplateView
from matches.models import Match, MatchEvent, Tournament



def home(request):
    now = timezone.now()

    active_tournament = Tournament.objects.filter(is_active=True).order_by("-year").first()

    next_matches = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        match_date__gte=now
    ).order_by("match_date")[:6]

    live_matches = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        status="live"
    ).order_by("match_date")

    featured_teams = Team.objects.filter(is_active=True).order_by("name")[:8]

    teams_by_group = (
        Team.objects.filter(is_active=True)
        .values("group")
        .annotate(total=Count("id"))
        .order_by("group")
    )

    top_ranked_teams = Team.objects.filter(
        is_active=True,
        fifa_ranking__isnull=False
    ).order_by("fifa_ranking")[:5]

    top_squads = Team.objects.filter(is_active=True).annotate(
        player_count=Count("players", filter=Q(players__is_called_up=True))
    ).order_by("-player_count", "name")[:5]

    group_standings = build_group_standings()
    top_scorers = get_top_scorers(limit=5)
    top_carded_players = get_top_carded_players(limit=5)
    most_eventful_matches = get_most_eventful_matches(limit=5)
    events_summary = get_events_summary()

    context = {
        "active_tournament": active_tournament,
        "total_teams": Team.objects.filter(is_active=True).count(),
        "total_players": Player.objects.filter(is_called_up=True).count(),
        "total_matches": Match.objects.count(),
        "live_matches_count": live_matches.count(),
        "next_matches": next_matches,
        "live_matches": live_matches,
        "featured_teams": featured_teams,
        "teams_by_group": teams_by_group,
        "top_ranked_teams": top_ranked_teams,
        "top_squads": top_squads,
        "group_standings": group_standings,
        "top_scorers": top_scorers,
        "top_carded_players": top_carded_players,
        "most_eventful_matches": most_eventful_matches,
        "events_summary": events_summary,
    }

    return render(request, "core/home.html", context)


from django.views.generic import TemplateView
from django.db.models import Count, Q
from matches.models import Match, MatchEvent, Tournament
from teams.models import Team
from players.models import Player
from .charts import build_bar_chart


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        active_tournament = Tournament.objects.filter(is_active=True).first()

        matches = Match.objects.all()
        if active_tournament:
            matches = matches.filter(tournament=active_tournament)

        context["active_tournament"] = active_tournament
        context["total_teams"] = Team.objects.filter(is_active=True).count()
        context["total_players"] = Player.objects.filter(is_called_up=True).count()
        context["total_matches"] = matches.count()
        context["finished_matches"] = matches.filter(status="finished").count()

        context["total_goals"] = MatchEvent.objects.filter(
            match__in=matches,
            event_type__in=["goal", "penalty_goal", "own_goal"]
        ).count()

        context["total_cards"] = MatchEvent.objects.filter(
            match__in=matches,
            event_type__in=["yellow_card", "red_card", "second_yellow_red"]
        ).count()

        top_scoring_teams = list(
            Team.objects.filter(is_active=True)
            .annotate(
                goal_events=Count(
                    "match_events",
                    filter=Q(match_events__event_type__in=["goal", "penalty_goal", "own_goal"])
                )
            )
            .order_by("-goal_events", "name")[:5]
        )

        most_disciplined_teams = list(
            Team.objects.filter(is_active=True)
            .annotate(
                card_events=Count(
                    "match_events",
                    filter=Q(match_events__event_type__in=["yellow_card", "red_card", "second_yellow_red"])
                )
            )
            .order_by("card_events", "name")[:5]
        )

        context["top_scoring_teams"] = top_scoring_teams
        context["most_disciplined_teams"] = most_disciplined_teams

        context["latest_matches"] = matches.select_related(
            "home_team", "away_team", "tournament"
        ).order_by("-match_date")[:6]

        context["goals_chart"] = build_bar_chart(
            title="Goles por selección",
            x_values=[team.name for team in top_scoring_teams],
            y_values=[team.goal_events for team in top_scoring_teams],
            y_axis_title="Goles",
        )

        context["cards_chart"] = build_bar_chart(
            title="Tarjetas por selección",
            x_values=[team.name for team in most_disciplined_teams],
            y_values=[team.card_events for team in most_disciplined_teams],
            y_axis_title="Tarjetas",
        )

        return context