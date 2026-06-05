from django.urls import path
from .views import (
    TournamentListAPIView,
    TournamentDetailAPIView,
    MatchListAPIView,
    MatchDetailAPIView,
    DashboardOverviewAPIView,
)

app_name = "matches_api"

urlpatterns = [
    path("dashboard/overview/", DashboardOverviewAPIView.as_view(), name="dashboard-overview"),
    path("tournaments/", TournamentListAPIView.as_view(), name="tournament-list"),
    path("tournaments/<int:pk>/", TournamentDetailAPIView.as_view(), name="tournament-detail"),
    path("", MatchListAPIView.as_view(), name="match-list"),
    path("<int:pk>/", MatchDetailAPIView.as_view(), name="match-detail"),
]