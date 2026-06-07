from django.urls import path
from .views import (
    MatchDetailPageView,
    TournamentTacticalDashboardView,
    GroupStandingsPageView,
    MatchListPageView,
    WorldCupDashboardView,
)

app_name = "matches"

urlpatterns = [
    path("", MatchListPageView.as_view(), name="match-page-list"),
    path("", WorldCupDashboardView.as_view(), name="world-cup-dashboard"),
    path("tactical-dashboard/", TournamentTacticalDashboardView.as_view(), name="tactical-dashboard"),
    path("groups/", GroupStandingsPageView.as_view(), name="group-standings"),
    path("<int:pk>/", MatchDetailPageView.as_view(), name="match-page-detail"),
]