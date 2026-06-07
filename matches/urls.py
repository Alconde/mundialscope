from django.urls import path
from .views import (
    MatchDetailPageView,
    TournamentTacticalDashboardView,
    GroupStandingsPageView,
    MatchListPageView,
)

app_name = "matches"

urlpatterns = [
    path("", MatchListPageView.as_view(), name="match-page-list"),
    path("tactical-dashboard/", TournamentTacticalDashboardView.as_view(), name="tactical-dashboard"),
    path("groups/", GroupStandingsPageView.as_view(), name="group-standings"),
    path("<int:pk>/", MatchDetailPageView.as_view(), name="match-page-detail"),
]