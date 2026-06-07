from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer
from django.views.generic import ListView, DetailView, TemplateView
from .services import build_team_stats
from .forms import TeamComparisonForm
from .comparison_services import build_team_comparison
from .report_services import generate_team_report
from .services import get_team_dashboard_kpis


class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ["confederation", "group", "is_active"]
    search_fields = ["name", "fifa_code", "coach"]
    ordering_fields = ["name", "fifa_ranking"]
    ordering = ["name"]


class TeamDetailAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ["confederation", "group", "is_active"]
    search_fields = ["name", "fifa_code", "coach"]
    ordering_fields = ["name", "fifa_ranking"]
    ordering = ["name"]


class TeamDetailAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamListPageView(ListView):
    model = Team
    template_name = "teams/team_list.html"
    context_object_name = "teams"
    queryset = Team.objects.filter(is_active=True).order_by("group", "name")


class TeamDetailPageView(DetailView):
    model = Team
    template_name = "teams/team_detail.html"
    context_object_name = "team"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.object

        context["players"] = team.players.filter(is_called_up=True).order_by(
            "position", "shirt_number", "last_name"
        )

        home_matches = team.home_matches.select_related("away_team", "tournament")
        away_matches = team.away_matches.select_related("home_team", "tournament")

        recent_matches = list(home_matches) + list(away_matches)
        recent_matches = sorted(recent_matches, key=lambda m: m.match_date, reverse=True)[:5]

        context["recent_matches"] = recent_matches
        context["player_count"] = context["players"].count()
        context["goalkeepers"] = context["players"].filter(position="GK").count()
        context["defenders"] = context["players"].filter(position="DF").count()
        context["midfielders"] = context["players"].filter(position="MF").count()
        context["forwards"] = context["players"].filter(position="FW").count()

        return context


class TeamComparisonPageView(TemplateView):
    template_name = "teams/team_compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TeamComparisonForm(self.request.GET or None)
        context["form"] = form
        context["comparison"] = None

        if form.is_valid():
            team_a = form.cleaned_data["team_a"]
            team_b = form.cleaned_data["team_b"]
            context["comparison"] = build_team_comparison(team_a, team_b)

        return context
    

class TeamListPageView(ListView):
    model = Team
    template_name = "teams/team_list.html"
    context_object_name = "teams"
    queryset = Team.objects.filter(is_active=True).order_by("group", "name")


class TeamDetailPageView(DetailView):
    model = Team
    template_name = "teams/team_detail.html"
    context_object_name = "team"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.object

        players = team.players.filter(is_called_up=True).order_by(
            "position", "shirt_number", "last_name"
        )

        team_kpis = get_team_dashboard_kpis(team)

        context["players"] = players
        context["player_count"] = players.count()
        context["goalkeepers"] = players.filter(position="GK").count()
        context["defenders"] = players.filter(position="DF").count()
        context["midfielders"] = players.filter(position="MF").count()
        context["forwards"] = players.filter(position="FW").count()

        context.update(team_kpis)

        return context


class TeamComparisonPageView(TemplateView):
    template_name = "teams/team_compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TeamComparisonForm(self.request.GET or None)
        context["form"] = form
        context["comparison"] = None

        if form.is_valid():
            team_a = form.cleaned_data["team_a"]
            team_b = form.cleaned_data["team_b"]
            context["comparison"] = build_team_comparison(team_a, team_b)

        return context