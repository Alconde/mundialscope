from django.db.models import Count, Q

from matches.models import Match, MatchEvent
from players.models import Player


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


def get_top_scorers(limit=10):
    return Player.objects.filter(
        match_events__event_type__in=GOAL_EVENT_TYPES
    ).annotate(
        goals=Count(
            "match_events",
            filter=Q(match_events__event_type__in=GOAL_EVENT_TYPES)
        )
    ).select_related("team").order_by("-goals", "last_name", "first_name")[:limit]


def get_top_carded_players(limit=10):
    return Player.objects.filter(
        match_events__event_type__in=CARD_EVENT_TYPES
    ).annotate(
        yellow_cards=Count(
            "match_events",
            filter=Q(match_events__event_type=MatchEvent.EventType.YELLOW_CARD)
        ),
        red_cards=Count(
            "match_events",
            filter=Q(
                match_events__event_type__in=[
                    MatchEvent.EventType.RED_CARD,
                    MatchEvent.EventType.SECOND_YELLOW_RED,
                ]
            )
        ),
        total_cards=Count(
            "match_events",
            filter=Q(match_events__event_type__in=CARD_EVENT_TYPES)
        ),
    ).select_related("team").order_by("-total_cards", "-red_cards", "last_name")[:limit]


def get_most_eventful_matches(limit=5):
    return Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).annotate(
        total_events=Count("events"),
        key_events=Count("events", filter=Q(events__is_key_event=True)),
        goals=Count("events", filter=Q(events__event_type__in=GOAL_EVENT_TYPES)),
        cards=Count("events", filter=Q(events__event_type__in=CARD_EVENT_TYPES)),
    ).order_by("-key_events", "-total_events", "-match_date")[:limit]


def get_events_summary():
    return MatchEvent.objects.aggregate(
        total_events=Count("id"),
        total_goals=Count("id", filter=Q(event_type__in=GOAL_EVENT_TYPES)),
        total_cards=Count("id", filter=Q(event_type__in=CARD_EVENT_TYPES)),
        total_key_events=Count("id", filter=Q(is_key_event=True)),
    )