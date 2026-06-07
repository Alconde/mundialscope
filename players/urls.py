from django.urls import path
from .views import (
    PlayerListPageView,
    PlayerDetailPageView,
    PlayerComparisonPageView,
    PlayerRankingPageView,
)

app_name = "players"

urlpatterns = [
    path("", PlayerListPageView.as_view(), name="player-list"),
    path("compare/", PlayerComparisonPageView.as_view(), name="player-compare"),
    path("rankings/", PlayerRankingPageView.as_view(), name="player-rankings"),
    path("<int:pk>/", PlayerDetailPageView.as_view(), name="player-detail"),
]