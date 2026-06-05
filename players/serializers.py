from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name", read_only=True)

    class Meta:
        model = Player
        fields = [
            "id",
            "team",
            "team_name",
            "first_name",
            "last_name",
            "shirt_number",
            "position",
            "date_of_birth",
            "club",
            "market_value",
            "is_called_up",
        ]