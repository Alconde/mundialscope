from django.db.models import Count, Q
from django.shortcuts import render
from django.utils import timezone

from matches.models import Match, Tournament
from players.models import Player
from teams.models import Team
from matches.services import build_group_standings


def home(request):
    now = timezone.now()

    active_tournament = Tournament.objects.filter(is_active=True).order_by("-year").first()

    next_matches = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        match_date__gte=now
    ).order_by("match_date")[:6]

    live_matches = Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        status="live"
    ).order_by("match_date")

    featured_teams = Team.objects.filter(is_active=True).order_by("name")[:8]

    teams_by_group = (
        Team.objects.filter(is_active=True)
        .values("group")
        .annotate(total=Count("id"))
        .order_by("group")
    )

    top_ranked_teams = Team.objects.filter(
        is_active=True,
        fifa_ranking__isnull=False
    ).order_by("fifa_ranking")[:5]

    top_squads = Team.objects.filter(is_active=True).annotate(
        player_count=Count("players", filter=Q(players__is_called_up=True))
    ).order_by("-player_count", "name")[:5]

    group_standings = build_group_standings()

    context = {
        "active_tournament": active_tournament,
        "total_teams": Team.objects.filter(is_active=True).count(),
        "total_players": Player.objects.filter(is_called_up=True).count(),
        "total_matches": Match.objects.count(),
        "live_matches_count": live_matches.count(),
        "next_matches": next_matches,
        "live_matches": live_matches,
        "featured_teams": featured_teams,
        "teams_by_group": teams_by_group,
        "top_ranked_teams": top_ranked_teams,
        "top_squads": top_squads,
        "group_standings": group_standings,
    }

    return render(request, "core/home.html", context)