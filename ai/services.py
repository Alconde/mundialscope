import json

from django.conf import settings

from openai import OpenAI


class AIServiceError(Exception):
    pass


def get_openai_client():
    if not settings.OPENAI_API_KEY:
        raise AIServiceError("OPENAI_API_KEY no está configurada.")
    return OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_structured_football_analysis(prompt, schema):
    if not settings.ENABLE_AI_ANALYSIS:
        raise AIServiceError("La IA está desactivada en la configuración.")

    client = get_openai_client()

    response = client.responses.create(
        model=settings.OPENAI_MODEL,
        input=prompt,
        text={
            "format": {
                "type": "json_schema",
                "name": "football_analysis",
                "schema": schema,
                "strict": True,
            }
        }
    )

    try:
        return json.loads(response.output_text)
    except Exception as exc:
        raise AIServiceError(f"No se pudo parsear la respuesta de IA: {exc}")