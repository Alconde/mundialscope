import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from teams.models import Team
from players.models import Player


POSITION_MAP = {
    "GK": "GK",
    "DF": "DF",
    "MF": "MF",
    "FW": "FW",
}


class Command(BaseCommand):
    help = "Importa jugadores convocados oficiales por selección desde un JSON preparado con datos FIFA."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            required=True,
            help="Ruta al archivo JSON con las convocatorias FIFA.",
        )
        parser.add_argument(
            "--team",
            type=str,
            help="Filtrar importación por nombre de selección o código FIFA.",
        )
        parser.add_argument(
            "--reset-missing",
            action="store_true",
            help="Marca is_called_up=False para jugadores existentes de la selección que no aparezcan en el archivo.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Simula la importación sin guardar cambios.",
        )

    def handle(self, *args, **options):
        file_path = Path(options["file"])

        if not file_path.exists():
            raise CommandError(f"No existe el archivo: {file_path}")

        with file_path.open("r", encoding="utf-8") as f:
            payload = json.load(f)

        squads = payload.get("teams", [])
        if not squads:
            raise CommandError("El JSON no contiene la clave 'teams' o está vacía.")

        team_filter = options.get("team")
        dry_run = options["dry_run"]
        reset_missing = options["reset_missing"]

        total_created = 0
        total_updated = 0
        total_teams = 0

        with transaction.atomic():
            for squad in squads:
                team_name = squad.get("team_name")
                fifa_code = squad.get("fifa_code")
                players = squad.get("players", [])

                if team_filter:
                    normalized_filter = team_filter.strip().lower()
                    if normalized_filter not in {
                        str(team_name).strip().lower(),
                        str(fifa_code).strip().lower(),
                    }:
                        continue

                team = self.find_team(team_name=team_name, fifa_code=fifa_code)
                imported_player_ids = []

                created_count = 0
                updated_count = 0

                for player_data in players:
                    player, created = self.upsert_player(team, player_data)
                    imported_player_ids.append(player.id)

                    if created:
                        created_count += 1
                    else:
                        updated_count += 1

                if reset_missing:
                    team.players.exclude(id__in=imported_player_ids).update(is_called_up=False)

                total_created += created_count
                total_updated += updated_count
                total_teams += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"{team.name}: {created_count} creados, {updated_count} actualizados, {len(imported_player_ids)} convocados"
                    )
                )

            if total_teams == 0:
                raise CommandError("No se encontró ninguna selección que coincida con el filtro indicado.")

            if dry_run:
                raise CommandError("Dry run completado. Se revierte la transacción porque se usó --dry-run.")

        self.stdout.write(
            self.style.SUCCESS(
                f"Importación completada: {total_teams} selecciones, {total_created} creados, {total_updated} actualizados."
            )
        )

    def find_team(self, team_name, fifa_code=None):
        qs = Team.objects.all()

        if fifa_code:
            team = qs.filter(fifa_code__iexact=fifa_code).first()
            if team:
                return team

        team = qs.filter(name__iexact=team_name).first()
        if team:
            return team

        raise CommandError(
            f"No se encontró la selección en la base de datos. team_name='{team_name}', fifa_code='{fifa_code}'"
        )

    def upsert_player(self, team, player_data):
        full_name = player_data.get("name", "").strip()
        if not full_name:
            raise CommandError(f"Jugador sin nombre en selección {team.name}")

        defaults = {
            "team": team,
            "position": POSITION_MAP.get(player_data.get("position"), player_data.get("position")),
            "shirt_name": player_data.get("shirt_name", "").strip(),
            "date_of_birth": player_data.get("date_of_birth"),
            "club": player_data.get("club", "").strip(),
            "height_cm": player_data.get("height_cm"),
            "is_called_up": True,
        }

        player = Player.objects.filter(
            team=team,
            name__iexact=full_name,
        ).first()

        if player:
            for field, value in defaults.items():
                setattr(player, field, value)
            player.save()
            return player, False

        player = Player.objects.create(
            name=full_name,
            **defaults,
        )
        return player, True