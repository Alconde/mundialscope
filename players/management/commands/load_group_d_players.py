from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


USA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Matt", "last_name": "Turner", "position": Player.Position.GOALKEEPER, "club": "Nottingham Forest", "external_id": "wc26-usa-matt-turner"},
    {"shirt_number": 12, "first_name": "Ethan", "last_name": "Horvath", "position": Player.Position.GOALKEEPER, "club": "Cardiff City", "external_id": "wc26-usa-ethan-horvath"},
    {"shirt_number": 23, "first_name": "Gaga", "last_name": "Slonina", "position": Player.Position.GOALKEEPER, "club": "Chelsea", "external_id": "wc26-usa-gaga-slonina"},

    {"shirt_number": 2, "first_name": "Sergino", "last_name": "Dest", "position": Player.Position.DEFENDER, "club": "PSV", "external_id": "wc26-usa-sergino-dest"},
    {"shirt_number": 3, "first_name": "Antonee", "last_name": "Robinson", "position": Player.Position.DEFENDER, "club": "Fulham", "external_id": "wc26-usa-antonee-robinson"},
    {"shirt_number": 4, "first_name": "Chris", "last_name": "Richards", "position": Player.Position.DEFENDER, "club": "Crystal Palace", "external_id": "wc26-usa-chris-richards"},
    {"shirt_number": 5, "first_name": "Tim", "last_name": "Ream", "position": Player.Position.DEFENDER, "club": "Fulham", "external_id": "wc26-usa-tim-ream"},
    {"shirt_number": 13, "first_name": "Joe", "last_name": "Scally", "position": Player.Position.DEFENDER, "club": "Borussia Monchengladbach", "external_id": "wc26-usa-joe-scally"},
    {"shirt_number": 14, "first_name": "Miles", "last_name": "Robinson", "position": Player.Position.DEFENDER, "club": "FC Cincinnati", "external_id": "wc26-usa-miles-robinson"},
    {"shirt_number": 15, "first_name": "Cameron", "last_name": "Carter-Vickers", "position": Player.Position.DEFENDER, "club": "Celtic", "external_id": "wc26-usa-cameron-carter-vickers"},

    {"shirt_number": 6, "first_name": "Tyler", "last_name": "Adams", "position": Player.Position.MIDFIELDER, "club": "Bournemouth", "external_id": "wc26-usa-tyler-adams"},
    {"shirt_number": 8, "first_name": "Weston", "last_name": "McKennie", "position": Player.Position.MIDFIELDER, "club": "Juventus", "external_id": "wc26-usa-weston-mckennie"},
    {"shirt_number": 10, "first_name": "Christian", "last_name": "Pulisic", "position": Player.Position.MIDFIELDER, "club": "AC Milan", "external_id": "wc26-usa-christian-pulisic"},
    {"shirt_number": 16, "first_name": "Gio", "last_name": "Reyna", "position": Player.Position.MIDFIELDER, "club": "Nottingham Forest", "external_id": "wc26-usa-gio-reyna"},
    {"shirt_number": 17, "first_name": "Yunus", "last_name": "Musah", "position": Player.Position.MIDFIELDER, "club": "AC Milan", "external_id": "wc26-usa-yunus-musah"},
    {"shirt_number": 18, "first_name": "Johnny", "last_name": "Cardoso", "position": Player.Position.MIDFIELDER, "club": "Real Betis", "external_id": "wc26-usa-johnny-cardoso"},

    {"shirt_number": 7, "first_name": "Timothy", "last_name": "Weah", "position": Player.Position.FORWARD, "club": "Juventus", "external_id": "wc26-usa-tim-weah"},
    {"shirt_number": 9, "first_name": "Folarin", "last_name": "Balogun", "position": Player.Position.FORWARD, "club": "Monaco", "external_id": "wc26-usa-folarin-balogun"},
    {"shirt_number": 11, "first_name": "Brenden", "last_name": "Aaronson", "position": Player.Position.FORWARD, "club": "Union Berlin", "external_id": "wc26-usa-brenden-aaronson"},
    {"shirt_number": 19, "first_name": "Haji", "last_name": "Wright", "position": Player.Position.FORWARD, "club": "Coventry City", "external_id": "wc26-usa-haji-wright"},
    {"shirt_number": 20, "first_name": "Ricardo", "last_name": "Pepi", "position": Player.Position.FORWARD, "club": "PSV", "external_id": "wc26-usa-ricardo-pepi"},
    {"shirt_number": 21, "first_name": "Josh", "last_name": "Sargent", "position": Player.Position.FORWARD, "club": "Norwich City", "external_id": "wc26-usa-josh-sargent"},
    {"shirt_number": 22, "first_name": "Malik", "last_name": "Tillman", "position": Player.Position.FORWARD, "club": "PSV", "external_id": "wc26-usa-malik-tillman"},
    {"shirt_number": 24, "first_name": "Kevin", "last_name": "Paredes", "position": Player.Position.FORWARD, "club": "Wolfsburg", "external_id": "wc26-usa-kevin-paredes"},
    {"shirt_number": 25, "first_name": "Jordan", "last_name": "Pefok", "position": Player.Position.FORWARD, "club": "Borussia Monchengladbach", "external_id": "wc26-usa-jordan-pefok"},
    {"shirt_number": 26, "first_name": "Paxten", "last_name": "Aaronson", "position": Player.Position.FORWARD, "club": "Eintracht Frankfurt", "external_id": "wc26-usa-paxten-aaronson"},
]


