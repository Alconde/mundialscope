from django.core.management.base import BaseCommand
from teams.models import Team
from players.models import Player


TEAMS_DATA = [
    {
        "name": "Spain",
        "fifa_code": "ESP",
        "confederation": "UEFA",
        "coach": "Luis de la Fuente",
        "fifa_ranking": 3,
        "group": "A",
        "primary_color": "#C60B1E",
        "secondary_color": "#FFC400",
    },
    {
        "name": "Argentina",
        "fifa_code": "ARG",
        "confederation": "CONMEBOL",
        "coach": "Lionel Scaloni",
        "fifa_ranking": 1,
        "group": "A",
        "primary_color": "#74ACDF",
        "secondary_color": "#FFFFFF",
    },
    {
        "name": "France",
        "fifa_code": "FRA",
        "confederation": "UEFA",
        "coach": "Didier Deschamps",
        "fifa_ranking": 2,
        "group": "B",
        "primary_color": "#002654",
        "secondary_color": "#ED2939",
    },
    {
        "name": "Brazil",
        "fifa_code": "BRA",
        "confederation": "CONMEBOL",
        "coach": "Dorival Júnior",
        "fifa_ranking": 5,
        "group": "B",
        "primary_color": "#FFDF00",
        "secondary_color": "#009C3B",
    },
]

PLAYERS_DATA = [
    {
        "team_code": "ESP",
        "first_name": "Álvaro",
        "last_name": "Morata",
        "shirt_number": 7,
        "position": "FW",
        "club": "Atlético de Madrid",
        "caps": 80,
        "international_goals": 36,
        "preferred_foot": "right",
        "height_cm": 190,
    },
    {
        "team_code": "ESP",
        "first_name": "Pedri",
        "last_name": "González",
        "shirt_number": 20,
        "position": "MF",
        "club": "FC Barcelona",
        "caps": 25,
        "international_goals": 2,
        "preferred_foot": "right",
        "height_cm": 174,
    },
    {
        "team_code": "ARG",
        "first_name": "Lautaro",
        "last_name": "Martínez",
        "shirt_number": 9,
        "position": "FW",
        "club": "Inter",
        "caps": 60,
        "international_goals": 28,
        "preferred_foot": "right",
        "height_cm": 174,
    },
    {
        "team_code": "FRA",
        "first_name": "Kylian",
        "last_name": "Mbappé",
        "shirt_number": 10,
        "position": "FW",
        "club": "Real Madrid",
        "caps": 75,
        "international_goals": 48,
        "preferred_foot": "right",
        "height_cm": 178,
    },
    {
        "team_code": "BRA",
        "first_name": "Vinícius",
        "last_name": "Júnior",
        "shirt_number": 7,
        "position": "FW",
        "club": "Real Madrid",
        "caps": 35,
        "international_goals": 6,
        "preferred_foot": "right",
        "height_cm": 176,
    },
]


class Command(BaseCommand):
    help = "Carga datos iniciales de selecciones y jugadores"

    def handle(self, *args, **kwargs):
        created_teams = 0
        created_players = 0

        for team_data in TEAMS_DATA:
            _, created = Team.objects.update_or_create(
                fifa_code=team_data["fifa_code"],
                defaults=team_data,
            )
            if created:
                created_teams += 1

        for player_data in PLAYERS_DATA:
            team = Team.objects.get(fifa_code=player_data["team_code"])

            defaults = {
                "shirt_number": player_data["shirt_number"],
                "position": player_data["position"],
                "club": player_data["club"],
                "caps": player_data["caps"],
                "international_goals": player_data["international_goals"],
                "preferred_foot": player_data["preferred_foot"],
                "height_cm": player_data["height_cm"],
            }

            _, created = Player.objects.update_or_create(
                team=team,
                first_name=player_data["first_name"],
                last_name=player_data["last_name"],
                defaults=defaults,
            )
            if created:
                created_players += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Carga completada. Selecciones creadas: {created_teams}. Jugadores creados: {created_players}."
            )
        )