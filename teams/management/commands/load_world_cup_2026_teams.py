from django.core.management.base import BaseCommand
from teams.models import Team


TEAMS_DATA = [
    {"name": "Mexico", "fifa_code": "MEX", "confederation": "CONCACAF", "group": "A", "is_active": True},
    {"name": "South Africa", "fifa_code": "RSA", "confederation": "CAF", "group": "A", "is_active": True},
    {"name": "South Korea", "fifa_code": "KOR", "confederation": "AFC", "group": "A", "is_active": True},
    {"name": "Czechia", "fifa_code": "CZE", "confederation": "UEFA", "group": "A", "is_active": True},

    {"name": "Canada", "fifa_code": "CAN", "confederation": "CONCACAF", "group": "B", "is_active": True},
    {"name": "Bosnia and Herzegovina", "fifa_code": "BIH", "confederation": "UEFA", "group": "B", "is_active": True},
    {"name": "Qatar", "fifa_code": "QAT", "confederation": "AFC", "group": "B", "is_active": True},
    {"name": "Switzerland", "fifa_code": "SUI", "confederation": "UEFA", "group": "B", "is_active": True},

    {"name": "Brazil", "fifa_code": "BRA", "confederation": "CONMEBOL", "group": "C", "is_active": True},
    {"name": "Morocco", "fifa_code": "MAR", "confederation": "CAF", "group": "C", "is_active": True},
    {"name": "Haiti", "fifa_code": "HAI", "confederation": "CONCACAF", "group": "C", "is_active": True},
    {"name": "Scotland", "fifa_code": "SCO", "confederation": "UEFA", "group": "C", "is_active": True},

    {"name": "United States", "fifa_code": "USA", "confederation": "CONCACAF", "group": "D", "is_active": True},
    {"name": "Paraguay", "fifa_code": "PAR", "confederation": "CONMEBOL", "group": "D", "is_active": True},
    {"name": "Australia", "fifa_code": "AUS", "confederation": "AFC", "group": "D", "is_active": True},
    {"name": "Türkiye", "fifa_code": "TUR", "confederation": "UEFA", "group": "D", "is_active": True},

    {"name": "Germany", "fifa_code": "GER", "confederation": "UEFA", "group": "E", "is_active": True},
    {"name": "Curacao", "fifa_code": "CUW", "confederation": "CONCACAF", "group": "E", "is_active": True},
    {"name": "Ivory Coast", "fifa_code": "CIV", "confederation": "CAF", "group": "E", "is_active": True},
    {"name": "Ecuador", "fifa_code": "ECU", "confederation": "CONMEBOL", "group": "E", "is_active": True},

    {"name": "Netherlands", "fifa_code": "NED", "confederation": "UEFA", "group": "F", "is_active": True},
    {"name": "Japan", "fifa_code": "JPN", "confederation": "AFC", "group": "F", "is_active": True},
    {"name": "Sweden", "fifa_code": "SWE", "confederation": "UEFA", "group": "F", "is_active": True},
    {"name": "Tunisia", "fifa_code": "TUN", "confederation": "CAF", "group": "F", "is_active": True},

    {"name": "Belgium", "fifa_code": "BEL", "confederation": "UEFA", "group": "G", "is_active": True},
    {"name": "Egypt", "fifa_code": "EGY", "confederation": "CAF", "group": "G", "is_active": True},
    {"name": "Iran", "fifa_code": "IRN", "confederation": "AFC", "group": "G", "is_active": True},
    {"name": "New Zealand", "fifa_code": "NZL", "confederation": "OFC", "group": "G", "is_active": True},

    {"name": "Spain", "fifa_code": "ESP", "confederation": "UEFA", "group": "H", "is_active": True},
    {"name": "Cape Verde", "fifa_code": "CPV", "confederation": "CAF", "group": "H", "is_active": True},
    {"name": "Saudi Arabia", "fifa_code": "KSA", "confederation": "AFC", "group": "H", "is_active": True},
    {"name": "Uruguay", "fifa_code": "URU", "confederation": "CONMEBOL", "group": "H", "is_active": True},

    {"name": "France", "fifa_code": "FRA", "confederation": "UEFA", "group": "I", "is_active": True},
    {"name": "Senegal", "fifa_code": "SEN", "confederation": "CAF", "group": "I", "is_active": True},
    {"name": "Iraq", "fifa_code": "IRQ", "confederation": "AFC", "group": "I", "is_active": True},
    {"name": "Norway", "fifa_code": "NOR", "confederation": "UEFA", "group": "I", "is_active": True},

    {"name": "Argentina", "fifa_code": "ARG", "confederation": "CONMEBOL", "group": "J", "is_active": True},
    {"name": "Algeria", "fifa_code": "ALG", "confederation": "CAF", "group": "J", "is_active": True},
    {"name": "Austria", "fifa_code": "AUT", "confederation": "UEFA", "group": "J", "is_active": True},
    {"name": "Jordan", "fifa_code": "JOR", "confederation": "AFC", "group": "J", "is_active": True},

    {"name": "Portugal", "fifa_code": "POR", "confederation": "UEFA", "group": "K", "is_active": True},
    {"name": "DR Congo", "fifa_code": "COD", "confederation": "CAF", "group": "K", "is_active": True},
    {"name": "Uzbekistan", "fifa_code": "UZB", "confederation": "AFC", "group": "K", "is_active": True},
    {"name": "Colombia", "fifa_code": "COL", "confederation": "CONMEBOL", "group": "K", "is_active": True},

    {"name": "England", "fifa_code": "ENG", "confederation": "UEFA", "group": "L", "is_active": True},
    {"name": "Croatia", "fifa_code": "CRO", "confederation": "UEFA", "group": "L", "is_active": True},
    {"name": "Ghana", "fifa_code": "GHA", "confederation": "CAF", "group": "L", "is_active": True},
    {"name": "Panama", "fifa_code": "PAN", "confederation": "CONCACAF", "group": "L", "is_active": True},
]


class Command(BaseCommand):
    help = "Carga las 48 selecciones del Mundial 2026 con sus grupos"

    def handle(self, *args, **kwargs):
        created_count = 0
        updated_count = 0

        for item in TEAMS_DATA:
            _, created = Team.objects.update_or_create(
                fifa_code=item["fifa_code"],
                defaults=item,
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Proceso completado. Equipos creados: {created_count}. Equipos actualizados: {updated_count}."
            )
        )