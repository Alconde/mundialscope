from django.core.management.base import BaseCommand
from teams.models import Team


TEAM_ENRICHMENT = {
    "MEX": {"coach": "Javier Aguirre", "fifa_ranking": 14, "primary_color": "#006847", "secondary_color": "#CE1126"},
    "RSA": {"coach": "Hugo Broos", "fifa_ranking": 56, "primary_color": "#007A4D", "secondary_color": "#FFB612"},
    "KOR": {"coach": "Hong Myung-bo", "fifa_ranking": 23, "primary_color": "#E31B23", "secondary_color": "#1B1B1B"},
    "CZE": {"coach": "Miroslav Koubek", "fifa_ranking": 39, "primary_color": "#D7141A", "secondary_color": "#11457E"},

    "CAN": {"coach": "Jesse Marsch", "fifa_ranking": 30, "primary_color": "#D80621", "secondary_color": "#FFFFFF"},
    "BIH": {"coach": "Sergej Barbarez", "fifa_ranking": 72, "primary_color": "#002F6C", "secondary_color": "#FDB913"},
    "QAT": {"coach": "Julen Lopetegui", "fifa_ranking": 58, "primary_color": "#8A1538", "secondary_color": "#FFFFFF"},
    "SUI": {"coach": "Murat Yakin", "fifa_ranking": 19, "primary_color": "#D52B1E", "secondary_color": "#FFFFFF"},

    "BRA": {"coach": "Carlo Ancelotti", "fifa_ranking": 6, "primary_color": "#FFDF00", "secondary_color": "#009C3B"},
    "MAR": {"coach": "Walid Regragui", "fifa_ranking": 8, "primary_color": "#C1272D", "secondary_color": "#006233"},
    "HAI": {"coach": "Sébastien Migné", "fifa_ranking": 83, "primary_color": "#00209F", "secondary_color": "#D21034"},
    "SCO": {"coach": "Steve Clarke", "fifa_ranking": 28, "primary_color": "#005EB8", "secondary_color": "#FFFFFF"},

    "USA": {"coach": "Mauricio Pochettino", "fifa_ranking": 17, "primary_color": "#3C3B6E", "secondary_color": "#B22234"},
    "PAR": {"coach": "Gustavo Alfaro", "fifa_ranking": 45, "primary_color": "#D52B1E", "secondary_color": "#FFFFFF"},
    "AUS": {"coach": "Tony Popovic", "fifa_ranking": 24, "primary_color": "#FFCD00", "secondary_color": "#00664B"},
    "TUR": {"coach": "Vincenzo Montella", "fifa_ranking": 27, "primary_color": "#E30A17", "secondary_color": "#FFFFFF"},

    "GER": {"coach": "Julian Nagelsmann", "fifa_ranking": 10, "primary_color": "#000000", "secondary_color": "#DD0000"},
    "CUW": {"coach": "Dick Advocaat", "fifa_ranking": 90, "primary_color": "#003DA5", "secondary_color": "#F9E814"},
    "CIV": {"coach": "Emerse Faé", "fifa_ranking": 41, "primary_color": "#F77F00", "secondary_color": "#009E60"},
    "ECU": {"coach": "Sebastián Beccacece", "fifa_ranking": 25, "primary_color": "#F7D117", "secondary_color": "#003893"},

    "NED": {"coach": "Ronald Koeman", "fifa_ranking": 7, "primary_color": "#F36C21", "secondary_color": "#FFFFFF"},
    "JPN": {"coach": "Hajime Moriyasu", "fifa_ranking": 18, "primary_color": "#0033A0", "secondary_color": "#FFFFFF"},
    "SWE": {"coach": "Graham Potter", "fifa_ranking": 31, "primary_color": "#006AA7", "secondary_color": "#FECC00"},
    "TUN": {"coach": "Sami Trabelsi", "fifa_ranking": 49, "primary_color": "#E70013", "secondary_color": "#FFFFFF"},

    "BEL": {"coach": "Rudi Garcia", "fifa_ranking": 9, "primary_color": "#000000", "secondary_color": "#ED2939"},
    "EGY": {"coach": "Hossam Hassan", "fifa_ranking": 34, "primary_color": "#CE1126", "secondary_color": "#000000"},
    "IRN": {"coach": "Amir Ghalenoei", "fifa_ranking": 20, "primary_color": "#239F40", "secondary_color": "#DA0000"},
    "NZL": {"coach": "Darren Bazeley", "fifa_ranking": 86, "primary_color": "#FFFFFF", "secondary_color": "#000000"},

    "ESP": {"coach": "Luis de la Fuente", "fifa_ranking": 2, "primary_color": "#AA151B", "secondary_color": "#F1BF00"},
    "CPV": {"coach": "Bubista", "fifa_ranking": 63, "primary_color": "#003893", "secondary_color": "#CF2027"},
    "KSA": {"coach": "Giorgos Donis", "fifa_ranking": 59, "primary_color": "#006C35", "secondary_color": "#FFFFFF"},
    "URU": {"coach": "Marcelo Bielsa", "fifa_ranking": 16, "primary_color": "#6CB4EE", "secondary_color": "#FFFFFF"},

    "FRA": {"coach": "Didier Deschamps", "fifa_ranking": 1, "primary_color": "#0055A4", "secondary_color": "#EF4135"},
    "SEN": {"coach": "Pape Thiaw", "fifa_ranking": 15, "primary_color": "#00853F", "secondary_color": "#FDEF42"},
    "IRQ": {"coach": "Graham Arnold", "fifa_ranking": 57, "primary_color": "#CE1126", "secondary_color": "#FFFFFF"},
    "NOR": {"coach": "Ståle Solbakken", "fifa_ranking": 43, "primary_color": "#BA0C2F", "secondary_color": "#00205B"},

    "ARG": {"coach": "Lionel Scaloni", "fifa_ranking": 3, "primary_color": "#74ACDF", "secondary_color": "#FFFFFF"},
    "ALG": {"coach": "Vladimir Petković", "fifa_ranking": 36, "primary_color": "#006233", "secondary_color": "#FFFFFF"},
    "AUT": {"coach": "Ralf Rangnick", "fifa_ranking": 22, "primary_color": "#ED2939", "secondary_color": "#FFFFFF"},
    "JOR": {"coach": "Jamal Sellami", "fifa_ranking": 64, "primary_color": "#000000", "secondary_color": "#CE1126"},

    "POR": {"coach": "Roberto Martínez", "fifa_ranking": 5, "primary_color": "#006600", "secondary_color": "#FF0000"},
    "COD": {"coach": "Sébastien Desabre", "fifa_ranking": 61, "primary_color": "#007FFF", "secondary_color": "#F7D618"},
    "UZB": {"coach": "Fabio Cannavaro", "fifa_ranking": 51, "primary_color": "#0099B5", "secondary_color": "#1EB53A"},
    "COL": {"coach": "Néstor Lorenzo", "fifa_ranking": 13, "primary_color": "#FCD116", "secondary_color": "#003893"},

    "ENG": {"coach": "Thomas Tuchel", "fifa_ranking": 4, "primary_color": "#FFFFFF", "secondary_color": "#CE1126"},
    "CRO": {"coach": "Zlatko Dalić", "fifa_ranking": 11, "primary_color": "#FF0000", "secondary_color": "#FFFFFF"},
    "GHA": {"coach": "Otto Addo", "fifa_ranking": 46, "primary_color": "#CE1126", "secondary_color": "#FCD116"},
    "PAN": {"coach": "Thomas Christiansen", "fifa_ranking": 33, "primary_color": "#072357", "secondary_color": "#DA121A"},
}


class Command(BaseCommand):
    help = "Enriquece las selecciones del Mundial 2026 con coach, ranking y colores"

    def handle(self, *args, **options):
        updated_count = 0
        missing_count = 0

        for fifa_code, data in TEAM_ENRICHMENT.items():
            try:
                team = Team.objects.get(fifa_code=fifa_code)
            except Team.DoesNotExist:
                missing_count += 1
                self.stdout.write(self.style.WARNING(f"No existe equipo con código {fifa_code}"))
                continue

            team.coach = data["coach"]
            team.fifa_ranking = data["fifa_ranking"]
            team.primary_color = data["primary_color"]
            team.secondary_color = data["secondary_color"]
            team.is_active = True
            team.save()

            updated_count += 1
            self.stdout.write(self.style.SUCCESS(f"Actualizado: {team.name}"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Proceso completado. Actualizados: {updated_count} | No encontrados: {missing_count}"
        ))