PARAGUAY_PLAYERS = [
    {"shirt_number": 1, "first_name": "Carlos", "last_name": "Coronel", "position": Player.Position.GOALKEEPER, "club": "New York Red Bulls", "external_id": "wc26-par-carlos-coronel"},
    {"shirt_number": 12, "first_name": "Santiago", "last_name": "Rojas", "position": Player.Position.GOALKEEPER, "club": "Tigre", "external_id": "wc26-par-santiago-rojas"},
    {"shirt_number": 23, "first_name": "Alfredo", "last_name": "Aguilar", "position": Player.Position.GOALKEEPER, "club": "Cerro Porteno", "external_id": "wc26-par-alfredo-aguilar"},

    {"shirt_number": 2, "first_name": "Gustavo", "last_name": "Velazquez", "position": Player.Position.DEFENDER, "club": "Guarani", "external_id": "wc26-par-gustavo-velazquez"},
    {"shirt_number": 3, "first_name": "Omar", "last_name": "Alderete", "position": Player.Position.DEFENDER, "club": "Getafe", "external_id": "wc26-par-omar-alderete"},
    {"shirt_number": 4, "first_name": "Fabian", "last_name": "Balbuena", "position": Player.Position.DEFENDER, "club": "Corinthians", "external_id": "wc26-par-fabian-balbuena"},
    {"shirt_number": 5, "first_name": "Junior", "last_name": "Alonso", "position": Player.Position.DEFENDER, "club": "Krasnodar", "external_id": "wc26-par-junior-alonso"},
    {"shirt_number": 13, "first_name": "Robert", "last_name": "Rojas", "position": Player.Position.DEFENDER, "club": "River Plate", "external_id": "wc26-par-robert-rojas"},
    {"shirt_number": 14, "first_name": "Blas", "last_name": "Riveros", "position": Player.Position.DEFENDER, "club": "Brondby", "external_id": "wc26-par-blas-riveros"},
    {"shirt_number": 15, "first_name": "Santiago", "last_name": "Arzamendia", "position": Player.Position.DEFENDER, "club": "Cadiz", "external_id": "wc26-par-santiago-arzamendia"},

    {"shirt_number": 6, "first_name": "Mathias", "last_name": "Villasanti", "position": Player.Position.MIDFIELDER, "club": "Gremio", "external_id": "wc26-par-mathias-villasanti"},
    {"shirt_number": 8, "first_name": "Miguel", "last_name": "Almiron", "position": Player.Position.MIDFIELDER, "club": "Newcastle United", "external_id": "wc26-par-miguel-almiron"},
    {"shirt_number": 10, "first_name": "Angel", "last_name": "Cardozo", "position": Player.Position.MIDFIELDER, "club": "Olimpia", "external_id": "wc26-par-angel-cardozo"},
    {"shirt_number": 16, "first_name": "Richard", "last_name": "Sanchez", "position": Player.Position.MIDFIELDER, "club": "Club America", "external_id": "wc26-par-richard-sanchez"},
    {"shirt_number": 17, "first_name": "Diego", "last_name": "Gomez", "position": Player.Position.MIDFIELDER, "club": "Inter Miami", "external_id": "wc26-par-diego-gomez"},
    {"shirt_number": 18, "first_name": "Matias", "last_name": "Rojas", "position": Player.Position.MIDFIELDER, "club": "Internacional", "external_id": "wc26-par-matias-rojas"},

    {"shirt_number": 7, "first_name": "Alejandro", "last_name": "Romero", "position": Player.Position.FORWARD, "club": "Al Ain", "external_id": "wc26-par-alejandro-romero"},
    {"shirt_number": 9, "first_name": "Gabriel", "last_name": "Avalos", "position": Player.Position.FORWARD, "club": "Argentinos Juniors", "external_id": "wc26-par-gabriel-avalos"},
    {"shirt_number": 11, "first_name": "Carlos", "last_name": "Gonzalez", "position": Player.Position.FORWARD, "club": "Toluca", "external_id": "wc26-par-carlos-gonzalez"},
    {"shirt_number": 19, "first_name": "Julio", "last_name": "Enciso", "position": Player.Position.FORWARD, "club": "Brighton", "external_id": "wc26-par-julio-enciso"},
    {"shirt_number": 20, "first_name": "Derlis", "last_name": "Gonzalez", "position": Player.Position.FORWARD, "club": "Olympiacos", "external_id": "wc26-par-derlis-gonzalez"},
    {"shirt_number": 21, "first_name": "Antonio", "last_name": "Sanabria", "position": Player.Position.FORWARD, "club": "Torino", "external_id": "wc26-par-antonio-sanabria"},
    {"shirt_number": 22, "first_name": "Robert", "last_name": "Morinigo", "position": Player.Position.FORWARD, "club": "Libertad", "external_id": "wc26-par-robert-morinigo"},
    {"shirt_number": 24, "first_name": "Sebastian", "last_name": "Ferreira", "position": Player.Position.FORWARD, "club": "Houston Dynamo", "external_id": "wc26-par-sebastian-ferreira"},
    {"shirt_number": 25, "first_name": "Rodrigo", "last_name": "Morinigo", "position": Player.Position.FORWARD, "club": "Olimpia", "external_id": "wc26-par-rodrigo-morinigo"},
    {"shirt_number": 26, "first_name": "Ivan", "last_name": "Franco", "position": Player.Position.FORWARD, "club": "CA Talleres", "external_id": "wc26-par-ivan-franco"},
]


AUSTRALIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Mathew", "last_name": "Ryan", "position": Player.Position.GOALKEEPER, "club": "AZ Alkmaar", "external_id": "wc26-aus-mathew-ryan"},
    {"shirt_number": 12, "first_name": "Joe", "last_name": "Gauci", "position": Player.Position.GOALKEEPER, "club": "Aston Villa", "external_id": "wc26-aus-joe-gauci"},
    {"shirt_number": 23, "first_name": "Thomas", "last_name": "Deng", "position": Player.Position.GOALKEEPER, "club": "Albirex Niigata", "external_id": "wc26-aus-thomas-deng"},

    {"shirt_number": 2, "first_name": "Nathaniel", "last_name": "Atkinson", "position": Player.Position.DEFENDER, "club": "Hearts", "external_id": "wc26-aus-nathaniel-atkinson"},
    {"shirt_number": 3, "first_name": "Kye", "last_name": "Rowles", "position": Player.Position.DEFENDER, "club": "Hearts", "external_id": "wc26-aus-kye-rowles"},
    {"shirt_number": 4, "first_name": "Harry", "last_name": "Souttar", "position": Player.Position.DEFENDER, "club": "Leicester City", "external_id": "wc26-aus-harry-souttar"},
    {"shirt_number": 5, "first_name": "Aziz", "last_name": "Behich", "position": Player.Position.DEFENDER, "club": "Melbourne City", "external_id": "wc26-aus-aziz-behich"},
    {"shirt_number": 13, "first_name": "Thomas", "last_name": "Deng", "position": Player.Position.DEFENDER, "club": "Albirex Niigata", "external_id": "wc26-aus-thomas-deng-def"},
    {"shirt_number": 14, "first_name": "Fran", "last_name": "Karacic", "position": Player.Position.DEFENDER, "club": "Brescia", "external_id": "wc26-aus-fran-karacic"},
    {"shirt_number": 15, "first_name": "Jordan", "last_name": "Bos", "position": Player.Position.DEFENDER, "club": "Westerlo", "external_id": "wc26-aus-jordan-bos"},

    {"shirt_number": 6, "first_name": "Jackson", "last_name": "Irvine", "position": Player.Position.MIDFIELDER, "club": "St. Pauli", "external_id": "wc26-aus-jackson-irvine"},
    {"shirt_number": 8, "first_name": "Ajdin", "last_name": "Hrustic", "position": Player.Position.MIDFIELDER, "club": "Hertha BSC", "external_id": "wc26-aus-ajdin-hrustic"},
    {"shirt_number": 10, "first_name": "Riley", "last_name": "McGree", "position": Player.Position.MIDFIELDER, "club": "Middlesbrough", "external_id": "wc26-aus-riley-mcgree"},
    {"shirt_number": 16, "first_name": "Keanu", "last_name": "Baccus", "position": Player.Position.MIDFIELDER, "club": "St. Mirren", "external_id": "wc26-aus-keanu-baccus"},
    {"shirt_number": 17, "first_name": "Connor", "last_name": "Metcalfe", "position": Player.Position.MIDFIELDER, "club": "St. Pauli", "external_id": "wc26-aus-connor-metcalfe"},
    {"shirt_number": 18, "first_name": "Denis", "last_name": "Genreau", "position": Player.Position.MIDFIELDER, "club": "Toulouse", "external_id": "wc26-aus-denis-genreau"},

    {"shirt_number": 7, "first_name": "Mathew", "last_name": "Leckie", "position": Player.Position.FORWARD, "club": "Melbourne City", "external_id": "wc26-aus-mathew-leckie"},
    {"shirt_number": 9, "first_name": "Jamie", "last_name": "Maclaren", "position": Player.Position.FORWARD, "club": "Melbourne City", "external_id": "wc26-aus-jamie-maclaren"},
    {"shirt_number": 11, "first_name": "Awer", "last_name": "Mabil", "position": Player.Position.FORWARD, "club": "Grasshoppers", "external_id": "wc26-aus-awer-mabil"},
    {"shirt_number": 19, "first_name": "Brandon", "last_name": "Borrello", "position": Player.Position.FORWARD, "club": "Western Sydney Wanderers", "external_id": "wc26-aus-brandon-borrello"},
    {"shirt_number": 20, "first_name": "Marco", "last_name": "Tilio", "position": Player.Position.FORWARD, "club": "Celtic", "external_id": "wc26-aus-marco-tilio"},
    {"shirt_number": 21, "first_name": "Garang", "last_name": "Kuol", "position": Player.Position.FORWARD, "club": "Newcastle United", "external_id": "wc26-aus-garang-kuol"},
    {"shirt_number": 22, "first_name": "Mitchell", "last_name": "Duke", "position": Player.Position.FORWARD, "club": "Machida Zelvia", "external_id": "wc26-aus-mitchell-duke"},
    {"shirt_number": 24, "first_name": "Alou", "last_name": "Kuol", "position": Player.Position.FORWARD, "club": "Stuttgart", "external_id": "wc26-aus-alou-kuol"},
    {"shirt_number": 25, "first_name": "Nicholas", "last_name": "D'Agostino", "position": Player.Position.FORWARD, "club": "Viking FK", "external_id": "wc26-aus-nicholas-dagostino"},
    {"shirt_number": 26, "first_name": "Jason", "last_name": "Cummings", "position": Player.Position.FORWARD, "club": "Central Coast Mariners", "external_id": "wc26-aus-jason-cummings"},
]


