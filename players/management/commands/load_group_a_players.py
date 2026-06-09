from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


MEXICO_PLAYERS = [
    {"shirt_number": 1, "first_name": "Raul", "last_name": "Rangel", "position": Player.Position.GOALKEEPER, "club": "Guadalajara", "external_id": "wc26-mex-raul-rangel"},
    {"shirt_number": 12, "first_name": "Carlos", "last_name": "Acevedo", "position": Player.Position.GOALKEEPER, "club": "Santos Laguna", "external_id": "wc26-mex-carlos-acevedo"},
    {"shirt_number": 23, "first_name": "Guillermo", "last_name": "Ochoa", "position": Player.Position.GOALKEEPER, "club": "AEL Limassol", "external_id": "wc26-mex-guillermo-ochoa"},

    {"shirt_number": 2, "first_name": "Jorge", "last_name": "Sanchez", "position": Player.Position.DEFENDER, "club": "PAOK", "external_id": "wc26-mex-jorge-sanchez"},
    {"shirt_number": 3, "first_name": "Cesar", "last_name": "Montes", "position": Player.Position.DEFENDER, "club": "Lokomotiv Moscow", "external_id": "wc26-mex-cesar-montes"},
    {"shirt_number": 4, "first_name": "Edson", "last_name": "Alvarez", "position": Player.Position.DEFENDER, "club": "Fenerbahce", "external_id": "wc26-mex-edson-alvarez"},
    {"shirt_number": 5, "first_name": "Johan", "last_name": "Vasquez", "position": Player.Position.DEFENDER, "club": "Genoa", "external_id": "wc26-mex-johan-vasquez"},
    {"shirt_number": 13, "first_name": "Israel", "last_name": "Reyes", "position": Player.Position.DEFENDER, "club": "America", "external_id": "wc26-mex-israel-reyes"},
    {"shirt_number": 14, "first_name": "Mateo", "last_name": "Chavez", "position": Player.Position.DEFENDER, "club": "AZ Alkmaar", "external_id": "wc26-mex-mateo-chavez"},
    {"shirt_number": 15, "first_name": "Jesus", "last_name": "Gallardo", "position": Player.Position.DEFENDER, "club": "Toluca", "external_id": "wc26-mex-jesus-gallardo"},

    {"shirt_number": 6, "first_name": "Erik", "last_name": "Lira", "position": Player.Position.MIDFIELDER, "club": "Cruz Azul", "external_id": "wc26-mex-erik-lira"},
    {"shirt_number": 8, "first_name": "Luis", "last_name": "Romo", "position": Player.Position.MIDFIELDER, "club": "Guadalajara", "external_id": "wc26-mex-luis-romo"},
    {"shirt_number": 10, "first_name": "Alvaro", "last_name": "Fidalgo", "position": Player.Position.MIDFIELDER, "club": "Real Betis", "external_id": "wc26-mex-alvaro-fidalgo"},
    {"shirt_number": 16, "first_name": "Orbelin", "last_name": "Pineda", "position": Player.Position.MIDFIELDER, "club": "AEK Athens", "external_id": "wc26-mex-orbelin-pineda"},
    {"shirt_number": 18, "first_name": "Obed", "last_name": "Vargas", "position": Player.Position.MIDFIELDER, "club": "Atletico Madrid", "external_id": "wc26-mex-obed-vargas"},
    {"shirt_number": 20, "first_name": "Gilberto", "last_name": "Mora", "position": Player.Position.MIDFIELDER, "club": "Tijuana", "external_id": "wc26-mex-gilberto-mora"},
    {"shirt_number": 21, "first_name": "Luis", "last_name": "Chavez", "position": Player.Position.MIDFIELDER, "club": "Dynamo Moscow", "external_id": "wc26-mex-luis-chavez"},
    {"shirt_number": 24, "first_name": "Brian", "last_name": "Gutierrez", "position": Player.Position.MIDFIELDER, "club": "Guadalajara", "external_id": "wc26-mex-brian-gutierrez"},

    {"shirt_number": 7, "first_name": "Raul", "last_name": "Jimenez", "position": Player.Position.FORWARD, "club": "Fulham", "external_id": "wc26-mex-raul-jimenez"},
    {"shirt_number": 9, "first_name": "Alexis", "last_name": "Vega", "position": Player.Position.FORWARD, "club": "Toluca", "external_id": "wc26-mex-alexis-vega"},
    {"shirt_number": 11, "first_name": "Santiago", "last_name": "Gimenez", "position": Player.Position.FORWARD, "club": "AC Milan", "external_id": "wc26-mex-santiago-gimenez"},
    {"shirt_number": 17, "first_name": "Armando", "last_name": "Gonzalez", "position": Player.Position.FORWARD, "club": "Guadalajara", "external_id": "wc26-mex-armando-gonzalez"},
    {"shirt_number": 19, "first_name": "Julian", "last_name": "Quinones", "position": Player.Position.FORWARD, "club": "Al Qadsiah", "external_id": "wc26-mex-julian-quinones"},
    {"shirt_number": 22, "first_name": "Cesar", "last_name": "Huerta", "position": Player.Position.FORWARD, "club": "Anderlecht", "external_id": "wc26-mex-cesar-huerta"},
    {"shirt_number": 25, "first_name": "Guillermo", "last_name": "Martinez", "position": Player.Position.FORWARD, "club": "Pumas", "external_id": "wc26-mex-guillermo-martinez"},
    {"shirt_number": 26, "first_name": "Roberto", "last_name": "Alvarado", "position": Player.Position.FORWARD, "club": "Guadalajara", "external_id": "wc26-mex-roberto-alvarado"},
]


