from matches.models import Match, MatchEvent
from players.models import Player


GOAL_EVENT_TYPES = [
    MatchEvent.EventType.GOAL,
    MatchEvent.EventType.PENALTY_GOAL,
]

CARD_EVENT_TYPES = [
    MatchEvent.EventType.YELLOW_CARD,
    MatchEvent.EventType.RED_CARD,
    MatchEvent.EventType.SECOND_YELLOW_RED,
]


def get_team_comparison_stats(team):
    matches = Match.objects.filter(
        status=Match.Status.FINISHED
    ).filter(
        home_team=team
    ) | Match.objects.filter(
        status=Match.Status.FINISHED
    ).filter(
        away_team=team
    )

    matches = matches.distinct().order_by("-match_date")

    played = 0
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0
    points = 0

    for match in matches:
        is_home = match.home_team_id == team.id
        scored = match.home_score if is_home else match.away_score
        conceded = match.away_score if is_home else match.home_score

        played += 1
        goals_for += scored
        goals_against += conceded

        if scored > conceded:
            wins += 1
            points += 3
        elif scored < conceded:
            losses += 1
        else:
            draws += 1
            points += 1

    total_players = Player.objects.filter(team=team, is_called_up=True).count()

    total_goals_events = MatchEvent.objects.filter(
        team=team,
        event_type__in=GOAL_EVENT_TYPES
    ).count()

    total_cards = MatchEvent.objects.filter(
        team=team,
        event_type__in=CARD_EVENT_TYPES
    ).count()

    key_events = MatchEvent.objects.filter(
        team=team,
        is_key_event=True
    ).count()

    avg_goals_for = round(goals_for / played, 2) if played else 0
    avg_goals_against = round(goals_against / played, 2) if played else 0
    goal_difference = goals_for - goals_against

    return {
        "team": team,
        "played": played,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "points": points,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goal_difference": goal_difference,
        "avg_goals_for": avg_goals_for,
        "avg_goals_against": avg_goals_against,
        "total_players": total_players,
        "event_goals": total_goals_events,
        "cards": total_cards,
        "key_events": key_events,
    }


def build_team_comparison(team_a, team_b):
    stats_a = get_team_comparison_stats(team_a)
    stats_b = get_team_comparison_stats(team_b)

    comparison_rows = [
        ("Puntos", stats_a["points"], stats_b["points"]),
        ("Partidos jugados", stats_a["played"], stats_b["played"]),
        ("Victorias", stats_a["wins"], stats_b["wins"]),
        ("Empates", stats_a["draws"], stats_b["draws"]),
        ("Derrotas", stats_a["losses"], stats_b["losses"]),
        ("Goles a favor", stats_a["goals_for"], stats_b["goals_for"]),
        ("Goles en contra", stats_a["goals_against"], stats_b["goals_against"]),
        ("Diferencia de goles", stats_a["goal_difference"], stats_b["goal_difference"]),
        ("Promedio GF", stats_a["avg_goals_for"], stats_b["avg_goals_for"]),
        ("Promedio GC", stats_a["avg_goals_against"], stats_b["avg_goals_against"]),
        ("Convocados", stats_a["total_players"], stats_b["total_players"]),
        ("Goles por eventos", stats_a["event_goals"], stats_b["event_goals"]),
        ("Tarjetas", stats_a["cards"], stats_b["cards"]),
        ("Eventos clave", stats_a["key_events"], stats_b["key_events"]),
    ]

    bar_chart = {
        "categories": ["Puntos", "Victorias", "GF", "DG", "Tarjetas", "Eventos clave"],
        "team_a_name": stats_a["team"].name,
        "team_b_name": stats_b["team"].name,
        "team_a_values": [
            stats_a["points"],
            stats_a["wins"],
            stats_a["goals_for"],
            stats_a["goal_difference"],
            stats_a["cards"],
            stats_a["key_events"],
        ],
        "team_b_values": [
            stats_b["points"],
            stats_b["wins"],
            stats_b["goals_for"],
            stats_b["goal_difference"],
            stats_b["cards"],
            stats_b["key_events"],
        ],
    }

    radar_chart = {
        "categories": ["Puntos", "Victorias", "GF", "DG", "Clave", "Convocados"],
        "team_a_name": stats_a["team"].name,
        "team_b_name": stats_b["team"].name,
        "team_a_values": [
            stats_a["points"],
            stats_a["wins"],
            stats_a["goals_for"],
            max(stats_a["goal_difference"], 0),
            stats_a["key_events"],
            stats_a["total_players"],
        ],
        "team_b_values": [
            stats_b["points"],
            stats_b["wins"],
            stats_b["goals_for"],
            max(stats_b["goal_difference"], 0),
            stats_b["key_events"],
            stats_b["total_players"],
        ],
    }

    return {
        "team_a_stats": stats_a,
        "team_b_stats": stats_b,
        "comparison_rows": comparison_rows,
        "bar_chart": bar_chart,
        "radar_chart": radar_chart,
    }