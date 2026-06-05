from django.db.models import Count, Q
from django.db.models.functions import TruncDate

from matches.models import Match, MatchEvent
from teams.models import Team


GOAL_EVENT_TYPES = [
    MatchEvent.EventType.GOAL,
    MatchEvent.EventType.PENALTY_GOAL,
    MatchEvent.EventType.OWN_GOAL,
]

CARD_EVENT_TYPES = [
    MatchEvent.EventType.YELLOW_CARD,
    MatchEvent.EventType.RED_CARD,
    MatchEvent.EventType.SECOND_YELLOW_RED,
]


def get_tournament_tactical_dashboard():
    finished_matches = Match.objects.filter(status=Match.Status.FINISHED)
    all_events = MatchEvent.objects.select_related("team", "match")

    total_matches = finished_matches.count()
    total_teams = Team.objects.filter(is_active=True).count()
    total_events = all_events.count()
    total_goals = all_events.filter(event_type__in=GOAL_EVENT_TYPES).count()
    total_cards = all_events.filter(event_type__in=CARD_EVENT_TYPES).count()
    total_key_events = all_events.filter(is_key_event=True).count()

    avg_goals_per_match = round(total_goals / total_matches, 2) if total_matches else 0
    avg_events_per_match = round(total_events / total_matches, 2) if total_matches else 0

    top_scoring_teams = Team.objects.filter(is_active=True).annotate(
        goals=Count("match_events", filter=Q(match_events__event_type__in=GOAL_EVENT_TYPES)),
        key_events=Count("match_events", filter=Q(match_events__is_key_event=True)),
    ).order_by("-goals", "-key_events", "name")[:5]

    most_disciplined_teams = Team.objects.filter(is_active=True).annotate(
        cards=Count("match_events", filter=Q(match_events__event_type__in=CARD_EVENT_TYPES))
    ).order_by("cards", "name")[:5]

    least_disciplined_teams = Team.objects.filter(is_active=True).annotate(
        cards=Count("match_events", filter=Q(match_events__event_type__in=CARD_EVENT_TYPES))
    ).order_by("-cards", "name")[:5]

    event_timeline = list(
        MatchEvent.objects.annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(
            total=Count("id"),
            goals=Count("id", filter=Q(event_type__in=GOAL_EVENT_TYPES)),
            cards=Count("id", filter=Q(event_type__in=CARD_EVENT_TYPES)),
            key_events=Count("id", filter=Q(is_key_event=True)),
        )
        .order_by("day")
    )

    matches_timeline = list(
        Match.objects.filter(status=Match.Status.FINISHED)
        .annotate(day=TruncDate("match_date"))
        .values("day")
        .annotate(total=Count("id"))
        .order_by("day")
    )

    tactical_alerts = []

    if avg_goals_per_match >= 3:
        tactical_alerts.append("El torneo muestra una media goleadora alta, lo que sugiere partidos abiertos o defensas poco estables.")
    else:
        tactical_alerts.append("La media goleadora es moderada o baja, lo que apunta a un torneo más controlado y competitivo.")

    if total_cards > total_goals:
        tactical_alerts.append("La disciplina está teniendo mucho peso en el torneo, con más acciones disciplinarias que goles registrados.")

    if total_key_events >= total_matches * 3 and total_matches > 0:
        tactical_alerts.append("El volumen de eventos clave por partido es alto, señal de encuentros con bastante actividad decisiva.")

    return {
        "summary": {
            "total_matches": total_matches,
            "total_teams": total_teams,
            "total_events": total_events,
            "total_goals": total_goals,
            "total_cards": total_cards,
            "total_key_events": total_key_events,
            "avg_goals_per_match": avg_goals_per_match,
            "avg_events_per_match": avg_events_per_match,
        },
        "top_scoring_teams": top_scoring_teams,
        "most_disciplined_teams": most_disciplined_teams,
        "least_disciplined_teams": least_disciplined_teams,
        "event_timeline": event_timeline,
        "matches_timeline": matches_timeline,
        "tactical_alerts": tactical_alerts,
    }