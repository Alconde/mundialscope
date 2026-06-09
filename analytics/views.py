from django.views.generic import TemplateView, DetailView
from teams.models import Team
from players.models import Player

from .forms import TeamCompareForm, PlayerCompareForm
from .services import (
    build_home_dashboard,
    build_team_dashboard,
    build_team_detail,
    build_team_comparison,
    build_player_dashboard,
    build_player_detail,
    build_player_comparison,
)


class AnalyticsHomeView(TemplateView):
    template_name = "analytics/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_home_dashboard())
        return context


class TeamAnalyticsListView(TemplateView):
    template_name = "analytics/teams/team_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_team_dashboard(filters=self.request.GET))
        return context


class TeamAnalyticsDetailView(DetailView):
    model = Team
    template_name = "analytics/teams/team_detail.html"
    context_object_name = "team"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_team_detail(self.object))
        return context


class TeamAnalyticsCompareView(TemplateView):
    template_name = "analytics/teams/team_compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TeamCompareForm(self.request.GET or None)
        context["form"] = form

        if form.is_valid():
            context["comparison"] = build_team_comparison(
                form.cleaned_data["team_a"],
                form.cleaned_data["team_b"],
            )

        return context


class PlayerAnalyticsListView(TemplateView):
    template_name = "analytics/players/player_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_player_dashboard(filters=self.request.GET))
        return context


class PlayerAnalyticsDetailView(DetailView):
    model = Player
    template_name = "analytics/players/player_detail.html"
    context_object_name = "player"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_player_detail(self.object))
        return context


class PlayerAnalyticsCompareView(TemplateView):
    template_name = "analytics/players/player_compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = PlayerCompareForm(self.request.GET or None)
        context["form"] = form

        if form.is_valid():
            context["comparison"] = build_player_comparison(
                form.cleaned_data["player_a"],
                form.cleaned_data["player_b"],
            )

        return context