from django.urls import path
from .views import TeamListPageView, TeamDetailPageView, TeamComparisonPageView

app_name = "teams"

urlpatterns = [
    path("", TeamListPageView.as_view(), name="team-list"),
    path("compare/", TeamComparisonPageView.as_view(), name="team-compare"),
    path("<int:pk>/", TeamDetailPageView.as_view(), name="team-detail"),
]