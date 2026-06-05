from rest_framework import serializers
from .models import Tournament, Match


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = [
            "id",
            "name",
            "year",
            "host_country",
            "tournament_type",
            "start_date",
            "end_date",
            "is_active",
        ]


class MatchSerializer(serializers.ModelSerializer):
    tournament_name = serializers.CharField(source="tournament.name", read_only=True)
    home_team_name = serializers.CharField(source="home_team.name", read_only=True)
    away_team_name = serializers.CharField(source="away_team.name", read_only=True)

    class Meta:
        model = Match
        fields = [
            "id",
            "tournament",
            "tournament_name",
            "home_team",
            "home_team_name",
            "away_team",
            "away_team_name",
            "stage",
            "group",
            "match_date",
            "stadium",
            "city",
            "status",
            "home_score",
            "away_score",
        ]