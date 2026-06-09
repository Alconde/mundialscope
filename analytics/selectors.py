from django.db.models import Q
from teams.models import Team
from players.models import Player
from matches.models import Match


def get_all_teams():
    return Team.objects.all().order_by("name")


def get_team_by_id(team_id):
    return Team.objects.get(pk=team_id)


def get_team_players(team):
    return (
        Player.objects.filter(team=team, is_called_up=True)
        .select_related("team")
        .order_by("shirt_number", "last_name", "first_name")
    )


def get_team_matches(team):
    return (
        Match.objects.filter(Q(home_team=team) | Q(away_team=team))
        .select_related("home_team", "away_team")
        .order_by("-match_date")
    )


def get_all_called_up_players():
    return (
        Player.objects.filter(is_called_up=True)
        .select_related("team")
        .order_by("team__name", "position", "last_name", "first_name")
    )


def get_player_by_id(player_id):
    return Player.objects.select_related("team").get(pk=player_id)


def get_all_matches():
    return Match.objects.select_related("home_team", "away_team").all()


def get_finished_matches():
    return (
        Match.objects.select_related("home_team", "away_team")
        .filter(status__in=["finished", "completed"])
    )


def get_team_dashboard_queryset(group=None):
    queryset = Team.objects.all().order_by("name")
    if group:
        queryset = queryset.filter(group__iexact=group)
    return queryset


def get_player_dashboard_queryset(team_id=None, position=None):
    queryset = Player.objects.filter(is_called_up=True).select_related("team")

    if team_id:
        queryset = queryset.filter(team_id=team_id)

    if position:
        queryset = queryset.filter(position=position)

    return queryset.order_by("team__name", "last_name", "first_name")