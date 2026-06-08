from django.core.management.base import BaseCommand
from teams.models import Team


TEAMS_2026 = [
    {"name": "Mexico", "fifa_code": "MEX", "confederation": Team.Confederation.CONCACAF, "group": "A"},
    {"name": "South Africa", "fifa_code": "RSA", "confederation": Team.Confederation.CAF, "group": "A"},
    {"name": "Korea Republic", "fifa_code": "KOR", "confederation": Team.Confederation.AFC, "group": "A"},
    {"name": "Czechia", "fifa_code": "CZE", "confederation": Team.Confederation.UEFA, "group": "A"},

    {"name": "Canada", "fifa_code": "CAN", "confederation": Team.Confederation.CONCACAF, "group": "B"},
    {"name": "Bosnia and Herzegovina", "fifa_code": "BIH", "confederation": Team.Confederation.UEFA, "group": "B"},
    {"name": "Qatar", "fifa_code": "QAT", "confederation": Team.Confederation.AFC, "group": "B"},
    {"name": "Switzerland", "fifa_code": "SUI", "confederation": Team.Confederation.UEFA, "group": "B"},

    {"name": "Brazil", "fifa_code": "BRA", "confederation": Team.Confederation.CONMEBOL, "group": "C"},
    {"name": "Morocco", "fifa_code": "MAR", "confederation": Team.Confederation.CAF, "group": "C"},
    {"name": "Haiti", "fifa_code": "HAI", "confederation": Team.Confederation.CONCACAF, "group": "C"},
    {"name": "Scotland", "fifa_code": "SCO", "confederation": Team.Confederation.UEFA, "group": "C"},

    {"name": "United States", "fifa_code": "USA", "confederation": Team.Confederation.CONCACAF, "group": "D"},
    {"name": "Paraguay", "fifa_code": "PAR", "confederation": Team.Confederation.CONMEBOL, "group": "D"},
    {"name": "Australia", "fifa_code": "AUS", "confederation": Team.Confederation.AFC, "group": "D"},
    {"name": "Türkiye", "fifa_code": "TUR", "confederation": Team.Confederation.UEFA, "group": "D"},

    {"name": "Germany", "fifa_code": "GER", "confederation": Team.Confederation.UEFA, "group": "E"},
    {"name": "Curaçao", "fifa_code": "CUW", "confederation": Team.Confederation.CONCACAF, "group": "E"},
    {"name": "Ivory Coast", "fifa_code": "CIV", "confederation": Team.Confederation.CAF, "group": "E"},
    {"name": "Ecuador", "fifa_code": "ECU", "confederation": Team.Confederation.CONMEBOL, "group": "E"},

    {"name": "Netherlands", "fifa_code": "NED", "confederation": Team.Confederation.UEFA, "group": "F"},
    {"name": "Japan", "fifa_code": "JPN", "confederation": Team.Confederation.AFC, "group": "F"},
    {"name": "Sweden", "fifa_code": "SWE", "confederation": Team.Confederation.UEFA, "group": "F"},
    {"name": "Tunisia", "fifa_code": "TUN", "confederation": Team.Confederation.CAF, "group": "F"},

    {"name": "Belgium", "fifa_code": "BEL", "confederation": Team.Confederation.UEFA, "group": "G"},
    {"name": "Egypt", "fifa_code": "EGY", "confederation": Team.Confederation.CAF, "group": "G"},
    {"name": "Iran", "fifa_code": "IRN", "confederation": Team.Confederation.AFC, "group": "G"},
    {"name": "New Zealand", "fifa_code": "NZL", "confederation": Team.Confederation.OFC, "group": "G"},

    {"name": "Spain", "fifa_code": "ESP", "confederation": Team.Confederation.UEFA, "group": "H"},
    {"name": "Cape Verde", "fifa_code": "CPV", "confederation": Team.Confederation.CAF, "group": "H"},
    {"name": "Saudi Arabia", "fifa_code": "KSA", "confederation": Team.Confederation.AFC, "group": "H"},
    {"name": "Uruguay", "fifa_code": "URU", "confederation": Team.Confederation.CONMEBOL, "group": "H"},

    {"name": "France", "fifa_code": "FRA", "confederation": Team.Confederation.UEFA, "group": "I"},
    {"name": "Senegal", "fifa_code": "SEN", "confederation": Team.Confederation.CAF, "group": "I"},
    {"name": "Iraq", "fifa_code": "IRQ", "confederation": Team.Confederation.AFC, "group": "I"},
    {"name": "Norway", "fifa_code": "NOR", "confederation": Team.Confederation.UEFA, "group": "I"},

    {"name": "Argentina", "fifa_code": "ARG", "confederation": Team.Confederation.CONMEBOL, "group": "J"},
    {"name": "Algeria", "fifa_code": "ALG", "confederation": Team.Confederation.CAF, "group": "J"},
    {"name": "Austria", "fifa_code": "AUT", "confederation": Team.Confederation.UEFA, "group": "J"},
    {"name": "Jordan", "fifa_code": "JOR", "confederation": Team.Confederation.AFC, "group": "J"},

    {"name": "Portugal", "fifa_code": "POR", "confederation": Team.Confederation.UEFA, "group": "K"},
    {"name": "DR Congo", "fifa_code": "COD", "confederation": Team.Confederation.CAF, "group": "K"},
    {"name": "Uzbekistan", "fifa_code": "UZB", "confederation": Team.Confederation.AFC, "group": "K"},
    {"name": "Colombia", "fifa_code": "COL", "confederation": Team.Confederation.CONMEBOL, "group": "K"},

    {"name": "England", "fifa_code": "ENG", "confederation": Team.Confederation.UEFA, "group": "L"},
    {"name": "Croatia", "fifa_code": "CRO", "confederation": Team.Confederation.UEFA, "group": "L"},
    {"name": "Ghana", "fifa_code": "GHA", "confederation": Team.Confederation.CAF, "group": "L"},
    {"name": "Panama", "fifa_code": "PAN", "confederation": Team.Confederation.CONCACAF, "group": "L"},
]


class Command(BaseCommand):
    help = "Carga o actualiza las selecciones y grupos del Mundial 2026"

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in TEAMS_2026:
            team, created = Team.objects.update_or_create(
                fifa_code=item["fifa_code"],
                defaults={
                    "name": item["name"],
                    "confederation": item["confederation"],
                    "group": item["group"],
                    "is_active": True,
                },
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Creado: {team.name}"))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f"Actualizado: {team.name}"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Proceso completado. Creados: {created_count} | Actualizados: {updated_count}"
        ))