from django.core.management.base import BaseCommand
from teams.models import Team


class Command(BaseCommand):
    help = "Muestra los campos disponibles en el modelo Team."

    def handle(self, *args, **options):
        field_names = [field.name for field in Team._meta.get_fields()]
        for name in field_names:
            self.stdout.write(name)