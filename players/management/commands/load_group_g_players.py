from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


BELGIUM_PLAYERS = [
    {"shirt_number": 1, "first_name": "Thibaut", "last_name": "Courtois", "position": Player.Position.GOALKEEPER, "club": "Real Madrid", "external_id": "wc26-bel-thibaut-courtois"},
    {"shirt_number": 12, "first_name": "Koen", "last_name": "Casteels", "position": Player.Position.GOALKEEPER, "club": "Al Qadsiah", "external_id": "wc26-bel-koen-casteels"},
    {"shirt_number": 23, "first_name": "Matz", "last_name": "Sels", "position": Player.Position.GOALKEEPER, "club": "Nottingham Forest", "external_id": "wc26-bel-matz-sels"},

    {"shirt_number": 2, "first_name": "Timothy", "last_name": "Castagne", "position": Player.Position.DEFENDER, "club": "Fulham", "external_id": "wc26-bel-timothy-castagne"},
    {"shirt_number": 3, "first_name": "Arthur", "last_name": "Theate", "position": Player.Position.DEFENDER, "club": "Rennes", "external_id": "wc26-bel-arthur-theate"},
    {"shirt_number": 4, "first_name": "Wout", "last_name": "Faes", "position": Player.Position.DEFENDER, "club": "Leicester City", "external_id": "wc26-bel-wout-faes"},
    {"shirt_number": 5, "first_name": "Jan", "last_name": "Vertonghen", "position": Player.Position.DEFENDER, "club": "Anderlecht", "external_id": "wc26-bel-jan-vertonghen"},
    {"shirt_number": 13, "first_name": "Zeno", "last_name": "Debast", "position": Player.Position.DEFENDER, "club": "Sporting CP", "external_id": "wc26-bel-zeno-debast"},
    {"shirt_number": 14, "first_name": "Thomas", "last_name": "Meunier", "position": Player.Position.DEFENDER, "club": "Trabzonspor", "external_id": "wc26-bel-thomas-meunier"},
    {"shirt_number": 15, "first_name": "Amadou", "last_name": "Onana", "position": Player.Position.DEFENDER, "club": "Everton", "external_id": "wc26-bel-amadou-onana"},

    {"shirt_number": 6, "first_name": "Kevin", "last_name": "De Bruyne", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-bel-kevin-de-bruyne"},
    {"shirt_number": 8, "first_name": "Youri", "last_name": "Tielemans", "position": Player.Position.MIDFIELDER, "club": "Aston Villa", "external_id": "wc26-bel-youri-tielemans"},
    {"shirt_number": 10, "first_name": "Yannick", "last_name": "Carrasco", "position": Player.Position.MIDFIELDER, "club": "Al Shabab", "external_id": "wc26-bel-yannick-carrasco"},
    {"shirt_number": 16, "first_name": "Leandro", "last_name": "Trossard", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-bel-leandro-trossard"},
    {"shirt_number": 17, "first_name": "Jeremy", "last_name": "Doku", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-bel-jeremy-doku"},
    {"shirt_number": 18, "first_name": "Orel", "last_name": "Mangala", "position": Player.Position.MIDFIELDER, "club": "Lyon", "external_id": "wc26-bel-orel-mangala"},

    {"shirt_number": 7, "first_name": "Romelu", "last_name": "Lukaku", "position": Player.Position.FORWARD, "club": "Roma", "external_id": "wc26-bel-romelu-lukaku"},
    {"shirt_number": 9, "first_name": "Lois", "last_name": "Openda", "position": Player.Position.FORWARD, "club": "RB Leipzig", "external_id": "wc26-bel-lois-openda"},
    {"shirt_number": 11, "first_name": "Dodi", "last_name": "Lukebakio", "position": Player.Position.FORWARD, "club": "Sevilla", "external_id": "wc26-bel-dodi-lukebakio"},
    {"shirt_number": 19, "first_name": "Charles", "last_name": "De Ketelaere", "position": Player.Position.FORWARD, "club": "Atalanta", "external_id": "wc26-bel-charles-de-ketelaere"},
    {"shirt_number": 20, "first_name": "Johan", "last_name": "Bakayoko", "position": Player.Position.FORWARD, "club": "PSV", "external_id": "wc26-bel-johan-bakayoko"},
    {"shirt_number": 21, "first_name": "Michy", "last_name": "Batshuayi", "position": Player.Position.FORWARD, "club": "Fenerbahce", "external_id": "wc26-bel-michy-batshuayi"},
    {"shirt_number": 22, "first_name": "Noah", "last_name": "Sadiki", "position": Player.Position.FORWARD, "club": "Union SG", "external_id": "wc26-bel-noah-sadiki"},
    {"shirt_number": 24, "first_name": "Thomas", "last_name": "Foket", "position": Player.Position.FORWARD, "club": "Reims", "external_id": "wc26-bel-thomas-foket"},
    {"shirt_number": 25, "first_name": "Yari", "last_name": "Verschaeren", "position": Player.Position.FORWARD, "club": "Anderlecht", "external_id": "wc26-bel-yari-verschaeren"},
    {"shirt_number": 26, "first_name": "Mike", "last_name": "Tresor", "position": Player.Position.FORWARD, "club": "Burnley", "external_id": "wc26-bel-mike-tresor"},
]


EGYPT_PLAYERS = [
    {"shirt_number": 1, "first_name": "Mohamed", "last_name": "El Shenawy", "position": Player.Position.GOALKEEPER, "club": "Al Ahly", "external_id": "wc26-egy-mohamed-el-shenawy"},
    {"shirt_number": 12, "first_name": "Gabaski", "last_name": "", "position": Player.Position.GOALKEEPER, "club": "Zamalek", "external_id": "wc26-egy-gabaski"},
    {"shirt_number": 23, "first_name": "Mahmoud", "last_name": "Gad", "position": Player.Position.GOALKEEPER, "club": "ENPPI", "external_id": "wc26-egy-mahmoud-gad"},

    {"shirt_number": 2, "first_name": "Ahmed", "last_name": "Hegazi", "position": Player.Position.DEFENDER, "club": "Al Ittihad", "external_id": "wc26-egy-ahmed-hegazi"},
    {"shirt_number": 3, "first_name": "Mahmoud", "last_name": "Alaa", "position": Player.Position.DEFENDER, "club": "Zamalek", "external_id": "wc26-egy-mahmoud-alaa"},
    {"shirt_number": 4, "first_name": "Ahmed", "last_name": "Abdelmonem", "position": Player.Position.DEFENDER, "club": "Al Ahly", "external_id": "wc26-egy-ahmed-abdelmonem"},
    {"shirt_number": 5, "first_name": "Omar", "last_name": "Kamal", "position": Player.Position.DEFENDER, "club": "Future FC", "external_id": "wc26-egy-omar-kamal"},
    {"shirt_number": 13, "first_name": "Mohamed", "last_name": "Hamdy", "position": Player.Position.DEFENDER, "club": "Pyramids FC", "external_id": "wc26-egy-mohamed-hamdy"},
    {"shirt_number": 14, "first_name": "Ramadan", "last_name": "Sobhi", "position": Player.Position.DEFENDER, "club": "Pyramids FC", "external_id": "wc26-egy-ramadan-sobhi"},
    {"shirt_number": 15, "first_name": "Mohamed", "last_name": "Hani", "position": Player.Position.DEFENDER, "club": "Al Ahly", "external_id": "wc26-egy-mohamed-hani"},

    {"shirt_number": 6, "first_name": "Tarek", "last_name": "Hamed", "position": Player.Position.MIDFIELDER, "club": "Damac", "external_id": "wc26-egy-tarek-hamed"},
    {"shirt_number": 8, "first_name": "Hamdy", "last_name": "Fathi", "position": Player.Position.MIDFIELDER, "club": "Al Ahli", "external_id": "wc26-egy-hamdy-fathi"},
    {"shirt_number": 10, "first_name": "Mohamed", "last_name": "Salah", "position": Player.Position.MIDFIELDER, "club": "Liverpool", "external_id": "wc26-egy-mohamed-salah"},
    {"shirt_number": 16, "first_name": "Ahmed", "last_name": "El-Fatouh", "position": Player.Position.MIDFIELDER, "club": "Zamalek", "external_id": "wc26-egy-ahmed-el-fatouh"},
    {"shirt_number": 17, "first_name": "Emam", "last_name": "Ashour", "position": Player.Position.MIDFIELDER, "club": "Al Ahly", "external_id": "wc26-egy-emam-ashour"},
    {"shirt_number": 18, "first_name": "Mahmoud", "last_name": "Trezeguet", "position": Player.Position.MIDFIELDER, "club": "Trabzonspor", "external_id": "wc26-egy-trezeguet"},

    {"shirt_number": 7, "first_name": "Mostafa", "last_name": "Mohamed", "position": Player.Position.FORWARD, "club": "Nantes", "external_id": "wc26-egy-mostafa-mohamed"},
    {"shirt_number": 9, "first_name": "Ahmed", "last_name": "Yasser Rayan", "position": Player.Position.FORWARD, "club": "Ceramica Cleopatra", "external_id": "wc26-egy-ahmed-yasser-rayan"},
    {"shirt_number": 11, "first_name": "Mahmoud", "last_name": "Kahraba", "position": Player.Position.FORWARD, "club": "Al Ahly", "external_id": "wc26-egy-mahmoud-kahraba"},
    {"shirt_number": 19, "first_name": "Omar", "last_name": "Marmoush", "position": Player.Position.FORWARD, "club": "Eintracht Frankfurt", "external_id": "wc26-egy-omar-marmoush"},
    {"shirt_number": 20, "first_name": "Hussein", "last_name": "El Shahat", "position": Player.Position.FORWARD, "club": "Al Ahly", "external_id": "wc26-egy-hussein-el-shahat"},
    {"shirt_number": 21, "first_name": "Ahmed", "last_name": "Sayed Zizo", "position": Player.Position.FORWARD, "club": "Zamalek", "external_id": "wc26-egy-ahmed-zizo"},
    {"shirt_number": 22, "first_name": "Mohamed", "last_name": "Sharif", "position": Player.Position.FORWARD, "club": "Al Khaleej", "external_id": "wc26-egy-mohamed-sharif"},
    {"shirt_number": 24, "first_name": "Mostafa", "last_name": "Fathi", "position": Player.Position.FORWARD, "club": "Pyramids FC", "external_id": "wc26-egy-mostafa-fathi"},
    {"shirt_number": 25, "first_name": "Saleh", "last_name": "Gomaa", "position": Player.Position.FORWARD, "club": "Ismaily", "external_id": "wc26-egy-saleh-gomaa"},
    {"shirt_number": 26, "first_name": "Karim", "last_name": "Hafez", "position": Player.Position.FORWARD, "club": "Yeni Malatyaspor", "external_id": "wc26-egy-karim-hafez"},
]


IRAN_PLAYERS = [
    {"shirt_number": 1, "first_name": "Alireza", "last_name": "Beiranvand", "position": Player.Position.GOALKEEPER, "club": "Persepolis", "external_id": "wc26-irn-alireza-beiranvand"},
    {"shirt_number": 12, "first_name": "Payam", "last_name": "Niazmand", "position": Player.Position.GOALKEEPER, "club": "Sepahan", "external_id": "wc26-irn-payam-niazmand"},
    {"shirt_number": 23, "first_name": "Amir", "last_name": "Abedzadeh", "position": Player.Position.GOALKEEPER, "club": "Ponferradina", "external_id": "wc26-irn-amir-abedzadeh"},

    {"shirt_number": 2, "first_name": "Ramin", "last_name": "Rezaeian", "position": Player.Position.DEFENDER, "club": "Sepahan", "external_id": "wc26-irn-ramin-rezaeian"},
    {"shirt_number": 3, "first_name": "Milad", "last_name": "Mohammadi", "position": Player.Position.DEFENDER, "club": "AEK Athens", "external_id": "wc26-irn-milad-mohammadi"},
    {"shirt_number": 4, "first_name": "Hossein", "last_name": "Kanaani", "position": Player.Position.DEFENDER, "club": "Persepolis", "external_id": "wc26-irn-hossein-kanaani"},
    {"shirt_number": 5, "first_name": "Morteza", "last_name": "Pouraliganji", "position": Player.Position.DEFENDER, "club": "Persepolis", "external_id": "wc26-irn-morteza-pouraliganji"},
    {"shirt_number": 13, "first_name": "Sadegh", "last_name": "Moharrami", "position": Player.Position.DEFENDER, "club": "Dinamo Zagreb", "external_id": "wc26-irn-sadegh-moharrami"},
    {"shirt_number": 14, "first_name": "Shoja", "last_name": "Khalilzadeh", "position": Player.Position.DEFENDER, "club": "Al Ahli", "external_id": "wc26-irn-shoja-khalilzadeh"},
    {"shirt_number": 15, "first_name": "Daniel", "last_name": "Esmaeilifar", "position": Player.Position.DEFENDER, "club": "Sepahan", "external_id": "wc26-irn-daniel-esmaeilifar"},

    {"shirt_number": 6, "first_name": "Saeid", "last_name": "Ezatolahi", "position": Player.Position.MIDFIELDER, "club": "Vejle", "external_id": "wc26-irn-saeid-ezatolahi"},
    {"shirt_number": 8, "first_name": "Ahmad", "last_name": "Nourollahi", "position": Player.Position.MIDFIELDER, "club": "Al Wahda", "external_id": "wc26-irn-ahmad-nourollahi"},
    {"shirt_number": 10, "first_name": "Sardar", "last_name": "Azmoun", "position": Player.Position.MIDFIELDER, "club": "Roma", "external_id": "wc26-irn-sardar-azmoun"},
    {"shirt_number": 16, "first_name": "Alireza", "last_name": "Jahanbakhsh", "position": Player.Position.MIDFIELDER, "club": "Feyenoord", "external_id": "wc26-irn-alireza-jahanbakhsh"},
    {"shirt_number": 17, "first_name": "Mehdi", "last_name": "Torabi", "position": Player.Position.MIDFIELDER, "club": "Persepolis", "external_id": "wc26-irn-mehdi-torabi"},
    {"shirt_number": 18, "first_name": "Ali", "last_name": "Gholizadeh", "position": Player.Position.MIDFIELDER, "club": "Legia Warsaw", "external_id": "wc26-irn-ali-gholizadeh"},

    {"shirt_number": 7, "first_name": "Mehdi", "last_name": "Taremi", "position": Player.Position.FORWARD, "club": "Porto", "external_id": "wc26-irn-mehdi-taremi"},
    {"shirt_number": 9, "first_name": "Karim", "last_name": "Ansarifard", "position": Player.Position.FORWARD, "club": "Omonia", "external_id": "wc26-irn-karim-ansarifard"},
    {"shirt_number": 11, "first_name": "Allahyar", "last_name": "Sayyadmanesh", "position": Player.Position.FORWARD, "club": "Hull City", "external_id": "wc26-irn-allahyar-sayyadmanesh"},
    {"shirt_number": 19, "first_name": "Reza", "last_name": "Shekari", "position": Player.Position.FORWARD, "club": "Gol Gohar", "external_id": "wc26-irn-reza-shekari"},
    {"shirt_number": 20, "first_name": "Omid", "last_name": "Ebrahimi", "position": Player.Position.FORWARD, "club": "Al Wakrah", "external_id": "wc26-irn-omid-ebrahimi"},
    {"shirt_number": 21, "first_name": "Shahriar", "last_name": "Moghanlou", "position": Player.Position.FORWARD, "club": "Sepahan", "external_id": "wc26-irn-shahriar-moghanlou"},
    {"shirt_number": 22, "first_name": "Mohammad", "last_name": "Karimi", "position": Player.Position.FORWARD, "club": "Sepahan", "external_id": "wc26-irn-mohammad-karimi"},
    {"shirt_number": 24, "first_name": "Arman", "last_name": "Ramezani", "position": Player.Position.FORWARD, "club": "Esteghlal", "external_id": "wc26-irn-arman-ramezani"},
    {"shirt_number": 25, "first_name": "Reza", "last_name": "Ghoochannejhad", "position": Player.Position.FORWARD, "club": "PEC Zwolle", "external_id": "wc26-irn-reza-ghoochannejhad"},
    {"shirt_number": 26, "first_name": "Ali", "last_name": "Alipour", "position": Player.Position.FORWARD, "club": "Gil Vicente", "external_id": "wc26-irn-ali-alipour"},
]


NEW_ZEALAND_PLAYERS = [
    {"shirt_number": 1, "first_name": "Oli", "last_name": "Sail", "position": Player.Position.GOALKEEPER, "club": "Perth Glory", "external_id": "wc26-nzl-oli-sail"},
    {"shirt_number": 12, "first_name": "Stefan", "last_name": "Marinovic", "position": Player.Position.GOALKEEPER, "club": "Hapoel Tel Aviv", "external_id": "wc26-nzl-stefan-marinovic"},
    {"shirt_number": 23, "first_name": "Michael", "last_name": "Woud", "position": Player.Position.GOALKEEPER, "club": "Kyoto Sanga", "external_id": "wc26-nzl-michael-woud"},

    {"shirt_number": 2, "first_name": "Liberato", "last_name": "Cacace", "position": Player.Position.DEFENDER, "club": "Empoli", "external_id": "wc26-nzl-liberato-cacace"},
    {"shirt_number": 3, "first_name": "Nando", "last_name": "Pijnaker", "position": Player.Position.DEFENDER, "club": "SJK", "external_id": "wc26-nzl-nando-pijnaker"},
    {"shirt_number": 4, "first_name": "Winston", "last_name": "Reid", "position": Player.Position.DEFENDER, "club": "Auckland City", "external_id": "wc26-nzl-winston-reid"},
    {"shirt_number": 5, "first_name": "Tommy", "last_name": "Smith", "position": Player.Position.DEFENDER, "club": "Colchester United", "external_id": "wc26-nzl-tommy-smith"},
    {"shirt_number": 13, "first_name": "Kelvin", "last_name": "Khalaf", "position": Player.Position.DEFENDER, "club": "Wellington Phoenix", "external_id": "wc26-nzl-kelvin-khalaf"},
    {"shirt_number": 14, "first_name": "Dane", "last_name": "Ingham", "position": Player.Position.DEFENDER, "club": "Newcastle Jets", "external_id": "wc26-nzl-dane-ingham"},
    {"shirt_number": 15, "first_name": "Callan", "last_name": "Elliot", "position": Player.Position.DEFENDER, "club": "Wellington Phoenix", "external_id": "wc26-nzl-callan-elliot"},

    {"shirt_number": 6, "first_name": "Joe", "last_name": "Bell", "position": Player.Position.MIDFIELDER, "club": "Brondby", "external_id": "wc26-nzl-joe-bell"},
    {"shirt_number": 8, "first_name": "Matt", "last_name": "Garbet", "position": Player.Position.MIDFIELDER, "club": "Torino", "external_id": "wc26-nzl-matt-garbet"},
    {"shirt_number": 10, "first_name": "Sarpreet", "last_name": "Singh", "position": Player.Position.MIDFIELDER, "club": "Brondby", "external_id": "wc26-nzl-sarpreet-singh"},
    {"shirt_number": 16, "first_name": "Clayton", "last_name": "Lewis", "position": Player.Position.MIDFIELDER, "club": "Macarthur FC", "external_id": "wc26-nzl-clayton-lewis"},
    {"shirt_number": 17, "first_name": "Marko", "last_name": "Stamenic", "position": Player.Position.MIDFIELDER, "club": "Red Star Belgrade", "external_id": "wc26-nzl-marko-stamenic"},
    {"shirt_number": 18, "first_name": "Callum", "last_name": "McCowatt", "position": Player.Position.MIDFIELDER, "club": "Silkeborg IF", "external_id": "wc26-nzl-callum-mccowatt"},

    {"shirt_number": 7, "first_name": "Chris", "last_name": "Wood", "position": Player.Position.FORWARD, "club": "Nottingham Forest", "external_id": "wc26-nzl-chris-wood"},
    {"shirt_number": 9, "first_name": "Ben", "last_name": "Waine", "position": Player.Position.FORWARD, "club": "Plymouth Argyle", "external_id": "wc26-nzl-ben-waine"},
    {"shirt_number": 11, "first_name": "Andre", "last_name": "de Jong", "position": Player.Position.FORWARD, "club": "Royal AM", "external_id": "wc26-nzl-andre-de-jong"},
    {"shirt_number": 19, "first_name": "Kosta", "last_name": "Barbarouses", "position": Player.Position.FORWARD, "club": "Wellington Phoenix", "external_id": "wc26-nzl-kosta-barbarouses"},
    {"shirt_number": 20, "first_name": "Marco", "last_name": "Rojas", "position": Player.Position.FORWARD, "club": "Wellington Phoenix", "external_id": "wc26-nzl-marco-rojas"},
    {"shirt_number": 21, "first_name": "Logan", "last_name": "Rogerson", "position": Player.Position.FORWARD, "club": "HJK Helsinki", "external_id": "wc26-nzl-logan-rogerson"},
    {"shirt_number": 22, "first_name": "Walter", "last_name": "Gael Sandoval", "position": Player.Position.FORWARD, "club": "Wellington Phoenix", "external_id": "wc26-nzl-walter-sandoval"},
    {"shirt_number": 24, "first_name": "Alex", "last_name": "Greive", "position": Player.Position.FORWARD, "club": "St. Mirren", "external_id": "wc26-nzl-alex-greive"},
    {"shirt_number": 25, "first_name": "Max", "last_name": "Mata", "position": Player.Position.FORWARD, "club": "Shrewsbury Town", "external_id": "wc26-nzl-max-mata"},
    {"shirt_number": 26, "first_name": "Eli", "last_name": "Just", "position": Player.Position.FORWARD, "club": "Vllaznia", "external_id": "wc26-nzl-eli-just"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo G del Mundial 2026"

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
            belgium = Team.objects.get(fifa_code="BEL")
            egypt = Team.objects.get(fifa_code="EGY")
            iran = Team.objects.get(fifa_code="IRN")
            new_zealand = Team.objects.get(fifa_code="NZL")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo G en la base de datos: {exc}")

        results = []

        results.append(("Belgium", *self.load_players_for_team(belgium, BELGIUM_PLAYERS)))
        results.append(("Egypt", *self.load_players_for_team(egypt, EGYPT_PLAYERS)))
        results.append(("Iran", *self.load_players_for_team(iran, IRAN_PLAYERS)))
        results.append(("New Zealand", *self.load_players_for_team(new_zealand, NEW_ZEALAND_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo G completada."))