TURKEY_PLAYERS = [
    {"shirt_number": 1, "first_name": "Ugurcan", "last_name": "Cakir", "position": Player.Position.GOALKEEPER, "club": "Trabzonspor", "external_id": "wc26-tur-ugurcan-cakir"},
    {"shirt_number": 12, "first_name": "Altay", "last_name": "Bayindir", "position": Player.Position.GOALKEEPER, "club": "Manchester United", "external_id": "wc26-tur-altay-bayindir"},
    {"shirt_number": 23, "first_name": "Mert", "last_name": "Gununok", "position": Player.Position.GOALKEEPER, "club": "Besiktas", "external_id": "wc26-tur-mert-gununok"},

    {"shirt_number": 2, "first_name": "Zeki", "last_name": "Celik", "position": Player.Position.DEFENDER, "club": "Roma", "external_id": "wc26-tur-zeki-celik"},
    {"shirt_number": 3, "first_name": "Merih", "last_name": "Demiral", "position": Player.Position.DEFENDER, "club": "Al Ahli", "external_id": "wc26-tur-merih-demiral"},
    {"shirt_number": 4, "first_name": "Caglar", "last_name": "Soyuncu", "position": Player.Position.DEFENDER, "club": "Fenerbahce", "external_id": "wc26-tur-caglar-soyuncu"},
    {"shirt_number": 5, "first_name": "Ozan", "last_name": "Kabak", "position": Player.Position.DEFENDER, "club": "Hoffenheim", "external_id": "wc26-tur-ozan-kabak"},
    {"shirt_number": 13, "first_name": "Ferdi", "last_name": "Kadioglu", "position": Player.Position.DEFENDER, "club": "Fenerbahce", "external_id": "wc26-tur-ferdi-kadioglu"},
    {"shirt_number": 14, "first_name": "Ridvan", "last_name": "Yilmaz", "position": Player.Position.DEFENDER, "club": "Rangers", "external_id": "wc26-tur-ridvan-yilmaz"},
    {"shirt_number": 15, "first_name": "Ahmetcan", "last_name": "Kaplan", "position": Player.Position.DEFENDER, "club": "Ajax", "external_id": "wc26-tur-ahmetcan-kaplan"},
    {"shirt_number": 16, "first_name": "Abdulkadir", "last_name": "Omur", "position": Player.Position.DEFENDER, "club": "Trabzonspor", "external_id": "wc26-tur-abdulkadir-omur"},

    {"shirt_number": 6, "first_name": "Hakan", "last_name": "Calhanoglu", "position": Player.Position.MIDFIELDER, "club": "Inter Milan", "external_id": "wc26-tur-hakan-calhanoglu"},
    {"shirt_number": 8, "first_name": "Orkun", "last_name": "Kokcu", "position": Player.Position.MIDFIELDER, "club": "Benfica", "external_id": "wc26-tur-orkun-kokcu"},
    {"shirt_number": 10, "first_name": "Yusuf", "last_name": "Yazici", "position": Player.Position.MIDFIELDER, "club": "Lille", "external_id": "wc26-tur-yusuf-yazici"},
    {"shirt_number": 17, "first_name": "Salih", "last_name": "Ozan", "position": Player.Position.MIDFIELDER, "club": "Besiktas", "external_id": "wc26-tur-salih-ozan"},
    {"shirt_number": 18, "first_name": "Okay", "last_name": "Yokuslu", "position": Player.Position.MIDFIELDER, "club": "West Brom", "external_id": "wc26-tur-okay-yokuslu"},

    {"shirt_number": 7, "first_name": "Cengiz", "last_name": "Under", "position": Player.Position.FORWARD, "club": "Fenerbahce", "external_id": "wc26-tur-cengiz-under"},
    {"shirt_number": 9, "first_name": "Enes", "last_name": "Unal", "position": Player.Position.FORWARD, "club": "Bournemouth", "external_id": "wc26-tur-enes-unal"},
    {"shirt_number": 11, "first_name": "Arda", "last_name": "Guler", "position": Player.Position.FORWARD, "club": "Real Madrid", "external_id": "wc26-tur-arda-guler"},
    {"shirt_number": 19, "first_name": "Kerem", "last_name": "Akturkoglu", "position": Player.Position.FORWARD, "club": "Galatasaray", "external_id": "wc26-tur-kerem-akturkoglu"},
    {"shirt_number": 20, "first_name": "Baris", "last_name": "Yilmaz", "position": Player.Position.FORWARD, "club": "Rennes", "external_id": "wc26-tur-baris-yilmaz"},
    {"shirt_number": 21, "first_name": "Bertuğ", "last_name": "Yildirim", "position": Player.Position.FORWARD, "club": "Rennes", "external_id": "wc26-tur-bertug-yildirim"},
    {"shirt_number": 22, "first_name": "Umut", "last_name": "Nayir", "position": Player.Position.FORWARD, "club": "Pendikspor", "external_id": "wc26-tur-umut-nayir"},
    {"shirt_number": 24, "first_name": "Ugur", "last_name": "Kafkas", "position": Player.Position.FORWARD, "club": "Trabzonspor", "external_id": "wc26-tur-ugur-kafkas"},
    {"shirt_number": 25, "first_name": "Irfan", "last_name": "Kahveci", "position": Player.Position.FORWARD, "club": "Fenerbahce", "external_id": "wc26-tur-irfan-kahveci"},
    {"shirt_number": 26, "first_name": "Mehmet", "last_name": "Aydin", "position": Player.Position.FORWARD, "club": "Schalke 04", "external_id": "wc26-tur-mehmet-aydin"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo D del Mundial 2026"

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
            usa = Team.objects.get(fifa_code="USA")
            paraguay = Team.objects.get(fifa_code="PAR")
            australia = Team.objects.get(fifa_code="AUS")
            turkey = Team.objects.get(fifa_code="TUR")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo D en la base de datos: {exc}")

        results = []

        results.append(("USA", *self.load_players_for_team(usa, USA_PLAYERS)))
        results.append(("Paraguay", *self.load_players_for_team(paraguay, PARAGUAY_PLAYERS)))
        results.append(("Australia", *self.load_players_for_team(australia, AUSTRALIA_PLAYERS)))
        results.append(("Turkey", *self.load_players_for_team(turkey, TURKEY_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo D completada."))