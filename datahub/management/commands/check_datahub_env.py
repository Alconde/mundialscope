from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Comprueba si las variables de entorno de datahub están bien cargadas."

    def handle(self, *args, **options):
        self.stdout.write(f"ENABLE_EXTERNAL_DATA_SYNC = {settings.ENABLE_EXTERNAL_DATA_SYNC}")
        self.stdout.write(f"FOOTBALL_DATA_BASE_URL = {settings.FOOTBALL_DATA_BASE_URL}")
        self.stdout.write(
            f"FOOTBALL_DATA_API_KEY configurada = {'sí' if bool(settings.FOOTBALL_DATA_API_KEY) else 'no'}"
        )