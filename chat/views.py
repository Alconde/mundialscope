from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import ChatConversation, ChatMessage
from .forms import ChatQuestionForm
from ai.services import AIServiceError, generate_structured_football_analysis
from matches.models import Match
from teams.models import Team
from matches.models import MatchEvent


def build_chat_system_prompt():
    return """
Eres un asistente interno de MundialScope, una plataforma profesional de análisis del Mundial.
Dispones de información sobre partidos, selecciones, eventos y estadísticas del torneo.

Responde SIEMPRE en español, con un tono profesional pero claro.
Cuando no tengas datos suficientes, dilo y explica qué faltaría.
Evita inventar marcadores o eventos concretos que no estén en el contexto.
""".strip()


def build_chat_context_for_question(question):
    matches = Match.objects.select_related("home_team", "away_team", "tournament").order_by("-match_date")[:5]
    teams = Team.objects.filter(is_active=True).order_by("name")[:10]

    match_lines = []
    for m in matches:
        match_lines.append(
            f"- {m.tournament.name} {m.tournament.year}, {m.stage}: "
            f"{m.home_team.name} {m.home_score}-{m.away_score} {m.away_team.name}"
        )

    team_lines = [f"- {t.name} ({t.confederation})" for t in teams]

    context_text = "PARTIDOS RECIENTES:\n" + ("\n".join(match_lines) or "- Sin partidos registrados") + "\n\n"
    context_text += "SELECCIONES ACTIVAS:\n" + ("\n".join(team_lines) or "- Sin selecciones activas")

    return context_text


def generate_chat_answer(question):
    system_prompt = build_chat_system_prompt()
    context = build_chat_context_for_question(question)

    prompt = f"""
{system_prompt}

CONTEXTO DISPONIBLE:
{context}

PREGUNTA DEL USUARIO:
{question}

Devuelve una respuesta estructurada.
""".strip()

    schema = {
        "type": "object",
        "properties": {
            "answer": {"type": "string"},
            "short_title": {"type": "string"},
        },
        "required": ["answer", "short_title"],
        "additionalProperties": False,
    }

    result = generate_structured_football_analysis(prompt, schema)
    return result["short_title"], result["answer"]


class ChatConversationListView(ListView):
    model = ChatConversation
    template_name = "chat/chat_list.html"
    context_object_name = "conversations"

    def get_queryset(self):
        return ChatConversation.objects.all()


class ChatConversationDetailView(DetailView):
    model = ChatConversation
    template_name = "chat/chat_detail.html"
    context_object_name = "conversation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ChatQuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ChatQuestionForm(request.POST or None)

        if form.is_valid():
            question = form.cleaned_data["question"]

            ChatMessage.objects.create(
                conversation=self.object,
                sender=ChatMessage.Sender.USER,
                content=question,
            )

            try:
                short_title, answer = generate_chat_answer(question)
            except AIServiceError as exc:
                short_title = "Error de análisis"
                answer = f"No se ha podido generar una respuesta de IA: {exc}"

            if not self.object.title and short_title:
                self.object.title = short_title[:255]
                self.object.save(update_fields=["title"])

            ChatMessage.objects.create(
                conversation=self.object,
                sender=ChatMessage.Sender.AI,
                content=answer,
            )

            return redirect(reverse("chat:chat-detail", kwargs={"pk": self.object.pk}))

        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)