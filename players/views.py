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
    paginate_by = 12

    def get_queryset(self):
        queryset = Player.objects.select_related("team").all().order_by("last_name", "first_name")

        team = self.request.GET.get("team")
        position = self.request.GET.get("position")
        called_up = self.request.GET.get("called_up")
        search = self.request.GET.get("search")

        if team:
            queryset = queryset.filter(team_id=team)

        if position:
            queryset = queryset.filter(position=position)

        if called_up == "yes":
            queryset = queryset.filter(is_called_up=True)
        elif called_up == "no":
            queryset = queryset.filter(is_called_up=False)

        if search:
            queryset = queryset.filter(
                first_name__icontains=search
            ) | queryset.filter(
                last_name__icontains=search
            ) | queryset.filter(
                club__icontains=search
            ) | queryset.filter(
                team__name__icontains=search
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(is_active=True).order_by("name")
        context["selected_team"] = self.request.GET.get("team", "")
        context["selected_position"] = self.request.GET.get("position", "")
        context["selected_called_up"] = self.request.GET.get("called_up", "")
        context["search_value"] = self.request.GET.get("search", "")
        context["position_choices"] = Player.Position.choices
        return context


class PlayerDetailPageView(DetailView):
    model = Player
    template_name = "players/player_detail.html"
    context_object_name = "player"

    def get_queryset(self):
        return Player.objects.select_related("team").prefetch_related("match_events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["player_stats"] = build_player_stats(self.object)
        return context