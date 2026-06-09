from django.urls import path
from .views import (
    AnalyticsHomeView,
    TeamAnalyticsListView,
    TeamAnalyticsDetailView,
    TeamAnalyticsCompareView,
    PlayerAnalyticsListView,
    PlayerAnalyticsDetailView,
    PlayerAnalyticsCompareView,
)

app_name = "analytics"

urlpatterns = [
    path("", AnalyticsHomeView.as_view(), name="home"),
    path("teams/", TeamAnalyticsListView.as_view(), name="team-dashboard"),
    path("teams/<int:pk>/", TeamAnalyticsDetailView.as_view(), name="team-detail"),
    path("teams/compare/", TeamAnalyticsCompareView.as_view(), name="team-compare"),
    path("players/", PlayerAnalyticsListView.as_view(), name="player-dashboard"),
    path("players/<int:pk>/", PlayerAnalyticsDetailView.as_view(), name="player-detail"),
    path("players/compare/", PlayerAnalyticsCompareView.as_view(), name="player-compare"),
]