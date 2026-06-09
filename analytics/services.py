from collections import Counter

from django.db.models import Count

from .selectors import (
    get_all_teams,
    get_all_called_up_players,
    get_all_matches,
    get_finished_matches,
    get_team_dashboard_queryset,
    get_team_matches,
    get_team_players,
    get_player_dashboard_queryset,
)
from .utils import safe_divide, build_player_full_name, normalize_ordering
from .constants import TEAM_DASHBOARD_DEFAULT_ORDER, PLAYER_DASHBOARD_DEFAULT_ORDER


def calculate_team_standings(team):
    matches = get_team_matches(team)

    played = 0
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0

    for match in matches:
        if match.home_score is None or match.away_score is None:
            continue

        played += 1

        if match.home_team_id == team.id:
            gf = match.home_score
            ga = match.away_score
        else:
            gf = match.away_score
            ga = match.home_score

        goals_for += gf
        goals_against += ga

        if gf > ga:
            wins += 1
        elif gf == ga:
            draws += 1
        else:
            losses += 1

    points = wins * 3 + draws
    goal_difference = goals_for - goals_against

    return {
        "played": played,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goal_difference": goal_difference,
        "points": points,
    }


def build_home_dashboard():
    teams = list(get_all_teams())
    players = list(get_all_called_up_players())
    matches = list(get_all_matches())
    finished_matches = list(get_finished_matches())

    total_goals = 0
    for match in finished_matches:
        total_goals += (match.home_score or 0) + (match.away_score or 0)

    team_rows = []
    for team in teams:
        standings = calculate_team_standings(team)
        team_rows.append({
            "team": team,
            **standings,
        })

    team_rows = sorted(
        team_rows,
        key=lambda item: (
            item["points"],
            item["goal_difference"],
            item["goals_for"],
            item["team"].name,
        ),
        reverse=True,
    )

    player_rows = []
    for player in players:
        player_rows.append({
            "player": player,
            "full_name": build_player_full_name(player),
            "team": player.team,
            "minutes_played": getattr(player, "minutes_played", 0) or 0,
            "goals": getattr(player, "goals", 0) or 0,
            "assists": getattr(player, "assists", 0) or 0,
        })

    top_scorers = sorted(
        player_rows,
        key=lambda item: (item["goals"], item["assists"], item["minutes_played"]),
        reverse=True,
    )[:10]

    top_minutes = sorted(
        player_rows,
        key=lambda item: item["minutes_played"],
        reverse=True,
    )[:10]

    return {
        "kpis": {
            "teams_total": len(teams),
            "players_total": len(players),
            "matches_total": len(matches),
            "finished_matches_total": len(finished_matches),
            "goals_total": total_goals,
            "goals_per_match": round(safe_divide(total_goals, len(finished_matches)), 2),
        },
        "top_teams": team_rows[:8],
        "top_scorers": top_scorers,
        "top_minutes": top_minutes,
    }


def build_team_dashboard(filters=None):
    filters = filters or {}
    group = filters.get("group")
    ordering = normalize_ordering(
        filters.get("ordering"),
        allowed_values=["name", "-name", "points", "-points", "goals_for", "-goals_for", "goal_difference", "-goal_difference"],
        default=TEAM_DASHBOARD_DEFAULT_ORDER,
    )

    teams = list(get_team_dashboard_queryset(group=group))
    rows = []

    for team in teams:
        standings = calculate_team_standings(team)
        called_up_count = get_team_players(team).count()

        rows.append({
            "team": team,
            "called_up_count": called_up_count,
            **standings,
        })

    reverse = ordering.startswith("-")
    field = ordering.lstrip("-")

    rows = sorted(
        rows,
        key=lambda item: (
            item[field] if field in item else getattr(item["team"], field, ""),
            item["team"].name,
        ),
        reverse=reverse,
    )

    return {
        "team_rows": rows,
        "selected_group": group or "",
        "selected_ordering": ordering,
    }


def build_team_detail(team):
    standings = calculate_team_standings(team)
    players = list(get_team_players(team))
    matches = list(get_team_matches(team))

    position_distribution = Counter(player.position for player in players)

    player_rows = []
    for player in players:
        player_rows.append({
            "player": player,
            "full_name": build_player_full_name(player),
            "minutes_played": getattr(player, "minutes_played", 0) or 0,
            "goals": getattr(player, "goals", 0) or 0,
            "assists": getattr(player, "assists", 0) or 0,
        })

    top_players_by_minutes = sorted(
        player_rows,
        key=lambda item: item["minutes_played"],
        reverse=True,
    )[:8]

    top_players_by_goals = sorted(
        player_rows,
        key=lambda item: (item["goals"], item["assists"]),
        reverse=True,
    )[:8]

    return {
        "standings": standings,
        "players": players,
        "matches": matches,
        "squad_size": len(players),
        "position_distribution": position_distribution,
        "top_players_by_minutes": top_players_by_minutes,
        "top_players_by_goals": top_players_by_goals,
    }


