from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


BRAZIL_PLAYERS = [
    {"shirt_number": 1, "first_name": "Alisson", "last_name": "Becker", "position": Player.Position.GOALKEEPER, "club": "Liverpool", "external_id": "wc26-bra-alisson-becker"},
    {"shirt_number": 12, "first_name": "Weverton", "last_name": "", "position": Player.Position.GOALKEEPER, "club": "Gremio", "external_id": "wc26-bra-weverton"},
    {"shirt_number": 23, "first_name": "Ederson", "last_name": "Moraes", "position": Player.Position.GOALKEEPER, "club": "Fenerbahce", "external_id": "wc26-bra-ederson"},

    {"shirt_number": 2, "first_name": "Wesley", "last_name": "Vinicius", "position": Player.Position.DEFENDER, "club": "Roma", "external_id": "wc26-bra-wesley-vinicius"},
    {"shirt_number": 3, "first_name": "Gabriel", "last_name": "Magalhaes", "position": Player.Position.DEFENDER, "club": "Arsenal", "external_id": "wc26-bra-gabriel-magalhaes"},
    {"shirt_number": 4, "first_name": "Marquinhos", "last_name": "", "position": Player.Position.DEFENDER, "club": "Paris Saint-Germain", "external_id": "wc26-bra-marquinhos"},
    {"shirt_number": 6, "first_name": "Alex", "last_name": "Sandro", "position": Player.Position.DEFENDER, "club": "Flamengo", "external_id": "wc26-bra-alex-sandro"},
    {"shirt_number": 13, "first_name": "Danilo", "last_name": "", "position": Player.Position.DEFENDER, "club": "Flamengo", "external_id": "wc26-bra-danilo"},
    {"shirt_number": 14, "first_name": "Bremer", "last_name": "", "position": Player.Position.DEFENDER, "club": "Juventus", "external_id": "wc26-bra-bremer"},
    {"shirt_number": 15, "first_name": "Leo", "last_name": "Pereira", "position": Player.Position.DEFENDER, "club": "Flamengo", "external_id": "wc26-bra-leo-pereira"},
    {"shirt_number": 16, "first_name": "Douglas", "last_name": "Santos", "position": Player.Position.DEFENDER, "club": "Zenit", "external_id": "wc26-bra-douglas-santos"},
    {"shirt_number": 25, "first_name": "Roger", "last_name": "Ibanez", "position": Player.Position.DEFENDER, "club": "Al Ahli", "external_id": "wc26-bra-roger-ibanez"},

    {"shirt_number": 5, "first_name": "Casemiro", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-bra-casemiro"},
    {"shirt_number": 8, "first_name": "Bruno", "last_name": "Guimaraes", "position": Player.Position.MIDFIELDER, "club": "Newcastle United", "external_id": "wc26-bra-bruno-guimaraes"},
    {"shirt_number": 15, "first_name": "Fabinho", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Al Ittihad", "external_id": "wc26-bra-fabinho"},
    {"shirt_number": 17, "first_name": "Danilo", "last_name": "Santos", "position": Player.Position.MIDFIELDER, "club": "Botafogo", "external_id": "wc26-bra-danilo-santos"},
    {"shirt_number": 20, "first_name": "Lucas", "last_name": "Paqueta", "position": Player.Position.MIDFIELDER, "club": "Flamengo", "external_id": "wc26-bra-lucas-paqueta"},

    {"shirt_number": 7, "first_name": "Vinicius", "last_name": "Junior", "position": Player.Position.FORWARD, "club": "Real Madrid", "external_id": "wc26-bra-vinicius-junior"},
    {"shirt_number": 9, "first_name": "Matheus", "last_name": "Cunha", "position": Player.Position.FORWARD, "club": "Manchester United", "external_id": "wc26-bra-matheus-cunha"},
    {"shirt_number": 10, "first_name": "Neymar", "last_name": "Junior", "position": Player.Position.FORWARD, "club": "Santos", "external_id": "wc26-bra-neymar-junior"},
    {"shirt_number": 11, "first_name": "Raphinha", "last_name": "", "position": Player.Position.FORWARD, "club": "Barcelona", "external_id": "wc26-bra-raphinha"},
    {"shirt_number": 18, "first_name": "Endrick", "last_name": "", "position": Player.Position.FORWARD, "club": "Lyon", "external_id": "wc26-bra-endrick"},
    {"shirt_number": 19, "first_name": "Luiz", "last_name": "Henrique", "position": Player.Position.FORWARD, "club": "Zenit", "external_id": "wc26-bra-luiz-henrique"},
    {"shirt_number": 21, "first_name": "Gabriel", "last_name": "Martinelli", "position": Player.Position.FORWARD, "club": "Arsenal", "external_id": "wc26-bra-gabriel-martinelli"},
    {"shirt_number": 22, "first_name": "Igor", "last_name": "Thiago", "position": Player.Position.FORWARD, "club": "Brentford", "external_id": "wc26-bra-igor-thiago"},
    {"shirt_number": 26, "first_name": "Rayan", "last_name": "", "position": Player.Position.FORWARD, "club": "Bournemouth", "external_id": "wc26-bra-rayan"},
]


MOROCCO_PLAYERS = [
    # Porteros
    {"shirt_number": 1, "first_name": "Yassine", "last_name": "Bounou", "position": Player.Position.GOALKEEPER, "club": "Al Hilal", "external_id": "wc26-mar-yassine-bounou"},
    {"shirt_number": 12, "first_name": "Munir", "last_name": "Mohamedi", "position": Player.Position.GOALKEEPER, "club": "Al Wehda", "external_id": "wc26-mar-munir-mohamedi"},
    {"shirt_number": 23, "first_name": "Ahmed", "last_name": "Reda Tagnaouti", "position": Player.Position.GOALKEEPER, "club": "Wydad AC", "external_id": "wc26-mar-ahmed-reda"},

    # Defensas
    {"shirt_number": 2, "first_name": "Achraf", "last_name": "Hakimi", "position": Player.Position.DEFENDER, "club": "Paris Saint-Germain", "external_id": "wc26-mar-achraf-hakimi"},
    {"shirt_number": 3, "first_name": "Noussair", "last_name": "Mazraoui", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-mar-noussair-mazraoui"},
    {"shirt_number": 4, "first_name": "Romain", "last_name": "Saiss", "position": Player.Position.DEFENDER, "club": "Al Saad", "external_id": "wc26-mar-romain-saiss"},
    {"shirt_number": 5, "first_name": "Nayef", "last_name": "Aguerd", "position": Player.Position.DEFENDER, "club": "West Ham United", "external_id": "wc26-mar-nayef-aguerd"},
    {"shirt_number": 13, "first_name": "Jawad", "last_name": "El Yamiq", "position": Player.Position.DEFENDER, "club": "Al Wahda", "external_id": "wc26-mar-jawad-el-yamiq"},
    {"shirt_number": 14, "first_name": "Yahia", "last_name": "Attiyat Allah", "position": Player.Position.DEFENDER, "club": "Wydad AC", "external_id": "wc26-mar-yahia-attiyat"},

    # Mediocentros
    {"shirt_number": 6, "first_name": "Sofyan", "last_name": "Amrabat", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-mar-sofyan-amrabat"},
    {"shirt_number": 8, "first_name": "Azzedine", "last_name": "Ounahi", "position": Player.Position.MIDFIELDER, "club": "Marseille", "external_id": "wc26-mar-azzedine-ounahi"},
    {"shirt_number": 10, "first_name": "Hakim", "last_name": "Ziyech", "position": Player.Position.MIDFIELDER, "club": "Galatasaray", "external_id": "wc26-mar-hakim-ziyech"},
    {"shirt_number": 15, "first_name": "Abdelhamid", "last_name": "Sabiri", "position": Player.Position.MIDFIELDER, "club": "Al Fayha", "external_id": "wc26-mar-abdelhamid-sabiri"},
    {"shirt_number": 16, "first_name": "Bilal", "last_name": "El Khannouss", "position": Player.Position.MIDFIELDER, "club": "Genk", "external_id": "wc26-mar-bilal-el-khannouss"},

    # Delanteros
    {"shirt_number": 7, "first_name": "Sofiane", "last_name": "Boufal", "position": Player.Position.FORWARD, "club": "Al Rayyan", "external_id": "wc26-mar-sofiane-boufal"},
    {"shirt_number": 9, "first_name": "Youssef", "last_name": "En-Nesyri", "position": Player.Position.FORWARD, "club": "Sevilla", "external_id": "wc26-mar-youssef-en-nesyri"},
    {"shirt_number": 11, "first_name": "Abde", "last_name": "Ezzalzouli", "position": Player.Position.FORWARD, "club": "Real Betis", "external_id": "wc26-mar-abde-ezzalzouli"},
    {"shirt_number": 17, "first_name": "Walid", "last_name": "Cheddira", "position": Player.Position.FORWARD, "club": "Frosinone", "external_id": "wc26-mar-walid-cheddira"},
    {"shirt_number": 18, "first_name": "Amine", "last_name": "Adli", "position": Player.Position.FORWARD, "club": "Bayer Leverkusen", "external_id": "wc26-mar-amine-adli"},
    {"shirt_number": 19, "first_name": "Tarik", "last_name": "Tissoudali", "position": Player.Position.FORWARD, "club": "Gent", "external_id": "wc26-mar-tarik-tissoudali"},
    {"shirt_number": 20, "first_name": "Ilias", "last_name": "Chair", "position": Player.Position.FORWARD, "club": "QPR", "external_id": "wc26-mar-ilias-chair"},
    {"shirt_number": 21, "first_name": "Zakaria", "last_name": "Aboukhlal", "position": Player.Position.FORWARD, "club": "Toulouse", "external_id": "wc26-mar-zakaria-aboukhlal"},
]


HAITI_PLAYERS = [
    {"shirt_number": 1, "first_name": "Johny", "last_name": "Placide", "position": Player.Position.GOALKEEPER, "club": "Bastia", "external_id": "wc26-hai-johny-placide"},
    {"shirt_number": 12, "first_name": "Alexandre", "last_name": "Pierre", "position": Player.Position.GOALKEEPER, "club": "Sochaux", "external_id": "wc26-hai-alexandre-pierre"},
    {"shirt_number": 23, "first_name": "Josue", "last_name": "Duverger", "position": Player.Position.GOALKEEPER, "club": "Cosmos Koblenz", "external_id": "wc26-hai-josue-duverger"},

    {"shirt_number": 2, "first_name": "Carlens", "last_name": "Arcus", "position": Player.Position.DEFENDER, "club": "Angers", "external_id": "wc26-hai-carlens-arcus"},
    {"shirt_number": 3, "first_name": "Ricardo", "last_name": "Ade", "position": Player.Position.DEFENDER, "club": "LDU Quito", "external_id": "wc26-hai-ricardo-ade"},
    {"shirt_number": 4, "first_name": "Hannes", "last_name": "Delcroix", "position": Player.Position.DEFENDER, "club": "Lugano", "external_id": "wc26-hai-hannes-delcroix"},
    {"shirt_number": 5, "first_name": "Martin", "last_name": "Experience", "position": Player.Position.DEFENDER, "club": "Nancy", "external_id": "wc26-hai-martin-experience"},
    {"shirt_number": 13, "first_name": "Lacroix", "last_name": "Markhus", "position": Player.Position.DEFENDER, "club": "Colorado Springs", "external_id": "wc26-hai-lacroix-markhus"},
    {"shirt_number": 14, "first_name": "Jean-Kevin", "last_name": "Duverne", "position": Player.Position.DEFENDER, "club": "Gent", "external_id": "wc26-hai-jean-kevin-duverne"},
    {"shirt_number": 15, "first_name": "Wilguens", "last_name": "Paugain", "position": Player.Position.DEFENDER, "club": "Zulte Waregem", "external_id": "wc26-hai-wilguens-paugain"},

    {"shirt_number": 6, "first_name": "Carl", "last_name": "Sainte", "position": Player.Position.MIDFIELDER, "club": "El Paso", "external_id": "wc26-hai-carl-sainte"},
    {"shirt_number": 8, "first_name": "Jean-Ricner", "last_name": "Bellegarde", "position": Player.Position.MIDFIELDER, "club": "Wolves", "external_id": "wc26-hai-jean-bellegarde"},
    {"shirt_number": 10, "first_name": "Leverton", "last_name": "Pierre", "position": Player.Position.MIDFIELDER, "club": "Vizela", "external_id": "wc26-hai-leverton-pierre"},
    {"shirt_number": 16, "first_name": "Danley", "last_name": "Jean Jacques", "position": Player.Position.MIDFIELDER, "club": "Philadelphia Union", "external_id": "wc26-hai-danley-jean-jacques"},
    {"shirt_number": 17, "first_name": "Dominique", "last_name": "Simon", "position": Player.Position.MIDFIELDER, "club": "Tatran Presov", "external_id": "wc26-hai-dominique-simon"},
    {"shirt_number": 18, "first_name": "Woodensky", "last_name": "Pierre", "position": Player.Position.MIDFIELDER, "club": "Violette", "external_id": "wc26-hai-woodensky-pierre"},

    {"shirt_number": 7, "first_name": "Derrick", "last_name": "Etienne", "position": Player.Position.FORWARD, "club": "Toronto FC", "external_id": "wc26-hai-derrick-etienne"},
    {"shirt_number": 9, "first_name": "Duckens", "last_name": "Nazon", "position": Player.Position.FORWARD, "club": "Esteghlal", "external_id": "wc26-hai-duckens-nazon"},
    {"shirt_number": 11, "first_name": "Don Louicius", "last_name": "Deedson", "position": Player.Position.FORWARD, "club": "FC Dallas", "external_id": "wc26-hai-deedson-louicius"},
    {"shirt_number": 19, "first_name": "Ruben", "last_name": "Providence", "position": Player.Position.FORWARD, "club": "Almere City", "external_id": "wc26-hai-ruben-providence"},
    {"shirt_number": 20, "first_name": "Lenny", "last_name": "Joseph", "position": Player.Position.FORWARD, "club": "Ferencvaros", "external_id": "wc26-hai-lenny-joseph"},
    {"shirt_number": 21, "first_name": "Wilson", "last_name": "Isidor", "position": Player.Position.FORWARD, "club": "Sunderland", "external_id": "wc26-hai-wilson-isidor"},
    {"shirt_number": 22, "first_name": "Yassin", "last_name": "Fortune", "position": Player.Position.FORWARD, "club": "Vizela", "external_id": "wc26-hai-yassin-fortune"},
    {"shirt_number": 24, "first_name": "Frantzdy", "last_name": "Pierrot", "position": Player.Position.FORWARD, "club": "Rizespor", "external_id": "wc26-hai-frantzdy-pierrot"},
    {"shirt_number": 25, "first_name": "Josue", "last_name": "Casimir", "position": Player.Position.FORWARD, "club": "Auxerre", "external_id": "wc26-hai-josue-casimir"},
    {"shirt_number": 26, "first_name": "Woodensky", "last_name": "Paupie Pierre", "position": Player.Position.FORWARD, "club": "Violette", "external_id": "wc26-hai-woodensky-paupie"},
]


SCOTLAND_PLAYERS = [
    {"shirt_number": 1, "first_name": "Angus", "last_name": "Gunn", "position": Player.Position.GOALKEEPER, "club": "Norwich City", "external_id": "wc26-sco-angus-gunn"},
    {"shirt_number": 12, "first_name": "Zander", "last_name": "Clark", "position": Player.Position.GOALKEEPER, "club": "Hearts", "external_id": "wc26-sco-zander-clark"},
    {"shirt_number": 23, "first_name": "Liam", "last_name": "Kelly", "position": Player.Position.GOALKEEPER, "club": "Motherwell", "external_id": "wc26-sco-liam-kelly"},

    {"shirt_number": 2, "first_name": "Aaron", "last_name": "Hickey", "position": Player.Position.DEFENDER, "club": "Brentford", "external_id": "wc26-sco-aaron-hickey"},
    {"shirt_number": 3, "first_name": "Andrew", "last_name": "Robertson", "position": Player.Position.DEFENDER, "club": "Liverpool", "external_id": "wc26-sco-andrew-robertson"},
    {"shirt_number": 4, "first_name": "Scott", "last_name": "McKenna", "position": Player.Position.DEFENDER, "club": "Kobenhavn", "external_id": "wc26-sco-scott-mckenna"},
    {"shirt_number": 5, "first_name": "Ryan", "last_name": "Porteous", "position": Player.Position.DEFENDER, "club": "Watford", "external_id": "wc26-sco-ryan-porteous"},
    {"shirt_number": 13, "first_name": "Kieran", "last_name": "Tierney", "position": Player.Position.DEFENDER, "club": "Real Sociedad", "external_id": "wc26-sco-kieran-tierney"},
    {"shirt_number": 14, "first_name": "Jack", "last_name": "Hendry", "position": Player.Position.DEFENDER, "club": "Al Ettifaq", "external_id": "wc26-sco-jack-hendry"},
    {"shirt_number": 15, "first_name": "Nathan", "last_name": "Patterson", "position": Player.Position.DEFENDER, "club": "Everton", "external_id": "wc26-sco-nathan-patterson"},
    {"shirt_number": 16, "first_name": "John", "last_name": "Souttar", "position": Player.Position.DEFENDER, "club": "Rangers", "external_id": "wc26-sco-john-souttar"},

    {"shirt_number": 6, "first_name": "Billy", "last_name": "Gilmour", "position": Player.Position.MIDFIELDER, "club": "Brighton", "external_id": "wc26-sco-billy-gilmour"},
    {"shirt_number": 7, "first_name": "John", "last_name": "McGinn", "position": Player.Position.MIDFIELDER, "club": "Aston Villa", "external_id": "wc26-sco-john-mcginn"},
    {"shirt_number": 8, "first_name": "Callum", "last_name": "McGregor", "position": Player.Position.MIDFIELDER, "club": "Celtic", "external_id": "wc26-sco-callum-mcgregor"},
    {"shirt_number": 10, "first_name": "Ryan", "last_name": "Christie", "position": Player.Position.MIDFIELDER, "club": "Bournemouth", "external_id": "wc26-sco-ryan-christie"},
    {"shirt_number": 17, "first_name": "Scott", "last_name": "McTominay", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-sco-scott-mctominay"},
    {"shirt_number": 18, "first_name": "Lewis", "last_name": "Ferguson", "position": Player.Position.MIDFIELDER, "club": "Bologna", "external_id": "wc26-sco-lewis-ferguson"},
    {"shirt_number": 19, "first_name": "Kenny", "last_name": "McLean", "position": Player.Position.MIDFIELDER, "club": "Norwich City", "external_id": "wc26-sco-kenny-mclean"},

    {"shirt_number": 9, "first_name": "Lyndon", "last_name": "Dykes", "position": Player.Position.FORWARD, "club": "QPR", "external_id": "wc26-sco-lyndon-dykes"},
    {"shirt_number": 11, "first_name": "Che", "last_name": "Adams", "position": Player.Position.FORWARD, "club": "Southampton", "external_id": "wc26-sco-che-adams"},
    {"shirt_number": 20, "first_name": "Lawrence", "last_name": "Shankland", "position": Player.Position.FORWARD, "club": "Hearts", "external_id": "wc26-sco-lawrence-shankland"},
    {"shirt_number": 21, "first_name": "Jacob", "last_name": "Brown", "position": Player.Position.FORWARD, "club": "Luton Town", "external_id": "wc26-sco-jacob-brown"},
    {"shirt_number": 22, "first_name": "Lewis", "last_name": "Morgan", "position": Player.Position.FORWARD, "club": "New York Red Bulls", "external_id": "wc26-sco-lewis-morgan"},
    {"shirt_number": 24, "first_name": "Ben", "last_name": "Doak", "position": Player.Position.FORWARD, "club": "Liverpool", "external_id": "wc26-sco-ben-doak"},
    {"shirt_number": 25, "first_name": "Kevin", "last_name": "Nisbet", "position": Player.Position.FORWARD, "club": "Millwall", "external_id": "wc26-sco-kevin-nisbet"},
    {"shirt_number": 26, "first_name": "Tony", "last_name": "Ralls", "position": Player.Position.FORWARD, "club": "Cardiff City", "external_id": "wc26-sco-tony-ralls"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo C del Mundial 2026"

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
            brazil = Team.objects.get(fifa_code="BRA")
            morocco = Team.objects.get(fifa_code="MAR")
            haiti = Team.objects.get(fifa_code="HAI")
            scotland = Team.objects.get(fifa_code="SCO")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo C en la base de datos: {exc}")

        results = []

        results.append(("Brazil", *self.load_players_for_team(brazil, BRAZIL_PLAYERS)))
        results.append(("Morocco", *self.load_players_for_team(morocco, MOROCCO_PLAYERS)))
        results.append(("Haiti", *self.load_players_for_team(haiti, HAITI_PLAYERS)))
        results.append(("Scotland", *self.load_players_for_team(scotland, SCOTLAND_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo C completada."))