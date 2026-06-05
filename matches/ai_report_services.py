from ai.services import generate_structured_football_analysis, AIServiceError
from matches.models import MatchEvent


GOAL_TYPES = [
    MatchEvent.EventType.GOAL,
    MatchEvent.EventType.PENALTY_GOAL,
    MatchEvent.EventType.OWN_GOAL,
]

CARD_TYPES = [
    MatchEvent.EventType.YELLOW_CARD,
    MatchEvent.EventType.RED_CARD,
    MatchEvent.EventType.SECOND_YELLOW_RED,
]


def build_match_ai_prompt(match):
    events = match.events.select_related("team", "player").all().order_by("minute", "extra_minute")

    event_lines = []
    for event in events[:25]:
        player_name = ""
        if event.player:
            player_name = f" · {event.player.first_name} {event.player.last_name}"

        extra = f"+{event.extra_minute}" if event.extra_minute else ""
        event_lines.append(
            f"- {event.minute}{extra}' | {event.team.name} | {event.get_event_type_display()}{player_name}"
        )

    events_text = "\n".join(event_lines) if event_lines else "- Sin eventos detallados"

    return f"""
Eres un analista táctico profesional especializado en fútbol internacional.
Analiza este partido del Mundial de forma breve, clara y profesional.

PARTIDO:
- Torneo: {match.tournament.name} {match.tournament.year}
- Fase: {match.stage}
- Partido: {match.home_team.name} vs {match.away_team.name}
- Resultado: {match.home_score}-{match.away_score}
- Estado: {match.status}
- Ciudad: {match.city or "No disponible"}

EVENTOS:
{events_text}

Devuelve un análisis estructurado en español.
""".strip()


def generate_match_ai_analysis(match):
    schema = {
        "type": "object",
        "properties": {
            "headline": {"type": "string"},
            "summary": {"type": "string"},
            "tactical_reading": {"type": "string"},
            "key_takeaways": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 3,
                "maxItems": 5
            }
        },
        "required": ["headline", "summary", "tactical_reading", "key_takeaways"],
        "additionalProperties": False
    }

    prompt = build_match_ai_prompt(match)
    return generate_structured_football_analysis(prompt, schema)