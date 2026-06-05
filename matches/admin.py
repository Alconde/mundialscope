from django.contrib import admin
from .models import Tournament, Match


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "host_country", "tournament_type", "is_active")
    list_filter = ("tournament_type", "is_active", "year")
    search_fields = ("name", "host_country")
    ordering = ("-year", "name")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "tournament",
        "home_team",
        "away_team",
        "stage",
        "group",
        "match_date",
        "status",
        "home_score",
        "away_score",
    )
    list_filter = ("stage", "status", "group", "tournament")
    search_fields = ("home_team__name", "away_team__name", "stadium", "city")
    ordering = ("match_date",)