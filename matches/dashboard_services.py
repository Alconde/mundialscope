from collections import defaultdict

from django.db.models import Count, Q, Sum
from django.utils import timezone

from matches.models import Match, Tournament
from teams.models import Team


def get_active_world_cup():
    return Tournament.objects.filter(
        tournament_type=Tournament.TournamentType.WORLD_CUP,
        is_active=True,
    ).order_by("-year").first()


def get_dashboard_kpis(tournament):
    matches = Match.objects.filter(tournament=tournament)

    total_matches = matches.count()
    finished_matches = matches.filter(status=Match.Status.FINISHED).count()
    live_matches = matches.filter(status=Match.Status.LIVE).count()
    scheduled_matches = matches.filter(status=Match.Status.SCHEDULED).count()

    goals_data = matches.aggregate(
        home_goals=Sum("home_score"),
        away_goals=Sum("away_score"),
    )
    total_goals = (goals_data["home_goals"] or 0) + (goals_data["away_goals"] or 0)

    total_teams = Team.objects.filter(
        Q(home_matches__tournament=tournament) | Q(away_matches__tournament=tournament)
    ).distinct().count()

    return {
        "total_matches": total_matches,
        "finished_matches": finished_matches,
        "live_matches": live_matches,
        "scheduled_matches": scheduled_matches,
        "total_goals": total_goals,
        "total_teams": total_teams,
    }


def get_upcoming_matches(tournament, limit=8):
    now = timezone.now()
    return Match.objects.filter(
        tournament=tournament,
        match_date__gte=now,
    ).select_related("home_team", "away_team").order_by("match_date")[:limit]


def get_recent_results(tournament, limit=8):
    return Match.objects.filter(
        tournament=tournament,
        status=Match.Status.FINISHED,
    ).select_related("home_team", "away_team").order_by("-match_date")[:limit]


def build_group_tables(tournament):
    matches = Match.objects.filter(
        tournament=tournament,
        status=Match.Status.FINISHED,
        stage=Match.Stage.GROUP,
    ).select_related("home_team", "away_team").order_by("match_date")

    group_data = defaultdict(lambda: defaultdict(lambda: {
        "team": None,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "goal_difference": 0,
        "points": 0,
    }))

    for match in matches:
        if not match.group:
            continue

        home = group_data[match.group][match.home_team_id]
        away = group_data[match.group][match.away_team_id]

        home["team"] = match.home_team
        away["team"] = match.away_team

        home["played"] += 1
        away["played"] += 1

        home["goals_for"] += match.home_score
        home["goals_against"] += match.away_score
        away["goals_for"] += match.away_score
        away["goals_against"] += match.home_score

        if match.home_score > match.away_score:
            home["wins"] += 1
            away["losses"] += 1
            home["points"] += 3
        elif match.home_score < match.away_score:
            away["wins"] += 1
            home["losses"] += 1
            away["points"] += 3
        else:
            home["draws"] += 1
            away["draws"] += 1
            home["points"] += 1
            away["points"] += 1

    tables = []

    for group_letter, teams_stats in sorted(group_data.items()):
        rows = list(teams_stats.values())

        for row in rows:
            row["goal_difference"] = row["goals_for"] - row["goals_against"]

        rows.sort(
            key=lambda item: (
                -item["points"],
                -item["goal_difference"],
                -item["goals_for"],
                item["team"].name,
            )
        )

        tables.append({
            "group": group_letter,
            "rows": rows,
        })

    return tables


def get_team_rankings(tournament, limit=6):
    teams = Team.objects.filter(
        Q(home_matches__tournament=tournament) | Q(away_matches__tournament=tournament)
    ).distinct()

    ranking_rows = []

    for team in teams:
        finished_matches = Match.objects.filter(
            tournament=tournament,
            status=Match.Status.FINISHED,
        ).filter(
            Q(home_team=team) | Q(away_team=team)
        )

        played = finished_matches.count()
        points = 0
        goals_for = 0
        goals_against = 0
        wins = 0

        for match in finished_matches:
            is_home = match.home_team_id == team.id
            scored = match.home_score if is_home else match.away_score
            conceded = match.away_score if is_home else match.home_score

            goals_for += scored
            goals_against += conceded

            if scored > conceded:
                wins += 1
                points += 3
            elif scored == conceded:
                points += 1

        ranking_rows.append({
            "team": team,
            "played": played,
            "wins": wins,
            "points": points,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_difference": goals_for - goals_against,
        })

    ranking_rows.sort(
        key=lambda item: (
            -item["points"],
            -item["goal_difference"],
            -item["goals_for"],
            item["team"].name,
        )
    )

    return ranking_rows[:limit]


def get_dashboard_context():
    tournament = get_active_world_cup()

    if not tournament:
        return {
            "tournament": None,
            "kpis": {},
            "upcoming_matches": [],
            "recent_results": [],
            "group_tables": [],
            "top_teams": [],
        }

    return {
        "tournament": tournament,
        "kpis": get_dashboard_kpis(tournament),
        "upcoming_matches": get_upcoming_matches(tournament),
        "recent_results": get_recent_results(tournament),
        "group_tables": build_group_tables(tournament),
        "top_teams": get_team_rankings(tournament),
    }