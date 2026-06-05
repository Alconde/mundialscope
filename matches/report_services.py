from django.utils.text import slugify

from matches.models import MatchEvent, MatchReport
from matches.ai_report_services import generate_match_ai_analysis
from ai.services import AIServiceError

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


def minute_label(event):
    if event.extra_minute:
        return f"{event.minute}+{event.extra_minute}'"
    return f"{event.minute}'"


def build_match_report_content(match):
    events = match.events.select_related("team", "player", "related_player").all()

    home_name = match.home_team.name
    away_name = match.away_team.name
    scoreline = f"{match.home_score} - {match.away_score}"

    if match.home_score > match.away_score:
        result_line = f"{home_name} derrotó a {away_name} por {scoreline}."
    elif match.home_score < match.away_score:
        result_line = f"{away_name} derrotó a {home_name} por {match.away_score} - {match.home_score}."
    else:
        result_line = f"{home_name} y {away_name} empataron {scoreline}."

    intro = (
        f"Partido correspondiente a {match.stage} del torneo {match.tournament.name} {match.tournament.year}, "
        f"disputado en {match.city or 'sede no disponible'}."
    )

    goal_events = [event for event in events if event.event_type in GOAL_TYPES]
    card_events = [event for event in events if event.event_type in CARD_TYPES]
    key_events = [event for event in events if event.is_key_event]

    if goal_events:
        goal_lines = []
        for event in goal_events:
            scorer = f"{event.player.first_name} {event.player.last_name}" if event.player else "Jugador no especificado"
            goal_lines.append(f"{minute_label(event)}: gol para {event.team.name}, anotado por {scorer}.")
        goals_text = "\n".join(goal_lines)
    else:
        goals_text = "No se registraron goles en la cronología del partido."

    if card_events:
        card_lines = []
        for event in card_events:
            player_name = f"{event.player.first_name} {event.player.last_name}" if event.player else "Jugador no especificado"
            card_lines.append(
                f"{minute_label(event)}: {event.get_event_type_display()} para {player_name} ({event.team.name})."
            )
        cards_text = "\n".join(card_lines)
    else:
        cards_text = "No se registraron tarjetas en este encuentro."

    if key_events:
        key_lines = []
        for event in key_events[:6]:
            label = event.title if event.title else event.get_event_type_display()
            key_lines.append(f"- {minute_label(event)} · {event.team.name} · {label}")
        key_points = "\n".join(key_lines)
    else:
        key_points = "- No hay eventos clave marcados todavía."

    tactical_notes = (
        f"{home_name} marcó {match.home_score} goles y {away_name} marcó {match.away_score}. "
        f"Se registraron {len(goal_events)} eventos de gol, {len(card_events)} eventos disciplinarios "
        f"y {len(key_events)} eventos clave. "
        "Esta versión del informe es automática y sirve como base inicial para análisis posterior."
    )

    summary = "\n\n".join([
        result_line,
        intro,
        "Goles y acciones decisivas:",
        goals_text,
        "Disciplina y control del partido:",
        cards_text,
    ])

    title = f"Informe automático: {home_name} vs {away_name}"
    slug = slugify(f"informe-{match.id}-{home_name}-{away_name}")

    return {
        "title": title,
        "slug": slug,
        "summary": summary,
        "key_points": key_points,
        "tactical_notes": tactical_notes,
    }


def generate_match_report(match):
    content = build_match_report_content(match)

    ai_content = {
        "headline": "",
        "summary": "",
        "tactical_reading": "",
        "key_takeaways": [],
    }

    try:
        ai_content = generate_match_ai_analysis(match)
    except AIServiceError:
        pass

    report, _ = MatchReport.objects.update_or_create(
        match=match,
        defaults={
            "title": content["title"],
            "slug": content["slug"],
            "summary": content["summary"],
            "key_points": content["key_points"],
            "tactical_notes": content["tactical_notes"],
            "ai_headline": ai_content.get("headline", ""),
            "ai_summary": ai_content.get("summary", ""),
            "ai_tactical_reading": ai_content.get("tactical_reading", ""),
            "ai_key_takeaways": "\n".join(ai_content.get("key_takeaways", [])),
            "is_auto_generated": True,
        },
    )
    return report