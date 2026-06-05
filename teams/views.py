from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer
from django.views.generic import DetailView
from .services import build_team_stats



class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ["confederation", "group", "is_active"]
    search_fields = ["name", "fifa_code", "coach"]
    ordering_fields = ["name", "fifa_ranking"]
    ordering = ["name"]


class TeamDetailAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ["confederation", "group", "is_active"]
    search_fields = ["name", "fifa_code", "coach"]
    ordering_fields = ["name", "fifa_ranking"]
    ordering = ["name"]


class TeamDetailAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailPageView(DetailView):
    model = Team
    template_name = "teams/team_detail.html"
    context_object_name = "team"

    def get_queryset(self):
        return Team.objects.prefetch_related("players")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team_stats"] = build_team_stats(self.object)
        return context