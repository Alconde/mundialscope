from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer
from django.views.generic import ListView, DetailView, TemplateView
from .services import build_team_stats
from .forms import TeamComparisonForm
from .comparison_services import build_team_comparison
from .report_services import generate_team_report
from .services import get_team_dashboard_kpis
from core.charts import build_line_chart, build_grouped_bar_chart, build_donut_chart, build_bar_chart

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

        players = team.players.filter(is_called_up=True).order_by(
            "position", "shirt_number", "last_name"
        )

        team_kpis = get_team_dashboard_kpis(team)

        goalkeepers = players.filter(position="GK").count()
        defenders = players.filter(position="DF").count()
        midfielders = players.filter(position="MF").count()
        forwards = players.filter(position="FW").count()

        context["players"] = players
        context["player_count"] = players.count()
        context["goalkeepers"] = goalkeepers
        context["defenders"] = defenders
        context["midfielders"] = midfielders
        context["forwards"] = forwards

        context.update(team_kpis)

        context["form_chart"] = build_line_chart(
            title="Puntos por partido",
            x_values=team_kpis["form_labels"],
            y_values=team_kpis["form_points"],
            y_axis_title="Puntos",
            line_color="#0f766e",
        )

        context["goals_chart"] = build_grouped_bar_chart(
            title="Goles a favor vs en contra",
            x_values=team_kpis["form_labels"],
            series=[
                {"name": "A favor", "values": team_kpis["goals_for_series"]},
                {"name": "En contra", "values": team_kpis["goals_against_series"]},
            ],
        )

        context["squad_chart"] = build_donut_chart(
            title="Distribución de plantilla",
            labels=["Porteros", "Defensas", "Centrocampistas", "Delanteros"],
            values=[goalkeepers, defenders, midfielders, forwards],
        )

        context["discipline_chart"] = build_bar_chart(
            title="Disciplina de la selección",
            x_values=["Amarillas", "Rojas"],
            y_values=[team_kpis["yellow_cards"], team_kpis["red_cards"]],
            y_axis_title="Tarjetas",
            bar_color="#b45309",
        )

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