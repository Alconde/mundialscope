from ai.services import generate_structured_football_analysis


def build_team_ai_prompt(team, summary_data):
    return f"""
Eres un analista táctico profesional especializado en selecciones nacionales.
Analiza esta selección del Mundial en español, de forma clara y concreta.

SELECCIÓN:
- Nombre: {team.name}
- Confederación: {team.confederation}
- Grupo: {team.group or "Sin grupo"}

DATOS:
- Partidos jugados: {summary_data["played"]}
- Victorias: {summary_data["wins"]}
- Empates: {summary_data["draws"]}
- Derrotas: {summary_data["losses"]}
- Goles a favor: {summary_data["goals_for"]}
- Goles en contra: {summary_data["goals_against"]}
- Eventos clave: {summary_data["key_events"]}
- Tarjetas: {summary_data["cards"]}

Devuelve una lectura estructurada.
""".strip()


def generate_team_ai_analysis(team_context):
    try:
        return generate_structured_football_analysis(team_context)
    except Exception as exc:
        return {
            "summary": "El análisis IA no está disponible en este entorno.",
            "details": str(exc),
        }