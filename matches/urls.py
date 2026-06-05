from django.urls import path
from .views import MatchListPageView, MatchDetailPageView, GroupStandingsPageView

app_name = "matches"

urlpatterns = [
    path("groups/", GroupStandingsPageView.as_view(), name="group-standings"),
    path("", MatchListPageView.as_view(), name="match-page-list"),
    path("<int:pk>/", MatchDetailPageView.as_view(), name="match-page-detail"),
]