SOUTH_AFRICA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Ronwen", "last_name": "Williams", "position": Player.Position.GOALKEEPER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-ronwen-williams"},
    {"shirt_number": 12, "first_name": "Sipho", "last_name": "Chaine", "position": Player.Position.GOALKEEPER, "club": "Orlando Pirates", "external_id": "wc26-rsa-sipho-chaine"},
    {"shirt_number": 23, "first_name": "Ricardo", "last_name": "Goss", "position": Player.Position.GOALKEEPER, "club": "Siwelele", "external_id": "wc26-rsa-ricardo-goss"},

    {"shirt_number": 2, "first_name": "Thabang", "last_name": "Matuludi", "position": Player.Position.DEFENDER, "club": "Polokwane City", "external_id": "wc26-rsa-thabang-matuludi"},
    {"shirt_number": 3, "first_name": "Khulumani", "last_name": "Ndamane", "position": Player.Position.DEFENDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-khulumani-ndamane"},
    {"shirt_number": 4, "first_name": "Aubrey", "last_name": "Modiba", "position": Player.Position.DEFENDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-aubrey-modiba"},
    {"shirt_number": 5, "first_name": "Mbekezeli", "last_name": "Mbokazi", "position": Player.Position.DEFENDER, "club": "Chicago Fire", "external_id": "wc26-rsa-mbekezeli-mbokazi"},
    {"shirt_number": 13, "first_name": "Samukele", "last_name": "Kabini", "position": Player.Position.DEFENDER, "club": "Molde", "external_id": "wc26-rsa-samukele-kabini"},
    {"shirt_number": 14, "first_name": "Nkosinathi", "last_name": "Sibisi", "position": Player.Position.DEFENDER, "club": "Orlando Pirates", "external_id": "wc26-rsa-nkosinathi-sibisi"},
    {"shirt_number": 15, "first_name": "Khuliso", "last_name": "Mudau", "position": Player.Position.DEFENDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-khuliso-mudau"},
    {"shirt_number": 16, "first_name": "Ime", "last_name": "Okon", "position": Player.Position.DEFENDER, "club": "Hannover 96", "external_id": "wc26-rsa-ime-okon"},
    {"shirt_number": 24, "first_name": "Olwethu", "last_name": "Makhanya", "position": Player.Position.DEFENDER, "club": "Philadelphia Union", "external_id": "wc26-rsa-olwethu-makhanya"},
    {"shirt_number": 25, "first_name": "Bradley", "last_name": "Cross", "position": Player.Position.DEFENDER, "club": "Kaizer Chiefs", "external_id": "wc26-rsa-bradley-cross"},

    {"shirt_number": 6, "first_name": "Teboho", "last_name": "Mokoena", "position": Player.Position.MIDFIELDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-teboho-mokoena"},
    {"shirt_number": 8, "first_name": "Thalente", "last_name": "Mbatha", "position": Player.Position.MIDFIELDER, "club": "Orlando Pirates", "external_id": "wc26-rsa-thalente-mbatha"},
    {"shirt_number": 10, "first_name": "Themba", "last_name": "Zwane", "position": Player.Position.MIDFIELDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-themba-zwane"},
    {"shirt_number": 17, "first_name": "Sphephelo", "last_name": "Sithole", "position": Player.Position.MIDFIELDER, "club": "Tondela", "external_id": "wc26-rsa-sphephelo-sithole"},
    {"shirt_number": 20, "first_name": "Jayden", "last_name": "Adams", "position": Player.Position.MIDFIELDER, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-jayden-adams"},

    {"shirt_number": 7, "first_name": "Oswin", "last_name": "Appollis", "position": Player.Position.FORWARD, "club": "Orlando Pirates", "external_id": "wc26-rsa-oswin-appollis"},
    {"shirt_number": 9, "first_name": "Tshepang", "last_name": "Moremi", "position": Player.Position.FORWARD, "club": "Orlando Pirates", "external_id": "wc26-rsa-tshepang-moremi"},
    {"shirt_number": 11, "first_name": "Lyle", "last_name": "Foster", "position": Player.Position.FORWARD, "club": "Burnley", "external_id": "wc26-rsa-lyle-foster"},
    {"shirt_number": 18, "first_name": "Relebohile", "last_name": "Mofokeng", "position": Player.Position.FORWARD, "club": "Orlando Pirates", "external_id": "wc26-rsa-relebohile-mofokeng"},
    {"shirt_number": 19, "first_name": "Thapelo", "last_name": "Maseko", "position": Player.Position.FORWARD, "club": "AEL Limassol", "external_id": "wc26-rsa-thapelo-maseko"},
    {"shirt_number": 21, "first_name": "Iqraam", "last_name": "Rayners", "position": Player.Position.FORWARD, "club": "Mamelodi Sundowns", "external_id": "wc26-rsa-iqraam-rayners"},
    {"shirt_number": 22, "first_name": "Evidence", "last_name": "Makgopa", "position": Player.Position.FORWARD, "club": "Orlando Pirates", "external_id": "wc26-rsa-evidence-makgopa"},
    {"shirt_number": 26, "first_name": "Kamogelo", "last_name": "Sebelebele", "position": Player.Position.FORWARD, "club": "Orlando Pirates", "external_id": "wc26-rsa-kamogelo-sebelebele"},
]


KOREA_REPUBLIC_PLAYERS = [
    {"shirt_number": 1, "first_name": "Kim", "last_name": "Seunggyu", "position": Player.Position.GOALKEEPER, "club": "FC Tokyo", "external_id": "wc26-kor-kim-seunggyu"},
    {"shirt_number": 12, "first_name": "Song", "last_name": "Bumkeun", "position": Player.Position.GOALKEEPER, "club": "Jeonbuk Hyundai Motors", "external_id": "wc26-kor-song-bumkeun"},
    {"shirt_number": 23, "first_name": "Jo", "last_name": "Hyeonwoo", "position": Player.Position.GOALKEEPER, "club": "Ulsan HD", "external_id": "wc26-kor-jo-hyeonwoo"},

    {"shirt_number": 2, "first_name": "Lee", "last_name": "Hanbeom", "position": Player.Position.DEFENDER, "club": "Midtjylland", "external_id": "wc26-kor-lee-hanbeom"},
    {"shirt_number": 3, "first_name": "Kim", "last_name": "Minjae", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-kor-kim-minjae"},
    {"shirt_number": 4, "first_name": "Kim", "last_name": "Taehyeon", "position": Player.Position.DEFENDER, "club": "Kashima Antlers", "external_id": "wc26-kor-kim-taehyeon"},
    {"shirt_number": 5, "first_name": "Lee", "last_name": "Taeseok", "position": Player.Position.DEFENDER, "club": "Austria Wien", "external_id": "wc26-kor-lee-taeseok"},
    {"shirt_number": 13, "first_name": "Cho", "last_name": "Wije", "position": Player.Position.DEFENDER, "club": "Jeonbuk Hyundai Motors", "external_id": "wc26-kor-cho-wije"},
    {"shirt_number": 14, "first_name": "Kim", "last_name": "Moonhwan", "position": Player.Position.DEFENDER, "club": "Daejeon Hana Citizen", "external_id": "wc26-kor-kim-moonhwan"},
    {"shirt_number": 15, "first_name": "Park", "last_name": "Jinseob", "position": Player.Position.DEFENDER, "club": "Zhejiang", "external_id": "wc26-kor-park-jinseob"},
    {"shirt_number": 16, "first_name": "Seol", "last_name": "Youngwoo", "position": Player.Position.DEFENDER, "club": "Crvena Zvezda", "external_id": "wc26-kor-seol-youngwoo"},
    {"shirt_number": 24, "first_name": "Jens", "last_name": "Castrop", "position": Player.Position.DEFENDER, "club": "Borussia Monchengladbach", "external_id": "wc26-kor-jens-castrop"},

    {"shirt_number": 6, "first_name": "Lee", "last_name": "Gihyuk", "position": Player.Position.MIDFIELDER, "club": "Gangwon", "external_id": "wc26-kor-lee-gihyuk"},
    {"shirt_number": 8, "first_name": "Hwang", "last_name": "Inbeom", "position": Player.Position.MIDFIELDER, "club": "Feyenoord", "external_id": "wc26-kor-hwang-inbeom"},
    {"shirt_number": 10, "first_name": "Paik", "last_name": "Seungho", "position": Player.Position.MIDFIELDER, "club": "Birmingham City", "external_id": "wc26-kor-paik-seungho"},
    {"shirt_number": 17, "first_name": "Lee", "last_name": "Jaesung", "position": Player.Position.MIDFIELDER, "club": "Mainz 05", "external_id": "wc26-kor-lee-jaesung"},
    {"shirt_number": 18, "first_name": "Bae", "last_name": "Junho", "position": Player.Position.MIDFIELDER, "club": "Stoke City", "external_id": "wc26-kor-bae-junho"},
    {"shirt_number": 19, "first_name": "Lee", "last_name": "Kangin", "position": Player.Position.MIDFIELDER, "club": "Paris Saint-Germain", "external_id": "wc26-kor-lee-kangin"},
    {"shirt_number": 20, "first_name": "Yang", "last_name": "Hyunjun", "position": Player.Position.MIDFIELDER, "club": "Celtic", "external_id": "wc26-kor-yang-hyunjun"},
    {"shirt_number": 21, "first_name": "Kim", "last_name": "Jingyu", "position": Player.Position.MIDFIELDER, "club": "Jeonbuk Hyundai Motors", "external_id": "wc26-kor-kim-jingyu"},
    {"shirt_number": 22, "first_name": "Eom", "last_name": "Jisung", "position": Player.Position.MIDFIELDER, "club": "Swansea City", "external_id": "wc26-kor-eom-jisung"},
    {"shirt_number": 25, "first_name": "Lee", "last_name": "Donggyeong", "position": Player.Position.MIDFIELDER, "club": "Ulsan HD", "external_id": "wc26-kor-lee-donggyeong"},

    {"shirt_number": 7, "first_name": "Son", "last_name": "Heungmin", "position": Player.Position.FORWARD, "club": "LAFC", "external_id": "wc26-kor-son-heungmin"},
    {"shirt_number": 9, "first_name": "Cho", "last_name": "Guesung", "position": Player.Position.FORWARD, "club": "Midtjylland", "external_id": "wc26-kor-cho-guesung"},
    {"shirt_number": 11, "first_name": "Hwang", "last_name": "Heechan", "position": Player.Position.FORWARD, "club": "Wolverhampton Wanderers", "external_id": "wc26-kor-hwang-heechan"},
    {"shirt_number": 26, "first_name": "Oh", "last_name": "Hyeongyu", "position": Player.Position.FORWARD, "club": "Besiktas", "external_id": "wc26-kor-oh-hyeongyu"},
]


CZECHIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Matej", "last_name": "Kovar", "position": Player.Position.GOALKEEPER, "club": "PSV", "external_id": "wc26-cze-matej-kovar"},
    {"shirt_number": 12, "first_name": "Jindrich", "last_name": "Stanek", "position": Player.Position.GOALKEEPER, "club": "Slavia Praha", "external_id": "wc26-cze-jindrich-stanek"},
    {"shirt_number": 23, "first_name": "Lukas", "last_name": "Hornicek", "position": Player.Position.GOALKEEPER, "club": "Braga", "external_id": "wc26-cze-lukas-hornicek"},

    {"shirt_number": 2, "first_name": "David", "last_name": "Zima", "position": Player.Position.DEFENDER, "club": "Slavia Praha", "external_id": "wc26-cze-david-zima"},
    {"shirt_number": 3, "first_name": "Tomas", "last_name": "Holes", "position": Player.Position.DEFENDER, "club": "Slavia Praha", "external_id": "wc26-cze-tomas-holes"},
    {"shirt_number": 4, "first_name": "Robin", "last_name": "Hranac", "position": Player.Position.DEFENDER, "club": "Hoffenheim", "external_id": "wc26-cze-robin-hranac"},
    {"shirt_number": 5, "first_name": "Vladimir", "last_name": "Coufal", "position": Player.Position.DEFENDER, "club": "Hoffenheim", "external_id": "wc26-cze-vladimir-coufal"},
    {"shirt_number": 6, "first_name": "Stepan", "last_name": "Chaloupek", "position": Player.Position.DEFENDER, "club": "Slavia Praha", "external_id": "wc26-cze-stepan-chaloupek"},
    {"shirt_number": 13, "first_name": "Ladislav", "last_name": "Krejci", "position": Player.Position.DEFENDER, "club": "Wolverhampton Wanderers", "external_id": "wc26-cze-ladislav-krejci"},
    {"shirt_number": 14, "first_name": "David", "last_name": "Jurasek", "position": Player.Position.DEFENDER, "club": "Slavia Praha", "external_id": "wc26-cze-david-jurasek"},
    {"shirt_number": 20, "first_name": "Jaroslav", "last_name": "Zeleny", "position": Player.Position.DEFENDER, "club": "Sparta Praha", "external_id": "wc26-cze-jaroslav-zeleny"},
    {"shirt_number": 21, "first_name": "David", "last_name": "Doudera", "position": Player.Position.DEFENDER, "club": "Slavia Praha", "external_id": "wc26-cze-david-doudera"},

    {"shirt_number": 8, "first_name": "Vladimir", "last_name": "Darida", "position": Player.Position.MIDFIELDER, "club": "Hradec Kralove", "external_id": "wc26-cze-vladimir-darida"},
    {"shirt_number": 16, "first_name": "Lukas", "last_name": "Cerv", "position": Player.Position.MIDFIELDER, "club": "Viktoria Plzen", "external_id": "wc26-cze-lukas-cerv"},
    {"shirt_number": 17, "first_name": "Lukas", "last_name": "Provod", "position": Player.Position.MIDFIELDER, "club": "Slavia Praha", "external_id": "wc26-cze-lukas-provod"},
    {"shirt_number": 18, "first_name": "Michal", "last_name": "Sadilek", "position": Player.Position.MIDFIELDER, "club": "Slavia Praha", "external_id": "wc26-cze-michal-sadilek"},
    {"shirt_number": 22, "first_name": "Tomas", "last_name": "Soucek", "position": Player.Position.MIDFIELDER, "club": "West Ham United", "external_id": "wc26-cze-tomas-soucek"},
    {"shirt_number": 24, "first_name": "Alexandr", "last_name": "Sojka", "position": Player.Position.MIDFIELDER, "club": "Viktoria Plzen", "external_id": "wc26-cze-alexandr-sojka"},
    {"shirt_number": 25, "first_name": "Hugo", "last_name": "Sochurek", "position": Player.Position.MIDFIELDER, "club": "Sparta Praha", "external_id": "wc26-cze-hugo-sochurek"},

    {"shirt_number": 7, "first_name": "Adam", "last_name": "Hlozek", "position": Player.Position.FORWARD, "club": "Hoffenheim", "external_id": "wc26-cze-adam-hlozek"},
    {"shirt_number": 9, "first_name": "Patrik", "last_name": "Schick", "position": Player.Position.FORWARD, "club": "Bayer Leverkusen", "external_id": "wc26-cze-patrik-schick"},
    {"shirt_number": 10, "first_name": "Jan", "last_name": "Kuchta", "position": Player.Position.FORWARD, "club": "Sparta Praha", "external_id": "wc26-cze-jan-kuchta"},
    {"shirt_number": 11, "first_name": "Mojmir", "last_name": "Chytil", "position": Player.Position.FORWARD, "club": "Slavia Praha", "external_id": "wc26-cze-mojmir-chytil"},
    {"shirt_number": 15, "first_name": "Pavel", "last_name": "Sulc", "position": Player.Position.FORWARD, "club": "Lyon", "external_id": "wc26-cze-pavel-sulc"},
    {"shirt_number": 19, "first_name": "Tomas", "last_name": "Chory", "position": Player.Position.FORWARD, "club": "Slavia Praha", "external_id": "wc26-cze-tomas-chory"},
    {"shirt_number": 26, "first_name": "Denis", "last_name": "Visinsky", "position": Player.Position.FORWARD, "club": "Viktoria Plzen", "external_id": "wc26-cze-denis-visinsky"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo A del Mundial 2026"

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
            mexico = Team.objects.get(fifa_code="MEX")
            south_africa = Team.objects.get(fifa_code="RSA")
            korea_republic = Team.objects.get(fifa_code="KOR")
            czechia = Team.objects.get(fifa_code="CZE")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo A en la base de datos: {exc}")

        results = []

        results.append(("Mexico", *self.load_players_for_team(mexico, MEXICO_PLAYERS)))
        results.append(("South Africa", *self.load_players_for_team(south_africa, SOUTH_AFRICA_PLAYERS)))
        results.append(("Korea Republic", *self.load_players_for_team(korea_republic, KOREA_REPUBLIC_PLAYERS)))
        results.append(("Czechia", *self.load_players_for_team(czechia, CZECHIA_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo A completada."))