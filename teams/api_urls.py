from django.urls import path
from .views import TeamListAPIView, TeamDetailAPIView

app_name = "teams_api"

urlpatterns = [
    path("", TeamListAPIView.as_view(), name="team-list"),
    path("<int:pk>/", TeamDetailAPIView.as_view(), name="team-detail"),
]