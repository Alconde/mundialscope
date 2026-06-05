from django import forms
from .models import Team


class TeamComparisonForm(forms.Form):
    team_a = forms.ModelChoiceField(
        queryset=Team.objects.filter(is_active=True).order_by("name"),
        label="Selección A"
    )
    team_b = forms.ModelChoiceField(
        queryset=Team.objects.filter(is_active=True).order_by("name"),
        label="Selección B"
    )

    def clean(self):
        cleaned_data = super().clean()
        team_a = cleaned_data.get("team_a")
        team_b = cleaned_data.get("team_b")

        if team_a and team_b and team_a == team_b:
            raise forms.ValidationError("Debes elegir dos selecciones distintas.")

        return cleaned_data