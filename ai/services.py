import json
import os
from django.conf import settings

from openai import OpenAI


class AIServiceError(Exception):
    pass


def get_openai_client():
    if not settings.OPENAI_API_KEY:
        raise AIServiceError("OPENAI_API_KEY no está configurada.")
    return OpenAI(api_key=settings.OPENAI_API_KEY)





def generate_structured_football_analysis(prompt):
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError(
            "La librería 'openai' no está instalada. Ejecuta: pip install openai"
        )

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Falta la variable de entorno OPENAI_API_KEY."
        )

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-5.4",
        input=prompt,
    )

    return response.output_text