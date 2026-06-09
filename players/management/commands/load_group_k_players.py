from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


PORTUGAL_PLAYERS = [
    {"shirt_number": 1, "first_name": "Diogo", "last_name": "Costa", "position": Player.Position.GOALKEEPER, "club": "Porto", "external_id": "wc26-por-diogo-costa"},
    {"shirt_number": 12, "first_name": "Rui", "last_name": "Patricio", "position": Player.Position.GOALKEEPER, "club": "Roma", "external_id": "wc26-por-rui-patricio"},
    {"shirt_number": 23, "first_name": "Jose", "last_name": "Sa", "position": Player.Position.GOALKEEPER, "club": "Wolverhampton Wanderers", "external_id": "wc26-por-jose-sa"},

    {"shirt_number": 2, "first_name": "Joao", "last_name": "Cancelo", "position": Player.Position.DEFENDER, "club": "Barcelona", "external_id": "wc26-por-joao-cancelo"},
    {"shirt_number": 3, "first_name": "Ruben", "last_name": "Dias", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-por-ruben-dias"},
    {"shirt_number": 4, "first_name": "Antonio", "last_name": "Silva", "position": Player.Position.DEFENDER, "club": "Benfica", "external_id": "wc26-por-antonio-silva"},
    {"shirt_number": 5, "first_name": "Diogo", "last_name": "Dalot", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-por-diogo-dalot"},
    {"shirt_number": 13, "first_name": "Nuno", "last_name": "Mendes", "position": Player.Position.DEFENDER, "club": "Paris Saint-Germain", "external_id": "wc26-por-nuno-mendes"},
    {"shirt_number": 14, "first_name": "Pepe", "last_name": "", "position": Player.Position.DEFENDER, "club": "Porto", "external_id": "wc26-por-pepe"},
    {"shirt_number": 15, "first_name": "Goncalo", "last_name": "Inacio", "position": Player.Position.DEFENDER, "club": "Sporting CP", "external_id": "wc26-por-goncalo-inacio"},

    {"shirt_number": 6, "first_name": "Bruno", "last_name": "Fernandes", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-por-bruno-fernandes"},
    {"shirt_number": 8, "first_name": "Bernardo", "last_name": "Silva", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-por-bernardo-silva"},
    {"shirt_number": 10, "first_name": "Vitinha", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Paris Saint-Germain", "external_id": "wc26-por-vitinha"},
    {"shirt_number": 16, "first_name": "Joao", "last_name": "Palhinha", "position": Player.Position.MIDFIELDER, "club": "Bayern Munich", "external_id": "wc26-por-joao-palhinha"},
    {"shirt_number": 17, "first_name": "Otavio", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Al Nassr", "external_id": "wc26-por-otavio"},
    {"shirt_number": 18, "first_name": "Ruben", "last_name": "Neves", "position": Player.Position.MIDFIELDER, "club": "Al Hilal", "external_id": "wc26-por-ruben-neves"},

    {"shirt_number": 7, "first_name": "Cristiano", "last_name": "Ronaldo", "position": Player.Position.FORWARD, "club": "Al Nassr", "external_id": "wc26-por-cristiano-ronaldo"},
    {"shirt_number": 9, "first_name": "Goncalo", "last_name": "Ramos", "position": Player.Position.FORWARD, "club": "Paris Saint-Germain", "external_id": "wc26-por-goncalo-ramos"},
    {"shirt_number": 11, "first_name": "Rafael", "last_name": "Leao", "position": Player.Position.FORWARD, "club": "AC Milan", "external_id": "wc26-por-rafael-leao"},
    {"shirt_number": 19, "first_name": "Diogo", "last_name": "Jota", "position": Player.Position.FORWARD, "club": "Liverpool", "external_id": "wc26-por-diogo-jota"},
    {"shirt_number": 20, "first_name": "Pedro", "last_name": "Neto", "position": Player.Position.FORWARD, "club": "Wolverhampton Wanderers", "external_id": "wc26-por-pedro-neto"},
    {"shirt_number": 21, "first_name": "Joao", "last_name": "Felix", "position": Player.Position.FORWARD, "club": "Barcelona", "external_id": "wc26-por-joao-felix"},
    {"shirt_number": 22, "first_name": "Francisco", "last_name": "Conceicao", "position": Player.Position.FORWARD, "club": "Porto", "external_id": "wc26-por-francisco-conceicao"},
    {"shirt_number": 24, "first_name": "Ricardo", "last_name": "Horta", "position": Player.Position.FORWARD, "club": "Braga", "external_id": "wc26-por-ricardo-horta"},
    {"shirt_number": 25, "first_name": "Bruma", "last_name": "", "position": Player.Position.FORWARD, "club": "Sporting CP", "external_id": "wc26-por-bruma"},
    {"shirt_number": 26, "first_name": "Goncalo", "last_name": "Guedes", "position": Player.Position.FORWARD, "club": "Villarreal", "external_id": "wc26-por-goncalo-guedes"},
]


DR_CONGO_PLAYERS = [
    {"shirt_number": 1, "first_name": "Lionel", "last_name": "Mpasi", "position": Player.Position.GOALKEEPER, "club": "Rodez", "external_id": "wc26-cod-lionel-mpasi"},
    {"shirt_number": 12, "first_name": "Joel", "last_name": "Kiassumbua", "position": Player.Position.GOALKEEPER, "club": "Servette", "external_id": "wc26-cod-joel-kiassumbua"},
    {"shirt_number": 23, "first_name": "Siadi", "last_name": "Baggio", "position": Player.Position.GOALKEEPER, "club": "TP Mazembe", "external_id": "wc26-cod-siadi-baggio"},

    {"shirt_number": 2, "first_name": "Dieumerci", "last_name": "Mukoko", "position": Player.Position.DEFENDER, "club": "TP Mazembe", "external_id": "wc26-cod-dieumerci-mukoko"},
    {"shirt_number": 3, "first_name": "Chancel", "last_name": "Mbemba", "position": Player.Position.DEFENDER, "club": "Marseille", "external_id": "wc26-cod-chancel-mbemba"},
    {"shirt_number": 4, "first_name": "Dylan", "last_name": "Batubinsika", "position": Player.Position.DEFENDER, "club": "Saint-Etienne", "external_id": "wc26-cod-dylan-batubinsika"},
    {"shirt_number": 5, "first_name": "Arthur", "last_name": "Masuaku", "position": Player.Position.DEFENDER, "club": "Besiktas", "external_id": "wc26-cod-arthur-masuaku"},
    {"shirt_number": 13, "first_name": "Joris", "last_name": "Kayembe", "position": Player.Position.DEFENDER, "club": "Genk", "external_id": "wc26-cod-joris-kayembe"},
    {"shirt_number": 14, "first_name": "Gedeon", "last_name": "Kalulu", "position": Player.Position.DEFENDER, "club": "Lorient", "external_id": "wc26-cod-gedeon-kalulu"},
    {"shirt_number": 15, "first_name": "Christian", "last_name": "Luyindama", "position": Player.Position.DEFENDER, "club": "Al Taawoun", "external_id": "wc26-cod-christian-luyindama"},

    {"shirt_number": 6, "first_name": "Samuel", "last_name": "Moutoussamy", "position": Player.Position.MIDFIELDER, "club": "Nantes", "external_id": "wc26-cod-samuel-moutoussamy"},
    {"shirt_number": 8, "first_name": "Gael", "last_name": "Kakuta", "position": Player.Position.MIDFIELDER, "club": "Amiens", "external_id": "wc26-cod-gael-kakuta"},
    {"shirt_number": 10, "first_name": "Theo", "last_name": "Bongonda", "position": Player.Position.MIDFIELDER, "club": "Cadiz", "external_id": "wc26-cod-theo-bongonda"},
    {"shirt_number": 16, "first_name": "Charles", "last_name": "Pickel", "position": Player.Position.MIDFIELDER, "club": "Cremonese", "external_id": "wc26-cod-charles-pickel"},
    {"shirt_number": 17, "first_name": "Aaron", "last_name": "Wan-Bissaka", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-cod-aaron-wan-bissaka"},
    {"shirt_number": 18, "first_name": "Neeskens", "last_name": "Kebano", "position": Player.Position.MIDFIELDER, "club": "Al Jazira", "external_id": "wc26-cod-neeskens-kebano"},

    {"shirt_number": 7, "first_name": "Cedric", "last_name": "Bakambu", "position": Player.Position.FORWARD, "club": "Real Betis", "external_id": "wc26-cod-cedric-bakambu"},
    {"shirt_number": 9, "first_name": "Fiston", "last_name": "Mayele", "position": Player.Position.FORWARD, "club": "Pyramids FC", "external_id": "wc26-cod-fiston-mayele"},
    {"shirt_number": 11, "first_name": "Yoane", "last_name": "Wissa", "position": Player.Position.FORWARD, "club": "Brentford", "external_id": "wc26-cod-yoane-wissa"},
    {"shirt_number": 19, "first_name": "Jackson", "last_name": "Muleka", "position": Player.Position.FORWARD, "club": "Besiktas", "external_id": "wc26-cod-jackson-muleka"},
    {"shirt_number": 20, "first_name": "Meschack", "last_name": "Elia", "position": Player.Position.FORWARD, "club": "Young Boys", "external_id": "wc26-cod-meschack-elia"},
    {"shirt_number": 21, "first_name": "Ben", "last_name": "Malango", "position": Player.Position.FORWARD, "club": "Qatar SC", "external_id": "wc26-cod-ben-malango"},
    {"shirt_number": 22, "first_name": "Silas", "last_name": "Katomp a Mvumpa", "position": Player.Position.FORWARD, "club": "Stuttgart", "external_id": "wc26-cod-silas-mvumpa"},
    {"shirt_number": 24, "first_name": "Jonathan", "last_name": "Bolingi", "position": Player.Position.FORWARD, "club": "Buriram United", "external_id": "wc26-cod-jonathan-bolingi"},
    {"shirt_number": 25, "first_name": "Paul-Jose", "last_name": "Mpoku", "position": Player.Position.FORWARD, "club": "Konyaspor", "external_id": "wc26-cod-paul-jose-mpoku"},
    {"shirt_number": 26, "first_name": "Dieumerci", "last_name": "Ndongala", "position": Player.Position.FORWARD, "club": "Apollon Limassol", "external_id": "wc26-cod-dieumerci-ndongala"},
]


UZBEKISTAN_PLAYERS = [
    {"shirt_number": 1, "first_name": "Eldor", "last_name": "Suyunov", "position": Player.Position.GOALKEEPER, "club": "Pakhtakor", "external_id": "wc26-uzb-eldor-suyunov"},
    {"shirt_number": 12, "first_name": "Abdumutalib", "last_name": "Abdullaev", "position": Player.Position.GOALKEEPER, "club": "Lokomotiv Tashkent", "external_id": "wc26-uzb-abdumutalib-abdullaev"},
    {"shirt_number": 23, "first_name": "Botirali", "last_name": "Ergashev", "position": Player.Position.GOALKEEPER, "club": "Nasaf", "external_id": "wc26-uzb-botirali-ergashev"},

    {"shirt_number": 2, "first_name": "Otabek", "last_name": "Shukurov", "position": Player.Position.DEFENDER, "club": "Sharjah", "external_id": "wc26-uzb-otabek-shukurov"},
    {"shirt_number": 3, "first_name": "Anzur", "last_name": "Ismailov", "position": Player.Position.DEFENDER, "club": "Pakhtakor", "external_id": "wc26-uzb-anzur-ismailov"},
    {"shirt_number": 4, "first_name": "Doston", "last_name": "Bekhkamov", "position": Player.Position.DEFENDER, "club": "Bunyodkor", "external_id": "wc26-uzb-doston-bekhkamov"},
    {"shirt_number": 5, "first_name": "Rustamjon", "last_name": "Ashurmatov", "position": Player.Position.DEFENDER, "club": "Gangwon", "external_id": "wc26-uzb-rustamjon-ashurmatov"},
    {"shirt_number": 13, "first_name": "Khojiakbar", "last_name": "Alijonov", "position": Player.Position.DEFENDER, "club": "Pakhtakor", "external_id": "wc26-uzb-khojiakbar-alijonov"},
    {"shirt_number": 14, "first_name": "Abbosbek", "last_name": "Fayzullayev", "position": Player.Position.DEFENDER, "club": "CSKA Moscow", "external_id": "wc26-uzb-abbosbek-fayzullayev"},
    {"shirt_number": 15, "first_name": "Jaloliddin", "last_name": "Masharipov", "position": Player.Position.DEFENDER, "club": "Al Nassr", "external_id": "wc26-uzb-jaloliddin-masharipov"},

    {"shirt_number": 6, "first_name": "Odil", "last_name": "Ahmedov", "position": Player.Position.MIDFIELDER, "club": "Cangzhou Mighty Lions", "external_id": "wc26-uzb-odil-ahmedov"},
    {"shirt_number": 8, "first_name": "Javokhir", "last_name": "Sidikov", "position": Player.Position.MIDFIELDER, "club": "Pakhtakor", "external_id": "wc26-uzb-javokhir-sidikov"},
    {"shirt_number": 10, "first_name": "Javlon", "last_name": "Qosimov", "position": Player.Position.MIDFIELDER, "club": "AGMK", "external_id": "wc26-uzb-javlon-qosimov"},
    {"shirt_number": 16, "first_name": "Ikromjon", "last_name": "Alibaev", "position": Player.Position.MIDFIELDER, "club": "Seongnam", "external_id": "wc26-uzb-ikromjon-alibaev"},
    {"shirt_number": 17, "first_name": "Doniyor", "last_name": "Narzikulov", "position": Player.Position.MIDFIELDER, "club": "Bunyodkor", "external_id": "wc26-uzb-doniyor-narzikulov"},
    {"shirt_number": 18, "first_name": "Akmal", "last_name": "Kholmurodov", "position": Player.Position.MIDFIELDER, "club": "Nasaf", "external_id": "wc26-uzb-akmal-kholmurodov"},

    {"shirt_number": 7, "first_name": "Eldor", "last_name": "Shomurodov", "position": Player.Position.FORWARD, "club": "Cagliari", "external_id": "wc26-uzb-eldor-shomurodov"},
    {"shirt_number": 9, "first_name": "Igor", "last_name": "Sergeev", "position": Player.Position.FORWARD, "club": "Tobol", "external_id": "wc26-uzb-igor-sergeev"},
    {"shirt_number": 11, "first_name": "Khojimat", "last_name": "Erkinov", "position": Player.Position.FORWARD, "club": "CSKA Moscow", "external_id": "wc26-uzb-khojimat-erkinov"},
    {"shirt_number": 19, "first_name": "Rustam", "last_name": "Yuldoshev", "position": Player.Position.FORWARD, "club": "AGMK", "external_id": "wc26-uzb-rustam-yuldoshev"},
    {"shirt_number": 20, "first_name": "Jasur", "last_name": "Yakhshiboev", "position": Player.Position.FORWARD, "club": "Navbahor", "external_id": "wc26-uzb-jasur-yakhshiboev"},
    {"shirt_number": 21, "first_name": "Sherzod", "last_name": "Azamov", "position": Player.Position.FORWARD, "club": "Sogdiana", "external_id": "wc26-uzb-sherzod-azamov"},
    {"shirt_number": 22, "first_name": "Farrukh", "last_name": "Sayfiyev", "position": Player.Position.FORWARD, "club": "Pakhtakor", "external_id": "wc26-uzb-farrukh-sayfiyev"},
    {"shirt_number": 24, "first_name": "Jahongir", "last_name": "Aliev", "position": Player.Position.FORWARD, "club": "Lokomotiv Tashkent", "external_id": "wc26-uzb-jahongir-aliev"},
    {"shirt_number": 25, "first_name": "Temur", "last_name": "Khojayev", "position": Player.Position.FORWARD, "club": "Metallurg Bekabad", "external_id": "wc26-uzb-temur-khojayev"},
    {"shirt_number": 26, "first_name": "Sherzod", "last_name": "Husanov", "position": Player.Position.FORWARD, "club": "Nasaf", "external_id": "wc26-uzb-sherzod-husanov"},
]


COLOMBIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Camilo", "last_name": "Vargas", "position": Player.Position.GOALKEEPER, "club": "Atlas", "external_id": "wc26-col-camilo-vargas"},
    {"shirt_number": 12, "first_name": "Alvaro", "last_name": "Montero", "position": Player.Position.GOALKEEPER, "club": "Millonarios", "external_id": "wc26-col-alvaro-montero"},
    {"shirt_number": 23, "first_name": "Kevin", "last_name": "Mier", "position": Player.Position.GOALKEEPER, "club": "Cruz Azul", "external_id": "wc26-col-kevin-mier"},

    {"shirt_number": 2, "first_name": "Santiago", "last_name": "Arias", "position": Player.Position.DEFENDER, "club": "Cincinnati", "external_id": "wc26-col-santiago-arias"},
    {"shirt_number": 3, "first_name": "Yerry", "last_name": "Mina", "position": Player.Position.DEFENDER, "club": "Cagliari", "external_id": "wc26-col-yerry-mina"},
    {"shirt_number": 4, "first_name": "Carlos", "last_name": "Cuesta", "position": Player.Position.DEFENDER, "club": "Genk", "external_id": "wc26-col-carlos-cuesta"},
    {"shirt_number": 5, "first_name": "Davinson", "last_name": "Sanchez", "position": Player.Position.DEFENDER, "club": "Galatasaray", "external_id": "wc26-col-davinson-sanchez"},
    {"shirt_number": 13, "first_name": "Daniel", "last_name": "Munoz", "position": Player.Position.DEFENDER, "club": "Crystal Palace", "external_id": "wc26-col-daniel-munoz"},
    {"shirt_number": 14, "first_name": "Johan", "last_name": "Mojica", "position": Player.Position.DEFENDER, "club": "Villarreal", "external_id": "wc26-col-johan-mojica"},
    {"shirt_number": 15, "first_name": "Deiver", "last_name": "Machado", "position": Player.Position.DEFENDER, "club": "Lens", "external_id": "wc26-col-deiver-machado"},

    {"shirt_number": 6, "first_name": "Jefferson", "last_name": "Lerma", "position": Player.Position.MIDFIELDER, "club": "Crystal Palace", "external_id": "wc26-col-jefferson-lerma"},
    {"shirt_number": 8, "first_name": "Mateus", "last_name": "Uribe", "position": Player.Position.MIDFIELDER, "club": "Al Sadd", "external_id": "wc26-col-mateus-uribe"},
    {"shirt_number": 10, "first_name": "James", "last_name": "Rodriguez", "position": Player.Position.MIDFIELDER, "club": "Sao Paulo", "external_id": "wc26-col-james-rodriguez"},
    {"shirt_number": 16, "first_name": "Jhon", "last_name": "Arias", "position": Player.Position.MIDFIELDER, "club": "Fluminense", "external_id": "wc26-col-jhon-arias"},
    {"shirt_number": 17, "first_name": "Luis", "last_name": "Sinisterra", "position": Player.Position.MIDFIELDER, "club": "Bournemouth", "external_id": "wc26-col-luis-sinisterra"},
    {"shirt_number": 18, "first_name": "Yaser", "last_name": "Asprilla", "position": Player.Position.MIDFIELDER, "club": "Watford", "external_id": "wc26-col-yaser-asprilla"},

    {"shirt_number": 7, "first_name": "Luis", "last_name": "Diaz", "position": Player.Position.FORWARD, "club": "Liverpool", "external_id": "wc26-col-luis-diaz"},
    {"shirt_number": 9, "first_name": "Rafael", "last_name": "Borre", "position": Player.Position.FORWARD, "club": "Internacional", "external_id": "wc26-col-rafael-borre"},
    {"shirt_number": 11, "first_name": "Jhon", "last_name": "Cordoba", "position": Player.Position.FORWARD, "club": "Krasnodar", "external_id": "wc26-col-jhon-cordoba"},
    {"shirt_number": 19, "first_name": "Miguel", "last_name": "Borja", "position": Player.Position.FORWARD, "club": "River Plate", "external_id": "wc26-col-miguel-borja"},
    {"shirt_number": 20, "first_name": "Jhon", "last_name": "Duran", "position": Player.Position.FORWARD, "club": "Aston Villa", "external_id": "wc26-col-jhon-duran"},
    {"shirt_number": 21, "first_name": "Roger", "last_name": "Martinez", "position": Player.Position.FORWARD, "club": "Racing Club", "external_id": "wc26-col-roger-martinez"},
    {"shirt_number": 22, "first_name": "Juan", "last_name": "Ferna ndez", "position": Player.Position.FORWARD, "club": "America de Cali", "external_id": "wc26-col-juan-fernandez"},
    {"shirt_number": 24, "first_name": "Diego", "last_name": "Valoyes", "position": Player.Position.FORWARD, "club": "Juarez", "external_id": "wc26-col-diego-valoyes"},
    {"shirt_number": 25, "first_name": "Jorge", "last_name": "Carrascal", "position": Player.Position.FORWARD, "club": "Dinamo Moscow", "external_id": "wc26-col-jorge-carrascal"},
    {"shirt_number": 26, "first_name": "Luis", "last_name": "Sandro", "position": Player.Position.FORWARD, "club": "Atletico Nacional", "external_id": "wc26-col-luis-sandro"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo K del Mundial 2026"

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
            portugal = Team.objects.get(fifa_code="POR")
            dr_congo = Team.objects.get(fifa_code="COD")
            uzbekistan = Team.objects.get(fifa_code="UZB")
            colombia = Team.objects.get(fifa_code="COL")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo K en la base de datos: {exc}")

        results = []

        results.append(("Portugal", *self.load_players_for_team(portugal, PORTUGAL_PLAYERS)))
        results.append(("DR Congo", *self.load_players_for_team(dr_congo, DR_CONGO_PLAYERS)))
        results.append(("Uzbekistan", *self.load_players_for_team(uzbekistan, UZBEKISTAN_PLAYERS)))
        results.append(("Colombia", *self.load_players_for_team(colombia, COLOMBIA_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo K completada."))