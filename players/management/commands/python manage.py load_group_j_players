from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


ARGENTINA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Emiliano", "last_name": "Martinez", "position": Player.Position.GOALKEEPER, "club": "Aston Villa", "external_id": "wc26-arg-emiliano-martinez"},
    {"shirt_number": 12, "first_name": "Geronimo", "last_name": "Rulli", "position": Player.Position.GOALKEEPER, "club": "Ajax", "external_id": "wc26-arg-geronimo-rulli"},
    {"shirt_number": 23, "first_name": "Franco", "last_name": "Armani", "position": Player.Position.GOALKEEPER, "club": "River Plate", "external_id": "wc26-arg-franco-armani"},

    {"shirt_number": 2, "first_name": "Nahuel", "last_name": "Molina", "position": Player.Position.DEFENDER, "club": "Atletico Madrid", "external_id": "wc26-arg-nahuel-molina"},
    {"shirt_number": 3, "first_name": "Cristian", "last_name": "Romero", "position": Player.Position.DEFENDER, "club": "Tottenham Hotspur", "external_id": "wc26-arg-cristian-romero"},
    {"shirt_number": 4, "first_name": "Nicolas", "last_name": "Otamendi", "position": Player.Position.DEFENDER, "club": "Benfica", "external_id": "wc26-arg-nicolas-otamendi"},
    {"shirt_number": 5, "first_name": "Lisandro", "last_name": "Martinez", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-arg-lisandro-martinez"},
    {"shirt_number": 13, "first_name": "Marcos", "last_name": "Acuña", "position": Player.Position.DEFENDER, "club": "Sevilla", "external_id": "wc26-arg-marcos-acuna"},
    {"shirt_number": 14, "first_name": "Nicolas", "last_name": "Tagliafico", "position": Player.Position.DEFENDER, "club": "Lyon", "external_id": "wc26-arg-nicolas-tagliafico"},
    {"shirt_number": 15, "first_name": "Gonzalo", "last_name": "Montiel", "position": Player.Position.DEFENDER, "club": "Nottingham Forest", "external_id": "wc26-arg-gonzalo-montiel"},

    {"shirt_number": 6, "first_name": "Rodrigo", "last_name": "De Paul", "position": Player.Position.MIDFIELDER, "club": "Atletico Madrid", "external_id": "wc26-arg-rodrigo-de-paul"},
    {"shirt_number": 8, "first_name": "Enzo", "last_name": "Fernandez", "position": Player.Position.MIDFIELDER, "club": "Chelsea", "external_id": "wc26-arg-enzo-fernandez"},
    {"shirt_number": 10, "first_name": "Lionel", "last_name": "Messi", "position": Player.Position.MIDFIELDER, "club": "Inter Miami", "external_id": "wc26-arg-lionel-messi"},
    {"shirt_number": 16, "first_name": "Alexis", "last_name": "Mac Allister", "position": Player.Position.MIDFIELDER, "club": "Liverpool", "external_id": "wc26-arg-alexis-mac-allister"},
    {"shirt_number": 17, "first_name": "Giovani", "last_name": "Lo Celso", "position": Player.Position.MIDFIELDER, "club": "Real Betis", "external_id": "wc26-arg-giovani-lo-celso"},
    {"shirt_number": 18, "first_name": "Leandro", "last_name": "Paredes", "position": Player.Position.MIDFIELDER, "club": "Roma", "external_id": "wc26-arg-leandro-paredes"},

    {"shirt_number": 7, "first_name": "Angel", "last_name": "Di Maria", "position": Player.Position.FORWARD, "club": "Benfica", "external_id": "wc26-arg-angel-di-maria"},
    {"shirt_number": 9, "first_name": "Julian", "last_name": "Alvarez", "position": Player.Position.FORWARD, "club": "Manchester City", "external_id": "wc26-arg-julian-alvarez"},
    {"shirt_number": 11, "first_name": "Angel", "last_name": "Correa", "position": Player.Position.FORWARD, "club": "Atletico Madrid", "external_id": "wc26-arg-angel-correa"},
    {"shirt_number": 19, "first_name": "Lautaro", "last_name": "Martinez", "position": Player.Position.FORWARD, "club": "Inter Milan", "external_id": "wc26-arg-lautaro-martinez"},
    {"shirt_number": 20, "first_name": "Nicolas", "last_name": "Gonzalez", "position": Player.Position.FORWARD, "club": "Fiorentina", "external_id": "wc26-arg-nicolas-gonzalez"},
    {"shirt_number": 21, "first_name": "Paulo", "last_name": "Dybala", "position": Player.Position.FORWARD, "club": "Roma", "external_id": "wc26-arg-paulo-dybala"},
    {"shirt_number": 22, "first_name": "Alejandro", "last_name": "Garnacho", "position": Player.Position.FORWARD, "club": "Manchester United", "external_id": "wc26-arg-alejandro-garnacho"},
    {"shirt_number": 24, "first_name": "Thiago", "last_name": "Almada", "position": Player.Position.FORWARD, "club": "Atlanta United", "external_id": "wc26-arg-thiago-almada"},
    {"shirt_number": 25, "first_name": "Facundo", "last_name": "Buonanotte", "position": Player.Position.FORWARD, "club": "Brighton", "external_id": "wc26-arg-facundo-buonanotte"},
    {"shirt_number": 26, "first_name": "Valentin", "last_name": "Carboni", "position": Player.Position.FORWARD, "club": "Inter Milan", "external_id": "wc26-arg-valentin-carboni"},
]


ALGERIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Rais", "last_name": "Mbolhi", "position": Player.Position.GOALKEEPER, "club": "Al Qadsiah", "external_id": "wc26-alg-rais-mbolhi"},
    {"shirt_number": 12, "first_name": "Mustapha", "last_name": "Zagba", "position": Player.Position.GOALKEEPER, "club": "Al Wehda", "external_id": "wc26-alg-mustapha-zagba"},
    {"shirt_number": 23, "first_name": "Anthony", "last_name": "Mandrea", "position": Player.Position.GOALKEEPER, "club": "Caen", "external_id": "wc26-alg-anthony-mandrea"},

    {"shirt_number": 2, "first_name": "Youcef", "last_name": "Atal", "position": Player.Position.DEFENDER, "club": "Nice", "external_id": "wc26-alg-youcef-atal"},
    {"shirt_number": 3, "first_name": "Aissa", "last_name": "Mandi", "position": Player.Position.DEFENDER, "club": "Villarreal", "external_id": "wc26-alg-aissa-mandi"},
    {"shirt_number": 4, "first_name": "Ramy", "last_name": "Bensebaini", "position": Player.Position.DEFENDER, "club": "Borussia Dortmund", "external_id": "wc26-alg-ramy-bensebaini"},
    {"shirt_number": 5, "first_name": "Abdelkader", "last_name": "Bedrane", "position": Player.Position.DEFENDER, "club": "ES Tunis", "external_id": "wc26-alg-abdelkader-bedrane"},
    {"shirt_number": 13, "first_name": "Houari", "last_name": "Ferhani", "position": Player.Position.DEFENDER, "club": "JS Kabylie", "external_id": "wc26-alg-houari-ferhani"},
    {"shirt_number": 14, "first_name": "Mohamed", "last_name": "Amine Tougai", "position": Player.Position.DEFENDER, "club": "ES Tunis", "external_id": "wc26-alg-mohamed-amine-tougai"},
    {"shirt_number": 15, "first_name": "Houssem", "last_name": "Aouar", "position": Player.Position.DEFENDER, "club": "Roma", "external_id": "wc26-alg-houssem-aouar"},

    {"shirt_number": 6, "first_name": "Ismael", "last_name": "Bennacer", "position": Player.Position.MIDFIELDER, "club": "AC Milan", "external_id": "wc26-alg-ismael-bennacer"},
    {"shirt_number": 8, "first_name": "Ramiz", "last_name": "Zerrouki", "position": Player.Position.MIDFIELDER, "club": "Feyenoord", "external_id": "wc26-alg-ramiz-zerrouki"},
    {"shirt_number": 10, "first_name": "Riyad", "last_name": "Mahrez", "position": Player.Position.MIDFIELDER, "club": "Al Ahli", "external_id": "wc26-alg-riyad-mahrez"},
    {"shirt_number": 16, "first_name": "Sofiane", "last_name": "Feghouli", "position": Player.Position.MIDFIELDER, "club": "Fatih Karagümrük", "external_id": "wc26-alg-sofiane-feghouli"},
    {"shirt_number": 17, "first_name": "Nabil", "last_name": "Bentaleb", "position": Player.Position.MIDFIELDER, "club": "Lille", "external_id": "wc26-alg-nabil-bentaleb"},
    {"shirt_number": 18, "first_name": "HarIs", "last_name": "Belkebla", "position": Player.Position.MIDFIELDER, "club": "Brest", "external_id": "wc26-alg-haris-belkebla"},

    {"shirt_number": 7, "first_name": "Islam", "last_name": "Slimani", "position": Player.Position.FORWARD, "club": "Coritiba", "external_id": "wc26-alg-islam-slimani"},
    {"shirt_number": 9, "first_name": "Baghdad", "last_name": "Bounedjah", "position": Player.Position.FORWARD, "club": "Al Sadd", "external_id": "wc26-alg-baghdad-bounedjah"},
    {"shirt_number": 11, "first_name": "Said", "last_name": "Benrahma", "position": Player.Position.FORWARD, "club": "Lyon", "external_id": "wc26-alg-said-benrahma"},
    {"shirt_number": 19, "first_name": "Yacine", "last_name": "Brahimi", "position": Player.Position.FORWARD, "club": "Al Rayyan", "external_id": "wc26-alg-yacine-brahimi"},
    {"shirt_number": 20, "first_name": "Youcef", "last_name": "Belaili", "position": Player.Position.FORWARD, "club": "MC Alger", "external_id": "wc26-alg-youcef-belaili"},
    {"shirt_number": 21, "first_name": "Adam", "last_name": "Ounas", "position": Player.Position.FORWARD, "club": "Lille", "external_id": "wc26-alg-adam-ounas"},
    {"shirt_number": 22, "first_name": "Farid", "last_name": "Boulaya", "position": Player.Position.FORWARD, "club": "Al Gharafa", "external_id": "wc26-alg-farid-boulaya"},
    {"shirt_number": 24, "first_name": "Andy", "last_name": "Delort", "position": Player.Position.FORWARD, "club": "Umm Salal", "external_id": "wc26-alg-andy-delort"},
    {"shirt_number": 25, "first_name": "Bilal", "last_name": "Brahimi", "position": Player.Position.FORWARD, "club": "Nice", "external_id": "wc26-alg-bilal-brahimi"},
    {"shirt_number": 26, "first_name": "Amine", "last_name": "Gouiri", "position": Player.Position.FORWARD, "club": "Rennes", "external_id": "wc26-alg-amine-gouiri"},
]


AUSTRIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Patrick", "last_name": "Pentz", "position": Player.Position.GOALKEEPER, "club": "Brondby", "external_id": "wc26-aut-patrick-pentz"},
    {"shirt_number": 12, "first_name": "Heinz", "last_name": "Lindner", "position": Player.Position.GOALKEEPER, "club": "Sion", "external_id": "wc26-aut-heinz-lindner"},
    {"shirt_number": 23, "first_name": "Alexander", "last_name": "Schlager", "position": Player.Position.GOALKEEPER, "club": "Salzburg", "external_id": "wc26-aut-alexander-schlager"},

    {"shirt_number": 2, "first_name": "Stefan", "last_name": "Posch", "position": Player.Position.DEFENDER, "club": "Bologna", "external_id": "wc26-aut-stefan-posch"},
    {"shirt_number": 3, "first_name": "David", "last_name": "Alaba", "position": Player.Position.DEFENDER, "club": "Real Madrid", "external_id": "wc26-aut-david-alaba"},
    {"shirt_number": 4, "first_name": "Philipp", "last_name": "Lienhart", "position": Player.Position.DEFENDER, "club": "Freiburg", "external_id": "wc26-aut-philipp-lienhart"},
    {"shirt_number": 5, "first_name": "Gernot", "last_name": "Trauner", "position": Player.Position.DEFENDER, "club": "Feyenoord", "external_id": "wc26-aut-gernot-trauner"},
    {"shirt_number": 13, "first_name": "Aleksandar", "last_name": "Dragovic", "position": Player.Position.DEFENDER, "club": "Crvena Zvezda", "external_id": "wc26-aut-aleksandar-dragovic"},
    {"shirt_number": 14, "first_name": "Andreas", "last_name": "Ulmer", "position": Player.Position.DEFENDER, "club": "Salzburg", "external_id": "wc26-aut-andreas-ulmer"},
    {"shirt_number": 15, "first_name": "Maximilian", "last_name": "Wober", "position": Player.Position.DEFENDER, "club": "Borussia Monchengladbach", "external_id": "wc26-aut-maximilian-wober"},

    {"shirt_number": 6, "first_name": "Konrad", "last_name": "Laimer", "position": Player.Position.MIDFIELDER, "club": "Bayern Munich", "external_id": "wc26-aut-konrad-laimer"},
    {"shirt_number": 8, "first_name": "Marcel", "last_name": "Sabitzer", "position": Player.Position.MIDFIELDER, "club": "Borussia Dortmund", "external_id": "wc26-aut-marcel-sabitzer"},
    {"shirt_number": 10, "first_name": "Florian", "last_name": "Grillitsch", "position": Player.Position.MIDFIELDER, "club": "Hoffenheim", "external_id": "wc26-aut-florian-grillitsch"},
    {"shirt_number": 16, "first_name": "Xaver", "last_name": "Schlager", "position": Player.Position.MIDFIELDER, "club": "RB Leipzig", "external_id": "wc26-aut-xaver-schlager"},
    {"shirt_number": 17, "first_name": "Christoph", "last_name": "Baumgartner", "position": Player.Position.MIDFIELDER, "club": "RB Leipzig", "external_id": "wc26-aut-christoph-baumgartner"},
    {"shirt_number": 18, "first_name": "Dejan", "last_name": "Ljubicic", "position": Player.Position.MIDFIELDER, "club": "Koln", "external_id": "wc26-aut-dejan-ljubicic"},

    {"shirt_number": 7, "first_name": "Marko", "last_name": "Arnautovic", "position": Player.Position.FORWARD, "club": "Inter Milan", "external_id": "wc26-aut-marko-arnautovic"},
    {"shirt_number": 9, "first_name": "Michael", "last_name": "Gregoritsch", "position": Player.Position.FORWARD, "club": "Freiburg", "external_id": "wc26-aut-michael-gregoritsch"},
    {"shirt_number": 11, "first_name": "Karim", "last_name": "Onisiwo", "position": Player.Position.FORWARD, "club": "Mainz 05", "external_id": "wc26-aut-karim-onisiwo"},
    {"shirt_number": 19, "first_name": "Sasa", "last_name": "Kalajdzic", "position": Player.Position.FORWARD, "club": "Wolves", "external_id": "wc26-aut-sasa-kalajdzic"},
    {"shirt_number": 20, "first_name": "Patrick", "last_name": "Wimmer", "position": Player.Position.FORWARD, "club": "Wolfsburg", "external_id": "wc26-aut-patrick-wimmer"},
    {"shirt_number": 21, "first_name": "Andreas", "last_name": "Weimann", "position": Player.Position.FORWARD, "club": "Bristol City", "external_id": "wc26-aut-andreas-weimann"},
    {"shirt_number": 22, "first_name": "Junior", "last_name": "Adamu", "position": Player.Position.FORWARD, "club": "Freiburg", "external_id": "wc26-aut-junior-adamu"},
    {"shirt_number": 24, "first_name": "Ercan", "last_name": "Kara", "position": Player.Position.FORWARD, "club": "Samsunspor", "external_id": "wc26-aut-ercan-kara"},
    {"shirt_number": 25, "first_name": "Christoph", "last_name": "Monschein", "position": Player.Position.FORWARD, "club": "WSG Tirol", "external_id": "wc26-aut-christoph-monschein"},
    {"shirt_number": 26, "first_name": "Benjamin", "last_name": "Sesko", "position": Player.Position.FORWARD, "club": "RB Leipzig", "external_id": "wc26-aut-benjamin-sesko"},
]


