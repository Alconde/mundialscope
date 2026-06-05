from django.urls import path
from .views import MatchDetailPageView, TournamentTacticalDashboardView, GroupStandingsPageView
app_name = "matches"

urlpatterns = [
    path("tactical-dashboard/", TournamentTacticalDashboardView.as_view(), name="tactical-dashboard"),
    path("<int:pk>/", MatchDetailPageView.as_view(), name="match-page-detail"),
    path("groups/", GroupStandingsPageView.as_view(), name="group-standings"),
    
]