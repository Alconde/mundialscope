from django.urls import path
from .views import PlayerListAPIView, PlayerDetailAPIView

app_name = "players_api"

urlpatterns = [
    path("", PlayerListAPIView.as_view(), name="player-list"),
    path("<int:pk>/", PlayerDetailAPIView.as_view(), name="player-detail"),
]