import csv
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from players.models import Player
from teams.models import Team


class Command(BaseCommand):
    help = "Carga jugadores del Mundial 2026 desde un archivo CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_path",
            type=str,
            help="Ruta al archivo CSV con los jugadores",
        )

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        created_count = 0
        updated_count = 0
        skipped_count = 0

        try:
            with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)

                required_columns = {
                    "team_code",
                    "name",
                    "shirt_name",
                    "position",
                    "date_of_birth",
                    "club",
                    "shirt_number",
                    "is_called_up",
                }

                missing = required_columns - set(reader.fieldnames or [])
                if missing:
                    raise CommandError(
                        f"Faltan columnas obligatorias en el CSV: {', '.join(sorted(missing))}"
                    )

                for row in reader:
                    team_code = (row.get("team_code") or "").strip().upper()
                    name = (row.get("name") or "").strip()

                    if not team_code or not name:
                        skipped_count += 1
                        self.stdout.write(
                            self.style.WARNING("Fila omitida: falta team_code o name")
                        )
                        continue

                    try:
                        team = Team.objects.get(fifa_code=team_code)
                    except Team.DoesNotExist:
                        skipped_count += 1
                        self.stdout.write(
                            self.style.WARNING(
                                f"Fila omitida: no existe selección con código {team_code}"
                            )
                        )
                        continue

                    date_of_birth = None
                    raw_dob = (row.get("date_of_birth") or "").strip()
                    if raw_dob:
                        try:
                            date_of_birth = datetime.strptime(raw_dob, "%Y-%m-%d").date()
                        except ValueError:
                            skipped_count += 1
                            self.stdout.write(
                                self.style.WARNING(
                                    f"Fecha inválida para {name}: {raw_dob}. Usa YYYY-MM-DD"
                                )
                            )
                            continue

                    raw_number = (row.get("shirt_number") or "").strip()
                    shirt_number = int(raw_number) if raw_number.isdigit() else None

                    is_called_up = (row.get("is_called_up") or "").strip().lower() in {
                        "1", "true", "yes", "si", "sí"
                    }

                    player, created = Player.objects.update_or_create(
                        team=team,
                        name=name,
                        defaults={
                            "shirt_name": (row.get("shirt_name") or "").strip(),
                            "position": (row.get("position") or "").strip(),
                            "date_of_birth": date_of_birth,
                            "club": (row.get("club") or "").strip(),
                            "shirt_number": shirt_number,
                            "is_called_up": is_called_up,
                        },
                    )

                    if created:
                        created_count += 1
                        self.stdout.write(self.style.SUCCESS(f"Creado: {player.name} ({team.fifa_code})"))
                    else:
                        updated_count += 1
                        self.stdout.write(self.style.WARNING(f"Actualizado: {player.name} ({team.fifa_code})"))

        except FileNotFoundError:
            raise CommandError(f"No se encontró el archivo: {csv_path}")

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Proceso completado. Creados: {created_count} | Actualizados: {updated_count} | Omitidos: {skipped_count}"
            )
        )