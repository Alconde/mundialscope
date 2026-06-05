from django.urls import path
from .views import TeamDetailPageView, TeamComparisonPageView

app_name = "teams"

urlpatterns = [
    path("compare/", TeamComparisonPageView.as_view(), name="team-compare"),
    path("<int:pk>/", TeamDetailPageView.as_view(), name="team-page-detail"),
]