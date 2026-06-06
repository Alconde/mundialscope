from django import forms


class ChatQuestionForm(forms.Form):
    question = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Pregunta al asistente sobre el Mundial, selecciones o partidos...",
            }
        ),
    )