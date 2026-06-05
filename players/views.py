from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer


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