from django.contrib import admin
from .models import Tournament, Match, MatchEvent


class MatchEventInline(admin.TabularInline):
    model = MatchEvent
    extra = 1
    fields = (
        "minute",
        "extra_minute",
        "event_type",
        "team",
        "player",
        "related_player",
        "is_key_event",
        "title",
        "description",
    )


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "host_country", "start_date", "end_date", "is_active")
    list_filter = ("year", "tournament_type", "is_active")
    search_fields = ("name", "host_country")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tournament",
        "home_team",
        "away_team",
        "match_date",
        "stage",
        "status",
        "home_score",
        "away_score",
    )
    list_filter = ("tournament", "stage", "status", "group")
    search_fields = ("home_team__name", "away_team__name", "stadium", "city")
    inlines = [MatchEventInline]


@admin.register(MatchEvent)
class MatchEventAdmin(admin.ModelAdmin):
    list_display = ("match", "minute", "event_type", "team", "player", "is_key_event")
    list_filter = ("event_type", "team", "is_key_event")
    search_fields = ("match__home_team__name", "match__away_team__name", "player__last_name", "title")