JORDAN_PLAYERS = [
    {"shirt_number": 1, "first_name": "Yazeed", "last_name": "Abu Laila", "position": Player.Position.GOALKEEPER, "club": "Al Faisaly", "external_id": "wc26-jor-yazeed-abu-laila"},
    {"shirt_number": 12, "first_name": "Amer", "last_name": "Shafi", "position": Player.Position.GOALKEEPER, "club": "Shabab Al Ordon", "external_id": "wc26-jor-amer-shafi"},
    {"shirt_number": 23, "first_name": "Mazen", "last_name": "Abu Hameed", "position": Player.Position.GOALKEEPER, "club": "Al Wehdat", "external_id": "wc26-jor-mazen-abu-hameed"},

    {"shirt_number": 2, "first_name": "Ehsan", "last_name": "Haddad", "position": Player.Position.DEFENDER, "club": "Al Wehdat", "external_id": "wc26-jor-ehsan-haddad"},
    {"shirt_number": 3, "first_name": "Tareq", "last_name": "Khattab", "position": Player.Position.DEFENDER, "club": "Al Wehdat", "external_id": "wc26-jor-tareq-khattab"},
    {"shirt_number": 4, "first_name": "Bahaa", "last_name": "Abdel Rahman", "position": Player.Position.DEFENDER, "club": "Al Faisaly", "external_id": "wc26-jor-bahaa-abdel-rahman"},
    {"shirt_number": 5, "first_name": "Yazan", "last_name": "Al Arab", "position": Player.Position.DEFENDER, "club": "Al Faisaly", "external_id": "wc26-jor-yazan-al-arab"},
    {"shirt_number": 13, "first_name": "Feras", "last_name": "Shelbaya", "position": Player.Position.DEFENDER, "club": "Al Wehdat", "external_id": "wc26-jor-feras-shelbaya"},
    {"shirt_number": 14, "first_name": "Duaa", "last_name": "Al Soud", "position": Player.Position.DEFENDER, "club": "Al Faisaly", "external_id": "wc26-jor-duaa-al-soud"},
    {"shirt_number": 15, "first_name": "Mohammad", "last_name": "Abu Zrayq", "position": Player.Position.DEFENDER, "club": "Al Wehdat", "external_id": "wc26-jor-mohammad-abu-zrayq"},

    {"shirt_number": 6, "first_name": "Ahmed", "last_name": "Samer", "position": Player.Position.MIDFIELDER, "club": "Al Faisaly", "external_id": "wc26-jor-ahmed-samer"},
    {"shirt_number": 8, "first_name": "Saed", "last_name": "Al Rawashdeh", "position": Player.Position.MIDFIELDER, "club": "Shabab Al Ordon", "external_id": "wc26-jor-saed-al-rawashdeh"},
    {"shirt_number": 10, "first_name": "Mousa", "last_name": "Al Taamari", "position": Player.Position.MIDFIELDER, "club": "Montpellier", "external_id": "wc26-jor-mousa-al-taamari"},
    {"shirt_number": 16, "first_name": "Yazan", "last_name": "Al Naimat", "position": Player.Position.MIDFIELDER, "club": "Al Ahli", "external_id": "wc26-jor-yazan-al-naimat"},
    {"shirt_number": 17, "first_name": "Mahmoud", "last_name": "Al Mardi", "position": Player.Position.MIDFIELDER, "club": "Al Faisaly", "external_id": "wc26-jor-mahmoud-al-mardi"},
    {"shirt_number": 18, "first_name": "Ali", "last_name": "Odeh", "position": Player.Position.MIDFIELDER, "club": "Al Hussein", "external_id": "wc26-jor-ali-odeh"},

    {"shirt_number": 7, "first_name": "Hamza", "last_name": "Al Dardour", "position": Player.Position.FORWARD, "club": "Al Sareeh", "external_id": "wc26-jor-hamza-al-dardour"},
    {"shirt_number": 9, "first_name": "Odai", "last_name": "Al Saify", "position": Player.Position.FORWARD, "club": "Al Faisaly", "external_id": "wc26-jor-odai-al-saify"},
    {"shirt_number": 11, "first_name": "Yousef", "last_name": "Al Rawabdeh", "position": Player.Position.FORWARD, "club": "Al Wehdat", "external_id": "wc26-jor-yousef-al-rawabdeh"},
    {"shirt_number": 19, "first_name": "Ahmed", "last_name": "Ersan", "position": Player.Position.FORWARD, "club": "Al Faisaly", "external_id": "wc26-jor-ahmed-ersan"},
    {"shirt_number": 20, "first_name": "Ali", "last_name": "Khader", "position": Player.Position.FORWARD, "club": "Al Wehdat", "external_id": "wc26-jor-ali-khader"},
    {"shirt_number": 21, "first_name": "Mohannad", "last_name": "Khair", "position": Player.Position.FORWARD, "club": "Al Ramtha", "external_id": "wc26-jor-mohannad-khair"},
    {"shirt_number": 22, "first_name": "Tamim", "last_name": "Saeed", "position": Player.Position.FORWARD, "club": "Al Jazeera", "external_id": "wc26-jor-tamim-saeed"},
    {"shirt_number": 24, "first_name": "Zaid", "last_name": "Jaber", "position": Player.Position.FORWARD, "club": "Al Faisaly", "external_id": "wc26-jor-zaid-jaber"},
    {"shirt_number": 25, "first_name": "Malek", "last_name": "Bani Attiah", "position": Player.Position.FORWARD, "club": "Al Wehdat", "external_id": "wc26-jor-malek-bani-attiah"},
    {"shirt_number": 26, "first_name": "Anas", "last_name": "Hammad", "position": Player.Position.FORWARD, "club": "Al Hussein", "external_id": "wc26-jor-anas-hammad"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo J del Mundial 2026"

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
            argentina = Team.objects.get(fifa_code="ARG")
            algeria = Team.objects.get(fifa_code="ALG")
            austria = Team.objects.get(fifa_code="AUT")
            jordan = Team.objects.get(fifa_code="JOR")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo J en la base de datos: {exc}")

        results = []

        results.append(("Argentina", *self.load_players_for_team(argentina, ARGENTINA_PLAYERS)))
        results.append(("Algeria", *self.load_players_for_team(algeria, ALGERIA_PLAYERS)))
        results.append(("Austria", *self.load_players_for_team(austria, AUSTRIA_PLAYERS)))
        results.append(("Jordan", *self.load_players_for_team(jordan, JORDAN_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo J completada."))