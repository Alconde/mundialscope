from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            "id",
            "name",
            "fifa_code",
            "confederation",
            "coach",
            "fifa_ranking",
            "group",
            "primary_color",
            "secondary_color",
            "is_active",
        ]