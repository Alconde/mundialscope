from django.urls import path
from .views import PlayerListPageView, PlayerDetailPageView

app_name = "players"

urlpatterns = [
    path("", PlayerListPageView.as_view(), name="player-page-list"),
    path("<int:pk>/", PlayerDetailPageView.as_view(), name="player-page-detail"),
]