from django import forms
from .models import Player


class PlayerComparisonForm(forms.Form):
    player_a = forms.ModelChoiceField(
        queryset=Player.objects.select_related("team").filter(is_called_up=True).order_by("team__name", "last_name"),
        label="Jugador A"
    )
    player_b = forms.ModelChoiceField(
        queryset=Player.objects.select_related("team").filter(is_called_up=True).order_by("team__name", "last_name"),
        label="Jugador B"
    )

    def clean(self):
        cleaned_data = super().clean()
        player_a = cleaned_data.get("player_a")
        player_b = cleaned_data.get("player_b")

        if player_a and player_b and player_a == player_b:
            raise forms.ValidationError("Debes seleccionar dos jugadores distintos.")

        return cleaned_data