def build_team_comparison(team_a, team_b):
    team_a_data = build_team_detail(team_a)
    team_b_data = build_team_detail(team_b)

    return {
        "team_a": {
            "team": team_a,
            **team_a_data["standings"],
            "squad_size": team_a_data["squad_size"],
        },
        "team_b": {
            "team": team_b,
            **team_b_data["standings"],
            "squad_size": team_b_data["squad_size"],
        },
    }


def build_player_dashboard(filters=None):
    filters = filters or {}
    team_id = filters.get("team")
    position = filters.get("position")
    ordering = normalize_ordering(
        filters.get("ordering"),
        allowed_values=["last_name", "-last_name", "minutes_played", "-minutes_played", "goals", "-goals", "assists", "-assists"],
        default=PLAYER_DASHBOARD_DEFAULT_ORDER,
    )

    players = list(get_player_dashboard_queryset(team_id=team_id, position=position))
    rows = []

    for player in players:
        minutes_played = getattr(player, "minutes_played", 0) or 0
        goals = getattr(player, "goals", 0) or 0
        assists = getattr(player, "assists", 0) or 0
        matches_played = getattr(player, "matches_played", 0) or 0
        cards = (getattr(player, "yellow_cards", 0) or 0) + (getattr(player, "red_cards", 0) or 0)

        rows.append({
            "player": player,
            "full_name": build_player_full_name(player),
            "team": player.team,
            "position": player.position,
            "club": player.club,
            "shirt_number": player.shirt_number,
            "minutes_played": minutes_played,
            "matches_played": matches_played,
            "goals": goals,
            "assists": assists,
            "cards": cards,
            "goal_contributions_per90": round(
                safe_divide((goals + assists) * 90, minutes_played), 2
            ),
        })

    reverse = ordering.startswith("-")
    field = ordering.lstrip("-")

    rows = sorted(
        rows,
        key=lambda item: item[field] if field in item else "",
        reverse=reverse,
    )

    return {
        "player_rows": rows,
        "selected_team": team_id or "",
        "selected_position": position or "",
        "selected_ordering": ordering,
    }


def build_player_detail(player):
    minutes_played = getattr(player, "minutes_played", 0) or 0
    goals = getattr(player, "goals", 0) or 0
    assists = getattr(player, "assists", 0) or 0
    matches_played = getattr(player, "matches_played", 0) or 0
    yellow_cards = getattr(player, "yellow_cards", 0) or 0
    red_cards = getattr(player, "red_cards", 0) or 0

    team_players = list(get_team_players(player.team))

    ranked_by_minutes = sorted(
        team_players,
        key=lambda item: getattr(item, "minutes_played", 0) or 0,
        reverse=True,
    )
    ranked_by_goals = sorted(
        team_players,
        key=lambda item: getattr(item, "goals", 0) or 0,
        reverse=True,
    )

    minutes_rank = next((index + 1 for index, p in enumerate(ranked_by_minutes) if p.id == player.id), None)
    goals_rank = next((index + 1 for index, p in enumerate(ranked_by_goals) if p.id == player.id), None)

    return {
        "full_name": build_player_full_name(player),
        "kpis": {
            "minutes_played": minutes_played,
            "matches_played": matches_played,
            "goals": goals,
            "assists": assists,
            "yellow_cards": yellow_cards,
            "red_cards": red_cards,
            "goal_contributions_per90": round(
                safe_divide((goals + assists) * 90, minutes_played), 2
            ),
        },
        "context": {
            "minutes_rank_in_team": minutes_rank,
            "goals_rank_in_team": goals_rank,
        },
    }


def build_player_comparison(player_a, player_b):
    player_a_data = build_player_detail(player_a)
    player_b_data = build_player_detail(player_b)

    return {
        "player_a": {
            "player": player_a,
            "full_name": player_a_data["full_name"],
            **player_a_data["kpis"],
        },
        "player_b": {
            "player": player_b,
            "full_name": player_b_data["full_name"],
            **player_b_data["kpis"],
        },
    }