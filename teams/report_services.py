from django.utils.text import slugify

from matches.models import Match, MatchEvent
from players.models import Player
from teams.models import TeamReport


GOAL_EVENT_TYPES = [
    MatchEvent.EventType.GOAL,
    MatchEvent.EventType.PENALTY_GOAL,
]

CARD_EVENT_TYPES = [
    MatchEvent.EventType.YELLOW_CARD,
    MatchEvent.EventType.RED_CARD,
    MatchEvent.EventType.SECOND_YELLOW_RED,
]


def get_team_matches(team):
    matches = Match.objects.filter(
        home_team=team
    ) | Match.objects.filter(
        away_team=team
    )
    return matches.select_related("home_team", "away_team", "tournament").order_by("-match_date").distinct()


def build_team_report_content(team):
    matches = list(get_team_matches(team))
    finished_matches = [match for match in matches if match.status == Match.Status.FINISHED]

    played = 0
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0
    last_results = []

    for match in finished_matches:
        is_home = match.home_team_id == team.id
        scored = match.home_score if is_home else match.away_score
        conceded = match.away_score if is_home else match.home_score
        opponent = match.away_team.name if is_home else match.home_team.name

        played += 1
        goals_for += scored
        goals_against += conceded

        if scored > conceded:
            wins += 1
            result = "victoria"
        elif scored < conceded:
            losses += 1
            result = "derrota"
        else:
            draws += 1
            result = "empate"

        last_results.append(f"- {team.name} {scored}-{conceded} {opponent}: {result}")

    called_up_players = Player.objects.filter(team=team, is_called_up=True).order_by("position", "last_name", "first_name")
    total_called_up = called_up_players.count()

    goals = MatchEvent.objects.filter(team=team, event_type__in=GOAL_EVENT_TYPES).count()
    cards = MatchEvent.objects.filter(team=team, event_type__in=CARD_EVENT_TYPES).count()
    key_events = MatchEvent.objects.filter(team=team, is_key_event=True).count()

    summary = (
        f"{team.name} compite en la confederación {team.confederation} "
        f"y actualmente forma parte del grupo {team.group or 'sin grupo asignado'}. "
        f"Ha disputado {played} partidos finalizados, con un balance de {wins} victorias, "
        f"{draws} empates y {losses} derrotas."
    )

    performance_overview = (
        f"La selección ha marcado {goals_for} goles y ha recibido {goals_against} en partidos finalizados. "
        f"Además, en la base de eventos acumula {goals} acciones de gol registradas y {key_events} eventos clave.\n\n"
        f"Últimos resultados:\n"
        + ("\n".join(last_results[:5]) if last_results else "- Todavía no hay resultados finales registrados.")
    )

    squad_notes = (
        f"La plantilla convocada actual incluye {total_called_up} jugadores. "
        f"Este dato permite contextualizar profundidad de plantilla y disponibilidad para el torneo."
    )

    discipline_notes = (
        f"La selección acumula {cards} eventos disciplinarios entre amarillas, rojas y segundas amarillas. "
        "Esta métrica sirve como primer indicador de control competitivo, agresividad defensiva o riesgo de sanciones."
    )

    title = f"Informe automático: {team.name}"
    slug = slugify(f"informe-seleccion-{team.id}-{team.name}")

    return {
        "title": title,
        "slug": slug,
        "summary": summary,
        "performance_overview": performance_overview,
        "squad_notes": squad_notes,
        "discipline_notes": discipline_notes,
    }


def generate_team_report(team):
    content = build_team_report_content(team)

    report, _ = TeamReport.objects.update_or_create(
        team=team,
        defaults={
            "title": content["title"],
            "slug": content["slug"],
            "summary": content["summary"],
            "performance_overview": content["performance_overview"],
            "squad_notes": content["squad_notes"],
            "discipline_notes": content["discipline_notes"],
            "is_auto_generated": True,
        }
    )
    return report