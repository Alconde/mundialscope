from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


ENGLAND_PLAYERS = [
    {"shirt_number": 1, "first_name": "Jordan", "last_name": "Pickford", "position": Player.Position.GOALKEEPER, "club": "Everton", "external_id": "wc26-eng-jordan-pickford"},
    {"shirt_number": 12, "first_name": "Aaron", "last_name": "Ramsdale", "position": Player.Position.GOALKEEPER, "club": "Arsenal", "external_id": "wc26-eng-aaron-ramsdale"},
    {"shirt_number": 23, "first_name": "Dean", "last_name": "Henderson", "position": Player.Position.GOALKEEPER, "club": "Crystal Palace", "external_id": "wc26-eng-dean-henderson"},

    {"shirt_number": 2, "first_name": "Kyle", "last_name": "Walker", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-eng-kyle-walker"},
    {"shirt_number": 3, "first_name": "Luke", "last_name": "Shaw", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-eng-luke-shaw"},
    {"shirt_number": 4, "first_name": "John", "last_name": "Stones", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-eng-john-stones"},
    {"shirt_number": 5, "first_name": "Harry", "last_name": "Maguire", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-eng-harry-maguire"},
    {"shirt_number": 13, "first_name": "Kieran", "last_name": "Trippier", "position": Player.Position.DEFENDER, "club": "Newcastle United", "external_id": "wc26-eng-kieran-trippier"},
    {"shirt_number": 14, "first_name": "Ben", "last_name": "Chilwell", "position": Player.Position.DEFENDER, "club": "Chelsea", "external_id": "wc26-eng-ben-chilwell"},
    {"shirt_number": 15, "first_name": "Marc", "last_name": "Guehi", "position": Player.Position.DEFENDER, "club": "Crystal Palace", "external_id": "wc26-eng-marc-guehi"},

    {"shirt_number": 6, "first_name": "Declan", "last_name": "Rice", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-eng-declan-rice"},
    {"shirt_number": 8, "first_name": "Jude", "last_name": "Bellingham", "position": Player.Position.MIDFIELDER, "club": "Real Madrid", "external_id": "wc26-eng-jude-bellingham"},
    {"shirt_number": 10, "first_name": "Phil", "last_name": "Foden", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-eng-phil-foden"},
    {"shirt_number": 16, "first_name": "Trent", "last_name": "Alexander-Arnold", "position": Player.Position.MIDFIELDER, "club": "Liverpool", "external_id": "wc26-eng-trent-alexander-arnold"},
    {"shirt_number": 17, "first_name": "Kobbie", "last_name": "Mainoo", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-eng-kobbie-mainoo"},
    {"shirt_number": 18, "first_name": "Conor", "last_name": "Gallagher", "position": Player.Position.MIDFIELDER, "club": "Chelsea", "external_id": "wc26-eng-conor-gallagher"},

    {"shirt_number": 7, "first_name": "Bukayo", "last_name": "Saka", "position": Player.Position.FORWARD, "club": "Arsenal", "external_id": "wc26-eng-bukayo-saka"},
    {"shirt_number": 9, "first_name": "Harry", "last_name": "Kane", "position": Player.Position.FORWARD, "club": "Bayern Munich", "external_id": "wc26-eng-harry-kane"},
    {"shirt_number": 11, "first_name": "Jack", "last_name": "Grealish", "position": Player.Position.FORWARD, "club": "Manchester City", "external_id": "wc26-eng-jack-grealish"},
    {"shirt_number": 19, "first_name": "Cole", "last_name": "Palmer", "position": Player.Position.FORWARD, "club": "Chelsea", "external_id": "wc26-eng-cole-palmer"},
    {"shirt_number": 20, "first_name": "Jarrod", "last_name": "Bowen", "position": Player.Position.FORWARD, "club": "West Ham United", "external_id": "wc26-eng-jarrod-bowen"},
    {"shirt_number": 21, "first_name": "Ivan", "last_name": "Toney", "position": Player.Position.FORWARD, "club": "Brentford", "external_id": "wc26-eng-ivan-toney"},
    {"shirt_number": 22, "first_name": "Anthony", "last_name": "Gordon", "position": Player.Position.FORWARD, "club": "Newcastle United", "external_id": "wc26-eng-anthony-gordon"},
    {"shirt_number": 24, "first_name": "Ollie", "last_name": "Watkins", "position": Player.Position.FORWARD, "club": "Aston Villa", "external_id": "wc26-eng-ollie-watkins"},
    {"shirt_number": 25, "first_name": "Eberechi", "last_name": "Eze", "position": Player.Position.FORWARD, "club": "Crystal Palace", "external_id": "wc26-eng-eberechi-eze"},
    {"shirt_number": 26, "first_name": "Harvey", "last_name": "Elliott", "position": Player.Position.FORWARD, "club": "Liverpool", "external_id": "wc26-eng-harvey-elliott"},
]


CROATIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Dominik", "last_name": "Livakovic", "position": Player.Position.GOALKEEPER, "club": "Fenerbahce", "external_id": "wc26-cro-dominik-livakovic"},
    {"shirt_number": 12, "first_name": "Ivica", "last_name": "Ivusic", "position": Player.Position.GOALKEEPER, "club": "Pafos", "external_id": "wc26-cro-ivica-ivusic"},
    {"shirt_number": 23, "first_name": "Ivo", "last_name": "Grbic", "position": Player.Position.GOALKEEPER, "club": "Atletico Madrid", "external_id": "wc26-cro-ivo-grbic"},

    {"shirt_number": 2, "first_name": "Josip", "last_name": "Juranovic", "position": Player.Position.DEFENDER, "club": "Union Berlin", "external_id": "wc26-cro-josip-juranovic"},
    {"shirt_number": 3, "first_name": "Borna", "last_name": "Sosa", "position": Player.Position.DEFENDER, "club": "Ajax", "external_id": "wc26-cro-borna-sosa"},
    {"shirt_number": 4, "first_name": "Josko", "last_name": "Gvardiol", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-cro-josko-gvardiol"},
    {"shirt_number": 5, "first_name": "Josip", "last_name": "Sutalo", "position": Player.Position.DEFENDER, "club": "Ajax", "external_id": "wc26-cro-josip-sutalo"},
    {"shirt_number": 13, "first_name": "Domagoj", "last_name": "Vida", "position": Player.Position.DEFENDER, "club": "AEK Athens", "external_id": "wc26-cro-domagoj-vida"},
    {"shirt_number": 14, "first_name": "Borna", "last_name": "Barisic", "position": Player.Position.DEFENDER, "club": "Rangers", "external_id": "wc26-cro-borna-barisic"},
    {"shirt_number": 15, "first_name": "Josip", "last_name": "Stanisic", "position": Player.Position.DEFENDER, "club": "Bayer Leverkusen", "external_id": "wc26-cro-josip-stanisic"},

    {"shirt_number": 6, "first_name": "Marcelo", "last_name": "Brozovic", "position": Player.Position.MIDFIELDER, "club": "Al Nassr", "external_id": "wc26-cro-marcelo-brozovic"},
    {"shirt_number": 8, "first_name": "Mateo", "last_name": "Kovacic", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-cro-mateo-kovacic"},
    {"shirt_number": 10, "first_name": "Luka", "last_name": "Modric", "position": Player.Position.MIDFIELDER, "club": "Real Madrid", "external_id": "wc26-cro-luka-modric"},
    {"shirt_number": 16, "first_name": "Mario", "last_name": "Pasalic", "position": Player.Position.MIDFIELDER, "club": "Atalanta", "external_id": "wc26-cro-mario-pasalic"},
    {"shirt_number": 17, "first_name": "Nikola", "last_name": "Vlasic", "position": Player.Position.MIDFIELDER, "club": "Torino", "external_id": "wc26-cro-nikola-vlasic"},
    {"shirt_number": 18, "first_name": "Lovro", "last_name": "Mayer", "position": Player.Position.MIDFIELDER, "club": "Wolfsburg", "external_id": "wc26-cro-lovro-mayer"},

    {"shirt_number": 7, "first_name": "Ivan", "last_name": "Perisic", "position": Player.Position.FORWARD, "club": "Hajduk Split", "external_id": "wc26-cro-ivan-perisic"},
    {"shirt_number": 9, "first_name": "Andrej", "last_name": "Kramaric", "position": Player.Position.FORWARD, "club": "Hoffenheim", "external_id": "wc26-cro-andrej-kramaric"},
    {"shirt_number": 11, "first_name": "Ante", "last_name": "Budimir", "position": Player.Position.FORWARD, "club": "Osasuna", "external_id": "wc26-cro-ante-budimir"},
    {"shirt_number": 19, "first_name": "Bruno", "last_name": "Petkovic", "position": Player.Position.FORWARD, "club": "Dinamo Zagreb", "external_id": "wc26-cro-bruno-petkovic"},
    {"shirt_number": 20, "first_name": "Mislav", "last_name": "Orsic", "position": Player.Position.FORWARD, "club": "Trabzonspor", "external_id": "wc26-cro-mislav-orsic"},
    {"shirt_number": 21, "first_name": "Josip", "last_name": "Brekalo", "position": Player.Position.FORWARD, "club": "Dinamo Zagreb", "external_id": "wc26-cro-josip-brekalo"},
    {"shirt_number": 22, "first_name": "Marco", "last_name": "Livaja", "position": Player.Position.FORWARD, "club": "Hajduk Split", "external_id": "wc26-cro-marko-livaja"},
    {"shirt_number": 24, "first_name": "Dion", "last_name": "Beljo", "position": Player.Position.FORWARD, "club": "Augsburg", "external_id": "wc26-cro-dion-beljo"},
    {"shirt_number": 25, "first_name": "Petar", "last_name": "Musa", "position": Player.Position.FORWARD, "club": "Benfica", "external_id": "wc26-cro-petar-musa"},
    {"shirt_number": 26, "first_name": "Stipe", "last_name": "Biuk", "position": Player.Position.FORWARD, "club": "Los Angeles FC", "external_id": "wc26-cro-stipe-biuk"},
]


GHANA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Lawrence", "last_name": "Ati-Zigi", "position": Player.Position.GOALKEEPER, "club": "St. Gallen", "external_id": "wc26-gha-lawrence-ati-zigi"},
    {"shirt_number": 12, "first_name": "Jojo", "last_name": "Wollacott", "position": Player.Position.GOALKEEPER, "club": "Hibernian", "external_id": "wc26-gha-jojo-wollacott"},
    {"shirt_number": 23, "first_name": "Richard", "last_name": "Ofori", "position": Player.Position.GOALKEEPER, "club": "Orlando Pirates", "external_id": "wc26-gha-richard-ofori"},

    {"shirt_number": 2, "first_name": "Denis", "last_name": "Odoi", "position": Player.Position.DEFENDER, "club": "Club Brugge", "external_id": "wc26-gha-denis-odoi"},
    {"shirt_number": 3, "first_name": "Gideon", "last_name": "Mensah", "position": Player.Position.DEFENDER, "club": "Auxerre", "external_id": "wc26-gha-gideon-mensah"},
    {"shirt_number": 4, "first_name": "Mohammed", "last_name": "Salisu", "position": Player.Position.DEFENDER, "club": "Monaco", "external_id": "wc26-gha-mohammed-salisu"},
    {"shirt_number": 5, "first_name": "Daniel", "last_name": "Amartey", "position": Player.Position.DEFENDER, "club": "Besiktas", "external_id": "wc26-gha-daniel-amartey"},
    {"shirt_number": 13, "first_name": "Alexander", "last_name": "Djiku", "position": Player.Position.DEFENDER, "club": "Fenerbahce", "external_id": "wc26-gha-alexander-djiku"},
    {"shirt_number": 14, "first_name": "Alidu", "last_name": "Seidu", "position": Player.Position.DEFENDER, "club": "Rennes", "external_id": "wc26-gha-alidu-seidu"},
    {"shirt_number": 15, "first_name": "Tariq", "last_name": "Lamptey", "position": Player.Position.DEFENDER, "club": "Brighton", "external_id": "wc26-gha-tariq-lamptey"},

    {"shirt_number": 6, "first_name": "Thomas", "last_name": "Partey", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-gha-thomas-partey"},
    {"shirt_number": 8, "first_name": "Mohammed", "last_name": "Kudus", "position": Player.Position.MIDFIELDER, "club": "West Ham United", "external_id": "wc26-gha-mohammed-kudus"},
    {"shirt_number": 10, "first_name": "Andre", "last_name": "Ayew", "position": Player.Position.MIDFIELDER, "club": "Le Havre", "external_id": "wc26-gha-andre-ayew"},
    {"shirt_number": 16, "first_name": "Salis", "last_name": "Abdul Samed", "position": Player.Position.MIDFIELDER, "club": "Lens", "external_id": "wc26-gha-salis-abdul-samed"},
    {"shirt_number": 17, "first_name": "Daniel-Kofi", "last_name": "Kyereh", "position": Player.Position.MIDFIELDER, "club": "Freiburg", "external_id": "wc26-gha-daniel-kofi-kyereh"},
    {"shirt_number": 18, "first_name": "Kamaldeen", "last_name": "Sulemana", "position": Player.Position.MIDFIELDER, "club": "Southampton", "external_id": "wc26-gha-kamaldeen-sulemana"},

    {"shirt_number": 7, "first_name": "Jordan", "last_name": "Ayew", "position": Player.Position.FORWARD, "club": "Crystal Palace", "external_id": "wc26-gha-jordan-ayew"},
    {"shirt_number": 9, "first_name": "Inaki", "last_name": "Williams", "position": Player.Position.FORWARD, "club": "Athletic Club", "external_id": "wc26-gha-inaki-williams"},
    {"shirt_number": 11, "first_name": "Antoine", "last_name": "Semenyo", "position": Player.Position.FORWARD, "club": "Bournemouth", "external_id": "wc26-gha-antoine-semenyo"},
    {"shirt_number": 19, "first_name": "Felix", "last_name": "Afena-Gyan", "position": Player.Position.FORWARD, "club": "Cremonese", "external_id": "wc26-gha-felix-afena-gyan"},
    {"shirt_number": 20, "first_name": "Abdul", "last_name": "Fatawu Issahaku", "position": Player.Position.FORWARD, "club": "Leicester City", "external_id": "wc26-gha-fatawu-issahaku"},
    {"shirt_number": 21, "first_name": "Osman", "last_name": "Bukari", "position": Player.Position.FORWARD, "club": "Red Star Belgrade", "external_id": "wc26-gha-osman-bukari"},
    {"shirt_number": 22, "first_name": "Ransford", "last_name": "Yeboah", "position": Player.Position.FORWARD, "club": "Hamburg", "external_id": "wc26-gha-ransford-yeboah"},
    {"shirt_number": 24, "first_name": "Joseph", "last_name": "Paintsil", "position": Player.Position.FORWARD, "club": "Genk", "external_id": "wc26-gha-joseph-paintsil"},
    {"shirt_number": 25, "first_name": "Emmanuel", "last_name": "Gyasi", "position": Player.Position.FORWARD, "club": "Empoli", "external_id": "wc26-gha-emmanuel-gyasi"},
    {"shirt_number": 26, "first_name": "Ibrahim", "last_name": "Sadiq", "position": Player.Position.FORWARD, "club": "AZ Alkmaar", "external_id": "wc26-gha-ibrahim-sadiq"},
]


PANAMA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Luis", "last_name": "Mejia", "position": Player.Position.GOALKEEPER, "club": "Nacional", "external_id": "wc26-pan-luis-mejia"},
    {"shirt_number": 12, "first_name": "Orlando", "last_name": "Mosquera", "position": Player.Position.GOALKEEPER, "club": "Bolivar", "external_id": "wc26-pan-orlando-mosquera"},
    {"shirt_number": 23, "first_name": "Jose", "last_name": "Calderon", "position": Player.Position.GOALKEEPER, "club": "Municipal", "external_id": "wc26-pan-jose-calderon"},

    {"shirt_number": 2, "first_name": "Michael", "last_name": "Amir Murillo", "position": Player.Position.DEFENDER, "club": "Marseille", "external_id": "wc26-pan-michael-murillo"},
    {"shirt_number": 3, "first_name": "Harold", "last_name": "Cummings", "position": Player.Position.DEFENDER, "club": "Always Ready", "external_id": "wc26-pan-harold-cummings"},
    {"shirt_number": 4, "first_name": "Fidel", "last_name": "Escobar", "position": Player.Position.DEFENDER, "club": "Saprissa", "external_id": "wc26-pan-fidel-escobar"},
    {"shirt_number": 5, "first_name": "Roman", "last_name": "Torres", "position": Player.Position.DEFENDER, "club": "Cartagines", "external_id": "wc26-pan-roman-torres"},
    {"shirt_number": 13, "first_name": "Eric", "last_name": "Davis", "position": Player.Position.DEFENDER, "club": "Dunajska Streda", "external_id": "wc26-pan-eric-davis"},
    {"shirt_number": 14, "first_name": "Jose", "last_name": "Cordoba", "position": Player.Position.DEFENDER, "club": "Levski Sofia", "external_id": "wc26-pan-jose-cordoba"},
    {"shirt_number": 15, "first_name": "Andres", "last_name": "Andrade", "position": Player.Position.DEFENDER, "club": "Lask", "external_id": "wc26-pan-andres-andrade"},

    {"shirt_number": 6, "first_name": "Anibal", "last_name": "Godoy", "position": Player.Position.MIDFIELDER, "club": "Nashville SC", "external_id": "wc26-pan-anibal-godoy"},
    {"shirt_number": 8, "first_name": "Adalberto", "last_name": "Carrasquilla", "position": Player.Position.MIDFIELDER, "club": "Houston Dynamo", "external_id": "wc26-pan-adalberto-carrasquilla"},
    {"shirt_number": 10, "first_name": "Edgar", "last_name": "Yoel Barcenas", "position": Player.Position.MIDFIELDER, "club": "Mazatlan", "external_id": "wc26-pan-edgar-barcenas"},
    {"shirt_number": 16, "first_name": "Alberto", "last_name": "Quintero", "position": Player.Position.MIDFIELDER, "club": "Universitario", "external_id": "wc26-pan-alberto-quintero"},
    {"shirt_number": 17, "first_name": "Jose Luis", "last_name": "Rodriguez", "position": Player.Position.MIDFIELDER, "club": "Famalicao", "external_id": "wc26-pan-jose-luis-rodriguez"},
    {"shirt_number": 18, "first_name": "Abdiel", "last_name": "Ayarsa", "position": Player.Position.MIDFIELDER, "club": "Aris Limassol", "external_id": "wc26-pan-abdiel-ayarsa"},

    {"shirt_number": 7, "first_name": "Armando", "last_name": "Cooper", "position": Player.Position.FORWARD, "club": "Maccabi Petah Tikva", "external_id": "wc26-pan-armando-cooper"},
    {"shirt_number": 9, "first_name": "Gabriel", "last_name": "Torres", "position": Player.Position.FORWARD, "club": "Alajuelense", "external_id": "wc26-pan-gabriel-torres"},
    {"shirt_number": 11, "first_name": "Rolando", "last_name": "Blackburn", "position": Player.Position.FORWARD, "club": "The Strongest", "external_id": "wc26-pan-rolando-blackburn"},
    {"shirt_number": 19, "first_name": "Ismael", "last_name": "Diaz", "position": Player.Position.FORWARD, "club": "Universidad Catolica", "external_id": "wc26-pan-ismael-diaz"},
    {"shirt_number": 20, "first_name": "Cecilio", "last_name": "Waterman", "position": Player.Position.FORWARD, "club": "Cobresal", "external_id": "wc26-pan-cecilio-waterman"},
    {"shirt_number": 21, "first_name": "Jose", "last_name": "Fajardo", "position": Player.Position.FORWARD, "club": "Cusco FC", "external_id": "wc26-pan-jose-fajardo"},
    {"shirt_number": 22, "first_name": "Edwin", "last_name": "Escobar", "position": Player.Position.FORWARD, "club": "Plaza Amador", "external_id": "wc26-pan-edwin-escobar"},
    {"shirt_number": 24, "first_name": "Freddy", "last_name": "Gondola", "position": Player.Position.FORWARD, "club": "Liga Deportiva Alajuelense", "external_id": "wc26-pan-freddy-gondola"},
    {"shirt_number": 25, "first_name": "Alfredo", "last_name": "Stephens", "position": Player.Position.FORWARD, "club": "9 de Octubre", "external_id": "wc26-pan-alfredo-stephens"},
    {"shirt_number": 26, "first_name": "Cristian", "last_name": "Quintero", "position": Player.Position.FORWARD, "club": "Tauro", "external_id": "wc26-pan-cristian-quintero"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo L del Mundial 2026"

    def load_players_for_team(self, team, players_data):
        created_count = 0
        updated_count = 0

        for item in players_data:
            player, created = Player.objects.update_or_create(
                team=team,
                shirt_number=item["shirt_number"],
                defaults={
                    "first_name": item["first_name"],
                    "last_name": item["last_name"],
                    "position": item["position"],
                    "club": item.get("club", ""),
                    "is_called_up": True,
                    "external_id": item["external_id"],
                },
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        return created_count, updated_count

    def handle(self, *args, **kwargs):
        try:
            england = Team.objects.get(fifa_code="ENG")
            croatia = Team.objects.get(fifa_code="CRO")
            ghana = Team.objects.get(fifa_code="GHA")
            panama = Team.objects.get(fifa_code="PAN")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo L en la base de datos: {exc}")

        results = []

        results.append(("England", *self.load_players_for_team(england, ENGLAND_PLAYERS)))
        results.append(("Croatia", *self.load_players_for_team(croatia, CROATIA_PLAYERS)))
        results.append(("Ghana", *self.load_players_for_team(ghana, GHANA_PLAYERS)))
        results.append(("Panama", *self.load_players_for_team(panama, PANAMA_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo L completada."))