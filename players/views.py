from django.views.generic import ListView, DetailView
from rest_framework import generics

from .models import Player
from .serializers import PlayerSerializer
from teams.models import Team
from .services import build_player_stats


class PlayerListAPIView(generics.ListAPIView):
    queryset = Player.objects.select_related("team").all()
    serializer_class = PlayerSerializer
    filterset_fields = ["team", "position", "is_called_up"]
    search_fields = ["first_name", "last_name", "club", "team__name"]
    ordering_fields = ["last_name", "shirt_number", "market_value"]
    ordering = ["last_name", "first_name"]


class PlayerDetailAPIView(generics.RetrieveAPIView):
    queryset = Player.objects.select_related("team").all()
    serializer_class = PlayerSerializer


class PlayerListPageView(ListView):
    model = Player
    template_name = "players/player_list.html"
    context_object_name = "players"
    paginate_by = 20

    def get_queryset(self):
        queryset = (
            Player.objects.select_related("team")
            .filter(is_called_up=True)
            .order_by("team__name", "position", "last_name", "first_name")
        )

        team_id = self.request.GET.get("team")
        position = self.request.GET.get("position")
        search = self.request.GET.get("q")

        if team_id:
            queryset = queryset.filter(team_id=team_id)

        if position:
            queryset = queryset.filter(position=position)

        if search:
            queryset = queryset.filter(
                first_name__icontains=search
            ) | queryset.filter(
                last_name__icontains=search
            ) | queryset.filter(
                club__icontains=search
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(is_active=True).order_by("name")
        context["positions"] = Player.Position.choices
        context["selected_team"] = self.request.GET.get("team", "")
        context["selected_position"] = self.request.GET.get("position", "")
        context["search_query"] = self.request.GET.get("q", "")
        return context


class PlayerDetailPageView(DetailView):
    model = Player
    template_name = "players/player_detail.html"
    context_object_name = "player"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.object
        context["recent_events"] = player.match_events.select_related(
            "match", "team"
        ).order_by("-created_at")[:10]
        return context