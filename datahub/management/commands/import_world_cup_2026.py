from django.core.management.base import BaseCommand

from datahub.exceptions import DataSyncError
from datahub.services import import_world_cup_2026_matches


class Command(BaseCommand):
    help = "Importa partidos base del Mundial 2026 desde proveedor externo."

    def handle(self, *args, **options):
        try:
            result = import_world_cup_2026_matches()
        except DataSyncError as exc:
            self.stdout.write(self.style.ERROR(f"Error de sincronización: {exc}"))
            return

        self.stdout.write(
            self.style.SUCCESS(
                f"Importación completada. Partidos procesados: {result['imported_matches']}"
            )
        )