from collections import defaultdict

from matches.models import Match
from teams.models import Team


def build_group_standings():
    teams = Team.objects.filter(is_active=True).order_by("group", "name")
    finished_group_matches = Match.objects.select_related(
        "home_team",
        "away_team",
    ).filter(
        stage=Match.Stage.GROUP,
        status=Match.Status.FINISHED,
    ).order_by("match_date")

    standings = defaultdict(list)
    standings_index = {}

    for team in teams:
        if not team.group:
            continue

        standings_index[team.id] = {
            "team": team,
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0,
        }

    for match in finished_group_matches:
        home = standings_index.get(match.home_team_id)
        away = standings_index.get(match.away_team_id)

        if not home or not away:
            continue

        home["played"] += 1
        away["played"] += 1

        home["goals_for"] += match.home_score
        home["goals_against"] += match.away_score
        away["goals_for"] += match.away_score
        away["goals_against"] += match.home_score

        if match.home_score > match.away_score:
            home["wins"] += 1
            home["points"] += 3
            away["losses"] += 1
        elif match.home_score < match.away_score:
            away["wins"] += 1
            away["points"] += 3
            home["losses"] += 1
        else:
            home["draws"] += 1
            away["draws"] += 1
            home["points"] += 1
            away["points"] += 1

    for item in standings_index.values():
        item["goal_difference"] = item["goals_for"] - item["goals_against"]
        standings[item["team"].group].append(item)

    for group, rows in standings.items():
        rows.sort(
            key=lambda row: (
                -row["points"],
                -row["goal_difference"],
                -row["goals_for"],
                row["team"].name,
            )
        )

    return dict(sorted(standings.items()))