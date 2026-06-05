from matches.models import MatchEvent


def build_player_stats(player):
    events = player.match_events.select_related(
        "match",
        "team",
    ).order_by("-minute", "-extra_minute")

    goals = 0
    yellow_cards = 0
    red_cards = 0
    key_events = 0

    for event in events:
        if event.event_type in [
            MatchEvent.EventType.GOAL,
            MatchEvent.EventType.PENALTY_GOAL,
        ]:
            goals += 1

        if event.event_type == MatchEvent.EventType.YELLOW_CARD:
            yellow_cards += 1

        if event.event_type in [
            MatchEvent.EventType.RED_CARD,
            MatchEvent.EventType.SECOND_YELLOW_RED,
        ]:
            red_cards += 1

        if event.is_key_event:
            key_events += 1

    return {
        "goals": goals,
        "yellow_cards": yellow_cards,
        "red_cards": red_cards,
        "key_events": key_events,
        "recent_events": events[:10],
    }