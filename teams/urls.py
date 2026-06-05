from django.urls import path
from .views import TeamDetailPageView

app_name = "teams"

urlpatterns = [
    path("<int:pk>/", TeamDetailPageView.as_view(), name="team-page-detail"),
]