from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


FRANCE_PLAYERS = [
    {"shirt_number": 1, "first_name": "Mike", "last_name": "Maignan", "position": Player.Position.GOALKEEPER, "club": "AC Milan", "external_id": "wc26-fra-mike-maignan"},
    {"shirt_number": 12, "first_name": "Alphonse", "last_name": "Areola", "position": Player.Position.GOALKEEPER, "club": "West Ham United", "external_id": "wc26-fra-alphonse-areola"},
    {"shirt_number": 23, "first_name": "Brice", "last_name": "Samba", "position": Player.Position.GOALKEEPER, "club": "Lens", "external_id": "wc26-fra-brice-samba"},

    {"shirt_number": 2, "first_name": "Jules", "last_name": "Kounde", "position": Player.Position.DEFENDER, "club": "Barcelona", "external_id": "wc26-fra-jules-kounde"},
    {"shirt_number": 3, "first_name": "Theo", "last_name": "Hernandez", "position": Player.Position.DEFENDER, "club": "AC Milan", "external_id": "wc26-fra-theo-hernandez"},
    {"shirt_number": 4, "first_name": "Dayot", "last_name": "Upamecano", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-fra-dayot-upamecano"},
    {"shirt_number": 5, "first_name": "Ibrahima", "last_name": "Konate", "position": Player.Position.DEFENDER, "club": "Liverpool", "external_id": "wc26-fra-ibrahima-konate"},
    {"shirt_number": 13, "first_name": "William", "last_name": "Saliba", "position": Player.Position.DEFENDER, "club": "Arsenal", "external_id": "wc26-fra-william-saliba"},
    {"shirt_number": 14, "first_name": "Ferland", "last_name": "Mendy", "position": Player.Position.DEFENDER, "club": "Real Madrid", "external_id": "wc26-fra-ferland-mendy"},
    {"shirt_number": 15, "first_name": "Benjamin", "last_name": "Pavard", "position": Player.Position.DEFENDER, "club": "Inter Milan", "external_id": "wc26-fra-benjamin-pavard"},

    {"shirt_number": 6, "first_name": "Aurelien", "last_name": "Tchouameni", "position": Player.Position.MIDFIELDER, "club": "Real Madrid", "external_id": "wc26-fra-aurelien-tchouameni"},
    {"shirt_number": 8, "first_name": "Eduardo", "last_name": "Camavinga", "position": Player.Position.MIDFIELDER, "club": "Real Madrid", "external_id": "wc26-fra-eduardo-camavinga"},
    {"shirt_number": 10, "first_name": "Antoine", "last_name": "Griezmann", "position": Player.Position.MIDFIELDER, "club": "Atletico Madrid", "external_id": "wc26-fra-antoine-griezmann"},
    {"shirt_number": 16, "first_name": "Adrien", "last_name": "Rabiot", "position": Player.Position.MIDFIELDER, "club": "Juventus", "external_id": "wc26-fra-adrien-rabiot"},
    {"shirt_number": 17, "first_name": "Youssouf", "last_name": "Fofana", "position": Player.Position.MIDFIELDER, "club": "Monaco", "external_id": "wc26-fra-youssouf-fofana"},
    {"shirt_number": 18, "first_name": "Warren", "last_name": "Zaire-Emery", "position": Player.Position.MIDFIELDER, "club": "Paris Saint-Germain", "external_id": "wc26-fra-warren-zaire-emery"},

    {"shirt_number": 7, "first_name": "Kylian", "last_name": "Mbappe", "position": Player.Position.FORWARD, "club": "Real Madrid", "external_id": "wc26-fra-kylian-mbappe"},
    {"shirt_number": 9, "first_name": "Olivier", "last_name": "Giroud", "position": Player.Position.FORWARD, "club": "Los Angeles FC", "external_id": "wc26-fra-olivier-giroud"},
    {"shirt_number": 11, "first_name": "Ousmane", "last_name": "Dembele", "position": Player.Position.FORWARD, "club": "Paris Saint-Germain", "external_id": "wc26-fra-ousmane-dembele"},
    {"shirt_number": 19, "first_name": "Randal", "last_name": "Kolo Muani", "position": Player.Position.FORWARD, "club": "Paris Saint-Germain", "external_id": "wc26-fra-randal-kolo-muani"},
    {"shirt_number": 20, "first_name": "Kingsley", "last_name": "Coman", "position": Player.Position.FORWARD, "club": "Bayern Munich", "external_id": "wc26-fra-kingsley-coman"},
    {"shirt_number": 21, "first_name": "Marcus", "last_name": "Thuram", "position": Player.Position.FORWARD, "club": "Inter Milan", "external_id": "wc26-fra-marcus-thuram"},
    {"shirt_number": 22, "first_name": "Bradley", "last_name": "Barcola", "position": Player.Position.FORWARD, "club": "Paris Saint-Germain", "external_id": "wc26-fra-bradley-barcola"},
    {"shirt_number": 24, "first_name": "Christopher", "last_name": "Nkunku", "position": Player.Position.FORWARD, "club": "Chelsea", "external_id": "wc26-fra-christopher-nkunku"},
    {"shirt_number": 25, "first_name": "Moussa", "last_name": "Diaby", "position": Player.Position.FORWARD, "club": "Aston Villa", "external_id": "wc26-fra-moussa-diaby"},
    {"shirt_number": 26, "first_name": "Rayan", "last_name": "Cherki", "position": Player.Position.FORWARD, "club": "Lyon", "external_id": "wc26-fra-rayan-cherki"},
]


SENEGAL_PLAYERS = [
    {"shirt_number": 1, "first_name": "Edouard", "last_name": "Mendy", "position": Player.Position.GOALKEEPER, "club": "Al Ahli", "external_id": "wc26-sen-edouard-mendy"},
    {"shirt_number": 12, "first_name": "Alfred", "last_name": "Gomis", "position": Player.Position.GOALKEEPER, "club": "Lorient", "external_id": "wc26-sen-alfred-gomis"},
    {"shirt_number": 23, "first_name": "Seny", "last_name": "Dieng", "position": Player.Position.GOALKEEPER, "club": "Middlesbrough", "external_id": "wc26-sen-seny-dieng"},

    {"shirt_number": 2, "first_name": "Youssouf", "last_name": "Sabal y", "position": Player.Position.DEFENDER, "club": "Real Betis", "external_id": "wc26-sen-youssouf-sabaly"},
    {"shirt_number": 3, "first_name": "Kalidou", "last_name": "Koulibaly", "position": Player.Position.DEFENDER, "club": "Al Hilal", "external_id": "wc26-sen-kalidou-koulibaly"},
    {"shirt_number": 4, "first_name": "Pape Abou", "last_name": "Cisse", "position": Player.Position.DEFENDER, "club": "Olympiacos", "external_id": "wc26-sen-pape-abou-cisse"},
    {"shirt_number": 5, "first_name": "Abdou Diallo", "last_name": "", "position": Player.Position.DEFENDER, "club": "Al-Arabi", "external_id": "wc26-sen-abdou-diallo"},
    {"shirt_number": 13, "first_name": "Fode", "last_name": "Ball o-Toure", "position": Player.Position.DEFENDER, "club": "Fulham", "external_id": "wc26-sen-fode-ballo-toure"},
    {"shirt_number": 14, "first_name": "Ismail", "last_name": "Jakobs", "position": Player.Position.DEFENDER, "club": "Monaco", "external_id": "wc26-sen-ismail-jakobs"},
    {"shirt_number": 15, "first_name": "Moussa", "last_name": "Niakhate", "position": Player.Position.DEFENDER, "club": "Nottingham Forest", "external_id": "wc26-sen-moussa-niakhate"},

    {"shirt_number": 6, "first_name": "Idrissa Gana", "last_name": "Gueye", "position": Player.Position.MIDFIELDER, "club": "Everton", "external_id": "wc26-sen-idrissa-gueye"},
    {"shirt_number": 8, "first_name": "Pape", "last_name": "Guye", "position": Player.Position.MIDFIELDER, "club": "Sevilla", "external_id": "wc26-sen-pape-guye"},
    {"shirt_number": 10, "first_name": "Sadio", "last_name": "Mane", "position": Player.Position.MIDFIELDER, "club": "Al Nassr", "external_id": "wc26-sen-sadio-mane"},
    {"shirt_number": 16, "first_name": "Nampalys", "last_name": "Mendy", "position": Player.Position.MIDFIELDER, "club": "Lens", "external_id": "wc26-sen-nampalys-mendy"},
    {"shirt_number": 17, "first_name": "Krepin", "last_name": "Diatta", "position": Player.Position.MIDFIELDER, "club": "Monaco", "external_id": "wc26-sen-krepin-diatta"},
    {"shirt_number": 18, "first_name": "Pape Matar", "last_name": "Sarr", "position": Player.Position.MIDFIELDER, "club": "Tottenham Hotspur", "external_id": "wc26-sen-pape-matar-sarr"},

    {"shirt_number": 7, "first_name": "Ismaila", "last_name": "Sarr", "position": Player.Position.FORWARD, "club": "Marseille", "external_id": "wc26-sen-ismaila-sarr"},
    {"shirt_number": 9, "first_name": "Boulaye", "last_name": "Dia", "position": Player.Position.FORWARD, "club": "Salernitana", "external_id": "wc26-sen-boulaye-dia"},
    {"shirt_number": 11, "first_name": "Habib Diallo", "last_name": "", "position": Player.Position.FORWARD, "club": "Al Shabab", "external_id": "wc26-sen-habib-diallo"},
    {"shirt_number": 19, "first_name": "Nicolas", "last_name": "Jackson", "position": Player.Position.FORWARD, "club": "Chelsea", "external_id": "wc26-sen-nicolas-jackson"},
    {"shirt_number": 20, "first_name": "Bamba", "last_name": "Dieng", "position": Player.Position.FORWARD, "club": "Lorient", "external_id": "wc26-sen-bamba-dieng"},
    {"shirt_number": 21, "first_name": "Famara", "last_name": "Diedhiou", "position": Player.Position.FORWARD, "club": "Al Ahli", "external_id": "wc26-sen-famara-diedhiou"},
    {"shirt_number": 22, "first_name": "Iliman", "last_name": "Ndiaye", "position": Player.Position.FORWARD, "club": "Everton", "external_id": "wc26-sen-iliman-ndiaye"},
    {"shirt_number": 24, "first_name": "Boulaye", "last_name": "Traore", "position": Player.Position.FORWARD, "club": "Metz", "external_id": "wc26-sen-boulaye-traore"},
    {"shirt_number": 25, "first_name": "Demba", "last_name": "Seck", "position": Player.Position.FORWARD, "club": "Torino", "external_id": "wc26-sen-demba-seck"},
    {"shirt_number": 26, "first_name": "Amara", "last_name": "Diouf", "position": Player.Position.FORWARD, "club": "Metz", "external_id": "wc26-sen-amara-diouf"},
]


IRAQ_PLAYERS = [
    {"shirt_number": 1, "first_name": "Jalal", "last_name": "Hassan", "position": Player.Position.GOALKEEPER, "club": "Al Zawraa", "external_id": "wc26-irq-jalal-hassan"},
    {"shirt_number": 12, "first_name": "Fahad", "last_name": "Talib", "position": Player.Position.GOALKEEPER, "club": "Al Shorta", "external_id": "wc26-irq-fahad-talib"},
    {"shirt_number": 23, "first_name": "Ali", "last_name": "Yahya", "position": Player.Position.GOALKEEPER, "club": "Al Quwa Al Jawiya", "external_id": "wc26-irq-ali-yahya"},

    {"shirt_number": 2, "first_name": "Rebin", "last_name": "Sulaka", "position": Player.Position.DEFENDER, "club": "Buriram United", "external_id": "wc26-irq-rebin-sulaka"},
    {"shirt_number": 3, "first_name": "Ahmad", "last_name": "Ibrahim", "position": Player.Position.DEFENDER, "club": "Al Shorta", "external_id": "wc26-irq-ahmad-ibrahim"},
    {"shirt_number": 4, "first_name": "Ali", "last_name": "Faez", "position": Player.Position.DEFENDER, "club": "Al Shorta", "external_id": "wc26-irq-ali-faez"},
    {"shirt_number": 5, "first_name": "Hussein", "last_name": "Ammar", "position": Player.Position.DEFENDER, "club": "Al Zawraa", "external_id": "wc26-irq-hussein-ammar"},
    {"shirt_number": 13, "first_name": "Mohammed", "last_name": "Qasim", "position": Player.Position.DEFENDER, "club": "Al Shorta", "external_id": "wc26-irq-mohammed-qasim"},
    {"shirt_number": 14, "first_name": "Ali", "last_name": "Adnan", "position": Player.Position.DEFENDER, "club": "Rubin Kazan", "external_id": "wc26-irq-ali-adnan"},
    {"shirt_number": 15, "first_name": "Mustafa", "last_name": "Nadhim", "position": Player.Position.DEFENDER, "club": "Al Talaba", "external_id": "wc26-irq-mustafa-nadhim"},

    {"shirt_number": 6, "first_name": "Amir", "last_name": "Al Ammari", "position": Player.Position.MIDFIELDER, "club": "Helsingborg", "external_id": "wc26-irq-amir-al-ammari"},
    {"shirt_number": 8, "first_name": "Bashar", "last_name": "Resan", "position": Player.Position.MIDFIELDER, "club": "Qatar SC", "external_id": "wc26-irq-bashar-resan"},
    {"shirt_number": 10, "first_name": "Mohannad", "last_name": "Ali", "position": Player.Position.MIDFIELDER, "club": "Aris Limassol", "external_id": "wc26-irq-mohannad-ali"},
    {"shirt_number": 16, "first_name": "Hussein", "last_name": "Ali", "position": Player.Position.MIDFIELDER, "club": "Al Shorta", "external_id": "wc26-irq-hussein-ali"},
    {"shirt_number": 17, "first_name": "Osama", "last_name": "Rashid", "position": Player.Position.MIDFIELDER, "club": "Vizela", "external_id": "wc26-irq-osama-rashid"},
    {"shirt_number": 18, "first_name": "Safaa", "last_name": "Hadi", "position": Player.Position.MIDFIELDER, "club": "Al Quwa Al Jawiya", "external_id": "wc26-irq-safaa-hadi"},

    {"shirt_number": 7, "first_name": "Aymen", "last_name": "Hussein", "position": Player.Position.FORWARD, "club": "Al Quwa Al Jawiya", "external_id": "wc26-irq-aymen-hussein"},
    {"shirt_number": 9, "first_name": "Alaa", "last_name": "Abdul Zahra", "position": Player.Position.FORWARD, "club": "Al Shorta", "external_id": "wc26-irq-alaa-abdul-zahra"},
    {"shirt_number": 11, "first_name": "Mohammed", "last_name": "Dawood", "position": Player.Position.FORWARD, "club": "Al Zawraa", "external_id": "wc26-irq-mohammed-dawood"},
    {"shirt_number": 19, "first_name": "Ali", "last_name": "Hussein", "position": Player.Position.FORWARD, "club": "Al Talaba", "external_id": "wc26-irq-ali-hussein"},
    {"shirt_number": 20, "first_name": "Mazid", "last_name": "Hameed", "position": Player.Position.FORWARD, "club": "Al Shorta", "external_id": "wc26-irq-mazid-hameed"},
    {"shirt_number": 21, "first_name": "Hussein", "last_name": "Jasim", "position": Player.Position.FORWARD, "club": "Al Naft", "external_id": "wc26-irq-hussein-jasim"},
    {"shirt_number": 22, "first_name": "Mohanad", "last_name": "Kadhim", "position": Player.Position.FORWARD, "club": "Al Karkh", "external_id": "wc26-irq-mohanad-kadhim"},
    {"shirt_number": 24, "first_name": "Ali", "last_name": "Faisal", "position": Player.Position.FORWARD, "club": "Al Minaa", "external_id": "wc26-irq-ali-faisal"},
    {"shirt_number": 25, "first_name": "Saad", "last_name": "Natiq", "position": Player.Position.FORWARD, "club": "Al Quwa Al Jawiya", "external_id": "wc26-irq-saad-natiq"},
    {"shirt_number": 26, "first_name": "Ahmed", "last_name": "Yasin", "position": Player.Position.FORWARD, "club": "AGF", "external_id": "wc26-irq-ahmed-yasin"},
]


NORWAY_PLAYERS = [
    {"shirt_number": 1, "first_name": "Orjan", "last_name": "Nyland", "position": Player.Position.GOALKEEPER, "club": "Sevilla", "external_id": "wc26-nor-orjan-nyland"},
    {"shirt_number": 12, "first_name": "Andre", "last_name": "Hansen", "position": Player.Position.GOALKEEPER, "club": "Rosenborg", "external_id": "wc26-nor-andre-hansen"},
    {"shirt_number": 23, "first_name": "Kristoffer", "last_name": "Klaesson", "position": Player.Position.GOALKEEPER, "club": "Leeds United", "external_id": "wc26-nor-kristoffer-klaesson"},

    {"shirt_number": 2, "first_name": "Marcus", "last_name": "Pedersen", "position": Player.Position.DEFENDER, "club": "Feyenoord", "external_id": "wc26-nor-marcus-pedersen"},
    {"shirt_number": 3, "first_name": "Birger", "last_name": "Meling", "position": Player.Position.DEFENDER, "club": "Rennes", "external_id": "wc26-nor-birger-meling"},
    {"shirt_number": 4, "first_name": "Leo", "last_name": "Ostigard", "position": Player.Position.DEFENDER, "club": "Napoli", "external_id": "wc26-nor-leo-ostigard"},
    {"shirt_number": 5, "first_name": "Kristoffer", "last_name": "Ajer", "position": Player.Position.DEFENDER, "club": "Brentford", "external_id": "wc26-nor-kristoffer-ajer"},
    {"shirt_number": 13, "first_name": "Julian", "last_name": "Ryerson", "position": Player.Position.DEFENDER, "club": "Borussia Dortmund", "external_id": "wc26-nor-julian-ryerson"},
    {"shirt_number": 14, "first_name": "Andreas", "last_name": "Hanche-Olsen", "position": Player.Position.DEFENDER, "club": "Mainz 05", "external_id": "wc26-nor-andreas-hanche-olsen"},
    {"shirt_number": 15, "first_name": "Fredrik", "last_name": "Björkan", "position": Player.Position.DEFENDER, "club": "Bodo/Glimt", "external_id": "wc26-nor-fredrik-bjorkan"},

    {"shirt_number": 6, "first_name": "Martin", "last_name": "Odegaard", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-nor-martin-odegaard"},
    {"shirt_number": 8, "first_name": "Sander", "last_name": "Berge", "position": Player.Position.MIDFIELDER, "club": "Burnley", "external_id": "wc26-nor-sander-berge"},
    {"shirt_number": 10, "first_name": "Patrick", "last_name": "Berg", "position": Player.Position.MIDFIELDER, "club": "Bodo/Glimt", "external_id": "wc26-nor-patrick-berg"},
    {"shirt_number": 16, "first_name": "Ola", "last_name": "Solbakken", "position": Player.Position.MIDFIELDER, "club": "Olympiakos", "external_id": "wc26-nor-ola-solbakken"},
    {"shirt_number": 17, "first_name": "Mathias", "last_name": "Normann", "position": Player.Position.MIDFIELDER, "club": "Al Raed", "external_id": "wc26-nor-mathias-normann"},
    {"shirt_number": 18, "first_name": "Morten", "last_name": "Thorsby", "position": Player.Position.MIDFIELDER, "club": "Genoa", "external_id": "wc26-nor-morten-thorsby"},

    {"shirt_number": 7, "first_name": "Erling", "last_name": "Haaland", "position": Player.Position.FORWARD, "club": "Manchester City", "external_id": "wc26-nor-erling-haaland"},
    {"shirt_number": 9, "first_name": "Alexander", "last_name": "Sorloth", "position": Player.Position.FORWARD, "club": "Villarreal", "external_id": "wc26-nor-alexander-sorloth"},
    {"shirt_number": 11, "first_name": "Ola", "last_name": "Kamara", "position": Player.Position.FORWARD, "club": "DC United", "external_id": "wc26-nor-ola-kamara"},
    {"shirt_number": 19, "first_name": "Jorgen", "last_name": "Strand Larsen", "position": Player.Position.FORWARD, "club": "Celta Vigo", "external_id": "wc26-nor-jorgen-strand-larsen"},
    {"shirt_number": 20, "first_name": "Aron", "last_name": "Donnum", "position": Player.Position.FORWARD, "club": "Standard Liege", "external_id": "wc26-nor-aron-donnum"},
    {"shirt_number": 21, "first_name": "Kristian", "last_name": "Thorstvedt", "position": Player.Position.FORWARD, "club": "Sassuolo", "external_id": "wc26-nor-kristian-thorstvedt"},
    {"shirt_number": 22, "first_name": "Mohamed", "last_name": "Elyounoussi", "position": Player.Position.FORWARD, "club": "Copenhagen", "external_id": "wc26-nor-mohamed-elyounoussi"},
    {"shirt_number": 24, "first_name": "Veton", "last_name": "Berisha", "position": Player.Position.FORWARD, "club": "Viking", "external_id": "wc26-nor-veton-berisha"},
    {"shirt_number": 25, "first_name": "Andreas", "last_name": "Svensson", "position": Player.Position.FORWARD, "club": "Rosenborg", "external_id": "wc26-nor-andreas-svensson"},
    {"shirt_number": 26, "first_name": "Oscar", "last_name": "Bobb", "position": Player.Position.FORWARD, "club": "Manchester City", "external_id": "wc26-nor-oscar-bobb"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo I del Mundial 2026"

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
            france = Team.objects.get(fifa_code="FRA")
            senegal = Team.objects.get(fifa_code="SEN")
            iraq = Team.objects.get(fifa_code="IRQ")
            norway = Team.objects.get(fifa_code="NOR")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo I en la base de datos: {exc}")

        results = []

        results.append(("France", *self.load_players_for_team(france, FRANCE_PLAYERS)))
        results.append(("Senegal", *self.load_players_for_team(senegal, SENEGAL_PLAYERS)))
        results.append(("Iraq", *self.load_players_for_team(iraq, IRAQ_PLAYERS)))
        results.append(("Norway", *self.load_players_for_team(norway, NORWAY_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo I completada."))