from django import forms
from teams.models import Team
from players.models import Player


class TeamCompareForm(forms.Form):
    team_a = forms.ModelChoiceField(
        queryset=Team.objects.order_by("name"),
        label="Selección A",
        empty_label="---------",
    )
    team_b = forms.ModelChoiceField(
        queryset=Team.objects.order_by("name"),
        label="Selección B",
        empty_label="---------",
    )


class PlayerCompareForm(forms.Form):
    player_a = forms.ModelChoiceField(
        queryset=Player.objects.filter(is_called_up=True)
        .select_related("team")
        .order_by("team__name", "first_name", "last_name"),
        label="Jugador A",
        empty_label="---------",
    )
    player_b = forms.ModelChoiceField(
        queryset=Player.objects.filter(is_called_up=True)
        .select_related("team")
        .order_by("team__name", "first_name", "last_name"),
        label="Jugador B",
        empty_label="---------",
    )