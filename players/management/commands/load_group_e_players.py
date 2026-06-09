from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


GERMANY_PLAYERS = [
    {"shirt_number": 1, "first_name": "Manuel", "last_name": "Neuer", "position": Player.Position.GOALKEEPER, "club": "Bayern Munich", "external_id": "wc26-ger-manuel-neuer"},
    {"shirt_number": 12, "first_name": "Marc-Andre", "last_name": "ter Stegen", "position": Player.Position.GOALKEEPER, "club": "Barcelona", "external_id": "wc26-ger-marc-andre-ter-stegen"},
    {"shirt_number": 23, "first_name": "Kevin", "last_name": "Trapp", "position": Player.Position.GOALKEEPER, "club": "Eintracht Frankfurt", "external_id": "wc26-ger-kevin-trapp"},

    {"shirt_number": 2, "first_name": "Joshua", "last_name": "Kimmich", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-ger-joshua-kimmich"},
    {"shirt_number": 3, "first_name": "David", "last_name": "Raum", "position": Player.Position.DEFENDER, "club": "RB Leipzig", "external_id": "wc26-ger-david-raum"},
    {"shirt_number": 4, "first_name": "Antonio", "last_name": "Rudiger", "position": Player.Position.DEFENDER, "club": "Real Madrid", "external_id": "wc26-ger-antonio-rudiger"},
    {"shirt_number": 5, "first_name": "Jonathan", "last_name": "Tah", "position": Player.Position.DEFENDER, "club": "Bayer Leverkusen", "external_id": "wc26-ger-jonathan-tah"},
    {"shirt_number": 13, "first_name": "Nico", "last_name": "Schlotterbeck", "position": Player.Position.DEFENDER, "club": "Borussia Dortmund", "external_id": "wc26-ger-nico-schlotterbeck"},
    {"shirt_number": 14, "first_name": "Robin", "last_name": "Gosens", "position": Player.Position.DEFENDER, "club": "Union Berlin", "external_id": "wc26-ger-robin-gosens"},
    {"shirt_number": 15, "first_name": "Benjamin", "last_name": "Henrichs", "position": Player.Position.DEFENDER, "club": "RB Leipzig", "external_id": "wc26-ger-benjamin-henrichs"},

    {"shirt_number": 6, "first_name": "Ilkay", "last_name": "Gundogan", "position": Player.Position.MIDFIELDER, "club": "Barcelona", "external_id": "wc26-ger-ilkay-gundogan"},
    {"shirt_number": 8, "first_name": "Leon", "last_name": "Goretzka", "position": Player.Position.MIDFIELDER, "club": "Bayern Munich", "external_id": "wc26-ger-leon-goretzka"},
    {"shirt_number": 10, "first_name": "Jamal", "last_name": "Musiala", "position": Player.Position.MIDFIELDER, "club": "Bayern Munich", "external_id": "wc26-ger-jamal-musiala"},
    {"shirt_number": 16, "first_name": "Florian", "last_name": "Wirtz", "position": Player.Position.MIDFIELDER, "club": "Bayer Leverkusen", "external_id": "wc26-ger-florian-wirtz"},
    {"shirt_number": 18, "first_name": "Kai", "last_name": "Havertz", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-ger-kai-havertz"},

    {"shirt_number": 7, "first_name": "Serge", "last_name": "Gnabry", "position": Player.Position.FORWARD, "club": "Bayern Munich", "external_id": "wc26-ger-serge-gnabry"},
    {"shirt_number": 9, "first_name": "Niclas", "last_name": "Fullkrug", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-ger-niclas-fullkrug"},
    {"shirt_number": 11, "first_name": "Leroy", "last_name": "Sane", "position": Player.Position.FORWARD, "club": "Bayern Munich", "external_id": "wc26-ger-leroy-sane"},
    {"shirt_number": 19, "first_name": "Thomas", "last_name": "Muller", "position": Player.Position.FORWARD, "club": "Bayern Munich", "external_id": "wc26-ger-thomas-muller"},
    {"shirt_number": 20, "first_name": "Julian", "last_name": "Brandt", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-ger-julian-brandt"},
    {"shirt_number": 21, "first_name": "Karim", "last_name": "Adeyemi", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-ger-karim-adeyemi"},
    {"shirt_number": 22, "first_name": "Youssoufa", "last_name": "Moukoko", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-ger-youssoufa-moukoko"},
    {"shirt_number": 24, "first_name": "Timo", "last_name": "Werner", "position": Player.Position.FORWARD, "club": "Tottenham Hotspur", "external_id": "wc26-ger-timo-werner"},
    {"shirt_number": 25, "first_name": "Kevin", "last_name": "Schade", "position": Player.Position.FORWARD, "club": "Brentford", "external_id": "wc26-ger-kevin-schade"},
    {"shirt_number": 26, "first_name": "Malik", "last_name": "Thiaw", "position": Player.Position.FORWARD, "club": "Milan", "external_id": "wc26-ger-malik-thiaw"},
]


CURACAO_PLAYERS = [
    {"shirt_number": 1, "first_name": "Eloy", "last_name": "Room", "position": Player.Position.GOALKEEPER, "club": "Columbus Crew", "external_id": "wc26-cuw-eloy-room"},
    {"shirt_number": 12, "first_name": "Jurick", "last_name": "Rohieta", "position": Player.Position.GOALKEEPER, "club": "RKC Waalwijk", "external_id": "wc26-cuw-jurick-rohieta"},
    {"shirt_number": 23, "first_name": "Trevor", "last_name": "Doornbusch", "position": Player.Position.GOALKEEPER, "club": "FC Emmen", "external_id": "wc26-cuw-trevor-doornbusch"},

    {"shirt_number": 2, "first_name": "Cuco", "last_name": "Martina", "position": Player.Position.DEFENDER, "club": "NAC Breda", "external_id": "wc26-cuw-cuco-martina"},
    {"shirt_number": 3, "first_name": "Vurnon", "last_name": "Anita", "position": Player.Position.DEFENDER, "club": "RKC Waalwijk", "external_id": "wc26-cuw-vurnon-anita"},
    {"shirt_number": 4, "first_name": "Rangelo", "last_name": "Janga", "position": Player.Position.DEFENDER, "club": "Apollon Limassol", "external_id": "wc26-cuw-rangelo-janga"},
    {"shirt_number": 5, "first_name": "Jurien", "last_name": "Gaari", "position": Player.Position.DEFENDER, "club": "RKC Waalwijk", "external_id": "wc26-cuw-jurien-gaari"},
    {"shirt_number": 13, "first_name": "Shermar", "last_name": "Garcia", "position": Player.Position.DEFENDER, "club": "CSKA Sofia", "external_id": "wc26-cuw-shermar-garcia"},
    {"shirt_number": 14, "first_name": "Leandro", "last_name": "Bacuna", "position": Player.Position.DEFENDER, "club": "Watford", "external_id": "wc26-cuw-leandro-bacuna"},
    {"shirt_number": 15, "first_name": "Xavier", "last_name": "Mous", "position": Player.Position.DEFENDER, "club": "PEC Zwolle", "external_id": "wc26-cuw-xavier-mous"},

    {"shirt_number": 6, "first_name": "Juninho", "last_name": "Bacuna", "position": Player.Position.MIDFIELDER, "club": "Birmingham City", "external_id": "wc26-cuw-juninho-bacuna"},
    {"shirt_number": 8, "first_name": "Brandley", "last_name": "Kuwas", "position": Player.Position.MIDFIELDER, "club": "GZ Evergrande", "external_id": "wc26-cuw-brandley-kuwas"},
    {"shirt_number": 10, "first_name": "Richelor", "last_name": "Sprangers", "position": Player.Position.MIDFIELDER, "club": "Helmond Sport", "external_id": "wc26-cuw-richelor-sprangers"},
    {"shirt_number": 16, "first_name": "Luivien", "last_name": "Lumanza", "position": Player.Position.MIDFIELDER, "club": "Stabaek", "external_id": "wc26-cuw-luivien-lumanza"},
    {"shirt_number": 17, "first_name": "Elson", "last_name": "Hooi", "position": Player.Position.MIDFIELDER, "club": "AEL Limassol", "external_id": "wc26-cuw-elson-hooi"},
    {"shirt_number": 18, "first_name": "Jeremy", "last_name": "de Nooijer", "position": Player.Position.MIDFIELDER, "club": "NAC Breda", "external_id": "wc26-cuw-jeremy-de-nooijer"},

    {"shirt_number": 7, "first_name": "Shanon", "last_name": "Ruiz", "position": Player.Position.FORWARD, "club": "Sparta Rotterdam", "external_id": "wc26-cuw-shanon-ruiz"},
    {"shirt_number": 9, "first_name": "Jarchinio", "last_name": "Antonia", "position": Player.Position.FORWARD, "club": "PAE Veria", "external_id": "wc26-cuw-jarchinio-antonia"},
    {"shirt_number": 11, "first_name": "Guyon", "last_name": "Fernandes", "position": Player.Position.FORWARD, "club": "ADO Den Haag", "external_id": "wc26-cuw-guyon-fernandes"},
    {"shirt_number": 19, "first_name": "Roshon", "last_name": "van Eijma", "position": Player.Position.FORWARD, "club": "FC Eindhoven", "external_id": "wc26-cuw-roshon-van-eijma"},
    {"shirt_number": 20, "first_name": "Gervane", "last_name": "Kastaneer", "position": Player.Position.FORWARD, "club": "Coventry City", "external_id": "wc26-cuw-gervane-kastaneer"},
    {"shirt_number": 21, "first_name": "Charlison", "last_name": "Benschop", "position": Player.Position.FORWARD, "club": "Apollon Limassol", "external_id": "wc26-cuw-charlison-benschop"},
    {"shirt_number": 22, "first_name": "Quincy", "last_name": "Hoesen", "position": Player.Position.FORWARD, "club": "FC Emmen", "external_id": "wc26-cuw-quincy-hoesen"},
    {"shirt_number": 24, "first_name": "Jairinho", "last_name": "Rozenstruik", "position": Player.Position.FORWARD, "club": "Dordrecht", "external_id": "wc26-cuw-jairinho-rozenstruik"},
    {"shirt_number": 25, "first_name": "Ashwin", "last_name": "Juliana", "position": Player.Position.FORWARD, "club": "NAC Breda", "external_id": "wc26-cuw-ashwin-juliana"},
    {"shirt_number": 26, "first_name": "Rangelo", "last_name": "Janga Jr", "position": Player.Position.FORWARD, "club": "Apollon Limassol", "external_id": "wc26-cuw-rangelo-janga-jr"},
]


IVORY_COAST_PLAYERS = [
    {"shirt_number": 1, "first_name": "Yahia", "last_name": "Fofana", "position": Player.Position.GOALKEEPER, "club": "Angers", "external_id": "wc26-civ-yahia-fofana"},
    {"shirt_number": 12, "first_name": "Badra", "last_name": "Ali Sangare", "position": Player.Position.GOALKEEPER, "club": "JDR Stars", "external_id": "wc26-civ-badra-sangare"},
    {"shirt_number": 23, "first_name": "Charles", "last_name": "Folley", "position": Player.Position.GOALKEEPER, "club": "ASEC Mimosas", "external_id": "wc26-civ-charles-folley"},

    {"shirt_number": 2, "first_name": "Serge", "last_name": "Aurier", "position": Player.Position.DEFENDER, "club": "Galatasaray", "external_id": "wc26-civ-serge-aurier"},
    {"shirt_number": 3, "first_name": "Odilon", "last_name": "Kossounou", "position": Player.Position.DEFENDER, "club": "Bayer Leverkusen", "external_id": "wc26-civ-odilon-kossounou"},
    {"shirt_number": 4, "first_name": "Eric Bailly", "last_name": "", "position": Player.Position.DEFENDER, "club": "Besiktas", "external_id": "wc26-civ-eric-bailly"},
    {"shirt_number": 5, "first_name": "Willy", "last_name": "Boly", "position": Player.Position.DEFENDER, "club": "Nottingham Forest", "external_id": "wc26-civ-willy-boly"},
    {"shirt_number": 13, "first_name": "Ghislain", "last_name": "Konan", "position": Player.Position.DEFENDER, "club": "Al Nassr", "external_id": "wc26-civ-ghislain-konan"},
    {"shirt_number": 14, "first_name": "Ousmane", "last_name": "Diomande", "position": Player.Position.DEFENDER, "club": "Sporting CP", "external_id": "wc26-civ-ousmane-diomande"},
    {"shirt_number": 15, "first_name": "Simon", "last_name": "Deli", "position": Player.Position.DEFENDER, "club": "Adana Demirspor", "external_id": "wc26-civ-simon-deli"},

    {"shirt_number": 6, "first_name": "Ibrahim", "last_name": "Sangare", "position": Player.Position.MIDFIELDER, "club": "Nottingham Forest", "external_id": "wc26-civ-ibrahim-sangare"},
    {"shirt_number": 8, "first_name": "Jean-Michael", "last_name": "Seri", "position": Player.Position.MIDFIELDER, "club": "Hull City", "external_id": "wc26-civ-jean-michael-seri"},
    {"shirt_number": 10, "first_name": "Franck", "last_name": "Kessie", "position": Player.Position.MIDFIELDER, "club": "Al Ahli", "external_id": "wc26-civ-franck-kessie"},
    {"shirt_number": 16, "first_name": "Hamed", "last_name": "Traore", "position": Player.Position.MIDFIELDER, "club": "Napoli", "external_id": "wc26-civ-hamed-traore"},
    {"shirt_number": 17, "first_name": "Seko", "last_name": "Fofana", "position": Player.Position.MIDFIELDER, "club": "Al Nassr", "external_id": "wc26-civ-seko-fofana"},
    {"shirt_number": 18, "first_name": "Jean", "last_name": "Onana", "position": Player.Position.MIDFIELDER, "club": "Besiktas", "external_id": "wc26-civ-jean-onana"},

    {"shirt_number": 7, "first_name": "Jeremie", "last_name": "Boga", "position": Player.Position.FORWARD, "club": "Nice", "external_id": "wc26-civ-jeremie-boga"},
    {"shirt_number": 9, "first_name": "Sebastien", "last_name": "Haller", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-civ-sebastien-haller"},
    {"shirt_number": 11, "first_name": "Nicolas", "last_name": "Pepe", "position": Player.Position.FORWARD, "club": "Trabzonspor", "external_id": "wc26-civ-nicolas-pepe"},
    {"shirt_number": 19, "first_name": "Max-Alain", "last_name": "Gradel", "position": Player.Position.FORWARD, "club": "Gaziantep", "external_id": "wc26-civ-max-alain-gradel"},
    {"shirt_number": 20, "first_name": "Wilfried", "last_name": "Zaha", "position": Player.Position.FORWARD, "club": "Galatasaray", "external_id": "wc26-civ-wilfried-zaha"},
    {"shirt_number": 21, "first_name": "Amad", "last_name": "Diallo", "position": Player.Position.FORWARD, "club": "Manchester United", "external_id": "wc26-civ-amad-diallo"},
    {"shirt_number": 22, "first_name": "Christian", "last_name": "Kouame", "position": Player.Position.FORWARD, "club": "Fiorentina", "external_id": "wc26-civ-christian-kouame"},
    {"shirt_number": 24, "first_name": "Karim", "last_name": "Konate", "position": Player.Position.FORWARD, "club": "RB Salzburg", "external_id": "wc26-civ-karim-konate"},
    {"shirt_number": 25, "first_name": "Simon", "last_name": "Adingra", "position": Player.Position.FORWARD, "club": "Brighton", "external_id": "wc26-civ-simon-adingra"},
    {"shirt_number": 26, "first_name": "Jonathan", "last_name": "Kodjia", "position": Player.Position.FORWARD, "club": "Al Gharafa", "external_id": "wc26-civ-jonathan-kodjia"},
]


ECUADOR_PLAYERS = [
    {"shirt_number": 1, "first_name": "Hernan", "last_name": "Galindez", "position": Player.Position.GOALKEEPER, "club": "Aucas", "external_id": "wc26-ecu-hernan-galindez"},
    {"shirt_number": 12, "first_name": "Alexander", "last_name": "Dominguez", "position": Player.Position.GOALKEEPER, "club": "Liga de Quito", "external_id": "wc26-ecu-alexander-dominguez"},
    {"shirt_number": 23, "first_name": "Moises", "last_name": "Ramirez", "position": Player.Position.GOALKEEPER, "club": "Independiente del Valle", "external_id": "wc26-ecu-moises-ramirez"},

    {"shirt_number": 2, "first_name": "Angelo", "last_name": "Preciado", "position": Player.Position.DEFENDER, "club": "Sparta Prague", "external_id": "wc26-ecu-angelo-preciado"},
    {"shirt_number": 3, "first_name": "Piero", "last_name": "Hincapie", "position": Player.Position.DEFENDER, "club": "Bayer Leverkusen", "external_id": "wc26-ecu-piero-hincapie"},
    {"shirt_number": 4, "first_name": "Felix", "last_name": "Torres", "position": Player.Position.DEFENDER, "club": "Corinthians", "external_id": "wc26-ecu-felix-torres"},
    {"shirt_number": 5, "first_name": "William", "last_name": "Pacho", "position": Player.Position.DEFENDER, "club": "Eintracht Frankfurt", "external_id": "wc26-ecu-william-pacho"},
    {"shirt_number": 13, "first_name": "Diego", "last_name": "Palacios", "position": Player.Position.DEFENDER, "club": "LAFC", "external_id": "wc26-ecu-diego-palacios"},
    {"shirt_number": 14, "first_name": "Jackson", "last_name": "Porozo", "position": Player.Position.DEFENDER, "club": "Troyes", "external_id": "wc26-ecu-jackson-porozo"},
    {"shirt_number": 15, "first_name": "Jose", "last_name": "Hurtado", "position": Player.Position.DEFENDER, "club": "Red Bull Bragantino", "external_id": "wc26-ecu-jose-hurtado"},

    {"shirt_number": 6, "first_name": "Carlos", "last_name": "Gruezo", "position": Player.Position.MIDFIELDER, "club": "San Jose Earthquakes", "external_id": "wc26-ecu-carlos-gruezo"},
    {"shirt_number": 8, "first_name": "Moisés", "last_name": "Caicedo", "position": Player.Position.MIDFIELDER, "club": "Chelsea", "external_id": "wc26-ecu-moises-caicedo"},
    {"shirt_number": 10, "first_name": "Angel", "last_name": "Mena", "position": Player.Position.MIDFIELDER, "club": "Leon", "external_id": "wc26-ecu-angel-mena"},
    {"shirt_number": 16, "first_name": "Jose", "last_name": "Cifuentes", "position": Player.Position.MIDFIELDER, "club": "Rangers", "external_id": "wc26-ecu-jose-cifuentes"},
    {"shirt_number": 17, "first_name": "Alan", "last_name": "Franco", "position": Player.Position.MIDFIELDER, "club": "Talleres", "external_id": "wc26-ecu-alan-franco"},
    {"shirt_number": 18, "first_name": "Joao", "last_name": "Rojas", "position": Player.Position.MIDFIELDER, "club": "Monterrey", "external_id": "wc26-ecu-joao-rojas"},

    {"shirt_number": 7, "first_name": "Gonzalo", "last_name": "Plata", "position": Player.Position.FORWARD, "club": "Al Sadd", "external_id": "wc26-ecu-gonzalo-plata"},
    {"shirt_number": 9, "first_name": "Enner", "last_name": "Valencia", "position": Player.Position.FORWARD, "club": "Internacional", "external_id": "wc26-ecu-enner-valencia"},
    {"shirt_number": 11, "first_name": "Michael", "last_name": "Estrada", "position": Player.Position.FORWARD, "club": "Cruz Azul", "external_id": "wc26-ecu-michael-estrada"},
    {"shirt_number": 19, "first_name": "Kevin", "last_name": "Rodriguez", "position": Player.Position.FORWARD, "club": "Union SG", "external_id": "wc26-ecu-kevin-rodriguez"},
    {"shirt_number": 20, "first_name": "Leonardo", "last_name": "Campana", "position": Player.Position.FORWARD, "club": "Inter Miami", "external_id": "wc26-ecu-leonardo-campana"},
    {"shirt_number": 21, "first_name": "Jordy", "last_name": "Caicedo", "position": Player.Position.FORWARD, "club": "Atlas", "external_id": "wc26-ecu-jordy-caicedo"},
    {"shirt_number": 22, "first_name": "Romario", "last_name": "Ibarra", "position": Player.Position.FORWARD, "club": "Independiente del Valle", "external_id": "wc26-ecu-romario-ibarra"},
    {"shirt_number": 24, "first_name": "Jeremy", "last_name": "Sarmiento", "position": Player.Position.FORWARD, "club": "Ipswich Town", "external_id": "wc26-ecu-jeremy-sarmiento"},
    {"shirt_number": 25, "first_name": "Kevin", "last_name": "Arroyo", "position": Player.Position.FORWARD, "club": "Emelec", "external_id": "wc26-ecu-kevin-arroyo"},
    {"shirt_number": 26, "first_name": "Jannner", "last_name": "Corrales", "position": Player.Position.FORWARD, "club": "LDU Quito", "external_id": "wc26-ecu-janner-corrales"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo E del Mundial 2026"

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
            germany = Team.objects.get(fifa_code="GER")
            curacao = Team.objects.get(fifa_code="CUW")
            ivory_coast = Team.objects.get(fifa_code="CIV")
            ecuador = Team.objects.get(fifa_code="ECU")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo E en la base de datos: {exc}")

        results = []

        results.append(("Germany", *self.load_players_for_team(germany, GERMANY_PLAYERS)))
        results.append(("Curacao", *self.load_players_for_team(curacao, CURACAO_PLAYERS)))
        results.append(("Ivory Coast", *self.load_players_for_team(ivory_coast, IVORY_COAST_PLAYERS)))
        results.append(("Ecuador", *self.load_players_for_team(ecuador, ECUADOR_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo E completada."))