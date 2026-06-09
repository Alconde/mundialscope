from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


NETHERLANDS_PLAYERS = [
    {"shirt_number": 1, "first_name": "Justin", "last_name": "Bijlow", "position": Player.Position.GOALKEEPER, "club": "Feyenoord", "external_id": "wc26-ned-justin-bijlow"},
    {"shirt_number": 12, "first_name": "Bart", "last_name": "Verbruggen", "position": Player.Position.GOALKEEPER, "club": "Brighton", "external_id": "wc26-ned-bart-verbruggen"},
    {"shirt_number": 23, "first_name": "Mark", "last_name": "Flekken", "position": Player.Position.GOALKEEPER, "club": "Brentford", "external_id": "wc26-ned-mark-flekken"},

    {"shirt_number": 2, "first_name": "Denzel", "last_name": "Dumfries", "position": Player.Position.DEFENDER, "club": "Inter Milan", "external_id": "wc26-ned-denzel-dumfries"},
    {"shirt_number": 3, "first_name": "Matthijs", "last_name": "de Ligt", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-ned-matthijs-de-ligt"},
    {"shirt_number": 4, "first_name": "Virgil", "last_name": "van Dijk", "position": Player.Position.DEFENDER, "club": "Liverpool", "external_id": "wc26-ned-virgil-van-dijk"},
    {"shirt_number": 5, "first_name": "Nathan", "last_name": "Ake", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-ned-nathan-ake"},
    {"shirt_number": 13, "first_name": "Jurriën", "last_name": "Timber", "position": Player.Position.DEFENDER, "club": "Arsenal", "external_id": "wc26-ned-jurrien-timber"},
    {"shirt_number": 14, "first_name": "Mickey", "last_name": "van de Ven", "position": Player.Position.DEFENDER, "club": "Tottenham Hotspur", "external_id": "wc26-ned-mickey-van-de-ven"},
    {"shirt_number": 15, "first_name": "Tyrell", "last_name": "Malacia", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-ned-tyrell-malacia"},

    {"shirt_number": 6, "first_name": "Frenkie", "last_name": "de Jong", "position": Player.Position.MIDFIELDER, "club": "Barcelona", "external_id": "wc26-ned-frenkie-de-jong"},
    {"shirt_number": 8, "first_name": "Teun", "last_name": "Koopmeiners", "position": Player.Position.MIDFIELDER, "club": "Atalanta", "external_id": "wc26-ned-teun-koopmeiners"},
    {"shirt_number": 10, "first_name": "Xavi", "last_name": "Simons", "position": Player.Position.MIDFIELDER, "club": "RB Leipzig", "external_id": "wc26-ned-xavi-simons"},
    {"shirt_number": 16, "first_name": "Marten", "last_name": "de Roon", "position": Player.Position.MIDFIELDER, "club": "Atalanta", "external_id": "wc26-ned-marten-de-roon"},
    {"shirt_number": 17, "first_name": "Joey", "last_name": "Veerman", "position": Player.Position.MIDFIELDER, "club": "PSV", "external_id": "wc26-ned-joey-veerman"},
    {"shirt_number": 18, "first_name": "Jerdy", "last_name": "Schouten", "position": Player.Position.MIDFIELDER, "club": "PSV", "external_id": "wc26-ned-jerdy-schouten"},

    {"shirt_number": 7, "first_name": "Steven", "last_name": "Bergwijn", "position": Player.Position.FORWARD, "club": "Ajax", "external_id": "wc26-ned-steven-bergwijn"},
    {"shirt_number": 9, "first_name": "Wout", "last_name": "Weghorst", "position": Player.Position.FORWARD, "club": "Hoffenheim", "external_id": "wc26-ned-wout-weghorst"},
    {"shirt_number": 11, "first_name": "Memphis", "last_name": "Depay", "position": Player.Position.FORWARD, "club": "Atletico Madrid", "external_id": "wc26-ned-memphis-depay"},
    {"shirt_number": 19, "first_name": "Cody", "last_name": "Gakpo", "position": Player.Position.FORWARD, "club": "Liverpool", "external_id": "wc26-ned-cody-gakpo"},
    {"shirt_number": 20, "first_name": "Donyell", "last_name": "Malen", "position": Player.Position.FORWARD, "club": "Borussia Dortmund", "external_id": "wc26-ned-donyell-malen"},
    {"shirt_number": 21, "first_name": "Brian", "last_name": "Brobbey", "position": Player.Position.FORWARD, "club": "Ajax", "external_id": "wc26-ned-brian-brobbey"},
    {"shirt_number": 22, "first_name": "Noa", "last_name": "Lang", "position": Player.Position.FORWARD, "club": "PSV", "external_id": "wc26-ned-noa-lang"},
    {"shirt_number": 24, "first_name": "Arnaut", "last_name": "Danjuma", "position": Player.Position.FORWARD, "club": "Everton", "external_id": "wc26-ned-arnaut-danjuma"},
    {"shirt_number": 25, "first_name": "Thijs", "last_name": "Dallinga", "position": Player.Position.FORWARD, "club": "Toulouse", "external_id": "wc26-ned-thijs-dallinga"},
    {"shirt_number": 26, "first_name": "Joshua", "last_name": "Zirkzee", "position": Player.Position.FORWARD, "club": "Bologna", "external_id": "wc26-ned-joshua-zirkzee"},
]


JAPAN_PLAYERS = [
    {"shirt_number": 1, "first_name": "Daniel", "last_name": "Schmidt", "position": Player.Position.GOALKEEPER, "club": "Sint-Truiden", "external_id": "wc26-jpn-daniel-schmidt"},
    {"shirt_number": 12, "first_name": "Kosuke", "last_name": "Nakamura", "position": Player.Position.GOALKEEPER, "club": "Portimonense", "external_id": "wc26-jpn-kosuke-nakamura"},
    {"shirt_number": 23, "first_name": "Keisuke", "last_name": "Osako", "position": Player.Position.GOALKEEPER, "club": "Sanfrecce Hiroshima", "external_id": "wc26-jpn-keisuke-osako"},

    {"shirt_number": 2, "first_name": "Hiroki", "last_name": "Sakai", "position": Player.Position.DEFENDER, "club": "Urawa Red Diamonds", "external_id": "wc26-jpn-hiroki-sakai"},
    {"shirt_number": 3, "first_name": "Takehiro", "last_name": "Tomiyasu", "position": Player.Position.DEFENDER, "club": "Arsenal", "external_id": "wc26-jpn-takehiro-tomiyasu"},
    {"shirt_number": 4, "first_name": "Ko", "last_name": "Itakura", "position": Player.Position.DEFENDER, "club": "Borussia Monchengladbach", "external_id": "wc26-jpn-ko-itakura"},
    {"shirt_number": 5, "first_name": "Maya", "last_name": "Yoshida", "position": Player.Position.DEFENDER, "club": "LA Galaxy", "external_id": "wc26-jpn-maya-yoshida"},
    {"shirt_number": 13, "first_name": "Yuta", "last_name": "Nakayama", "position": Player.Position.DEFENDER, "club": "Huddersfield Town", "external_id": "wc26-jpn-yuta-nakayama"},
    {"shirt_number": 14, "first_name": "Hiroki", "last_name": "Ito", "position": Player.Position.DEFENDER, "club": "Stuttgart", "external_id": "wc26-jpn-hiroki-ito"},
    {"shirt_number": 15, "first_name": "Sho", "last_name": "Sasaki", "position": Player.Position.DEFENDER, "club": "Sanfrecce Hiroshima", "external_id": "wc26-jpn-sho-sasaki"},

    {"shirt_number": 6, "first_name": "Wataru", "last_name": "Endo", "position": Player.Position.MIDFIELDER, "club": "Liverpool", "external_id": "wc26-jpn-wataru-endo"},
    {"shirt_number": 8, "first_name": "Ao", "last_name": "Tanaka", "position": Player.Position.MIDFIELDER, "club": "Fortuna Dusseldorf", "external_id": "wc26-jpn-ao-tanaka"},
    {"shirt_number": 10, "first_name": "Daichi", "last_name": "Kamada", "position": Player.Position.MIDFIELDER, "club": "Lazio", "external_id": "wc26-jpn-daichi-kamada"},
    {"shirt_number": 16, "first_name": "Hidemasa", "last_name": "Morita", "position": Player.Position.MIDFIELDER, "club": "Sporting CP", "external_id": "wc26-jpn-hidemasa-morita"},
    {"shirt_number": 17, "first_name": "Ritsu", "last_name": "Doan", "position": Player.Position.MIDFIELDER, "club": "Freiburg", "external_id": "wc26-jpn-ritsu-doan"},
    {"shirt_number": 18, "first_name": "Takumi", "last_name": "Minamino", "position": Player.Position.MIDFIELDER, "club": "Monaco", "external_id": "wc26-jpn-takumi-minamino"},

    {"shirt_number": 7, "first_name": "Takefusa", "last_name": "Kubo", "position": Player.Position.FORWARD, "club": "Real Sociedad", "external_id": "wc26-jpn-takefusa-kubo"},
    {"shirt_number": 9, "first_name": "Ayase", "last_name": "Ueda", "position": Player.Position.FORWARD, "club": "Feyenoord", "external_id": "wc26-jpn-ayase-ueda"},
    {"shirt_number": 11, "first_name": "Kaoru", "last_name": "Mitoma", "position": Player.Position.FORWARD, "club": "Brighton", "external_id": "wc26-jpn-kaoru-mitoma"},
    {"shirt_number": 19, "first_name": "Daizen", "last_name": "Maeda", "position": Player.Position.FORWARD, "club": "Celtic", "external_id": "wc26-jpn-daizen-maeda"},
    {"shirt_number": 20, "first_name": "Shuto", "last_name": "Machino", "position": Player.Position.FORWARD, "club": "Shonan Bellmare", "external_id": "wc26-jpn-shuto-machino"},
    {"shirt_number": 21, "first_name": "Kyogo", "last_name": "Furuhashi", "position": Player.Position.FORWARD, "club": "Celtic", "external_id": "wc26-jpn-kyogo-furuhashi"},
    {"shirt_number": 22, "first_name": "Hiroki", "last_name": "Abe", "position": Player.Position.FORWARD, "club": "FC Tokyo", "external_id": "wc26-jpn-hiroki-abe"},
    {"shirt_number": 24, "first_name": "Keito", "last_name": "Nakamura", "position": Player.Position.FORWARD, "club": "LASK", "external_id": "wc26-jpn-keito-nakamura"},
    {"shirt_number": 25, "first_name": "Yukinari", "last_name": "Sugawara", "position": Player.Position.FORWARD, "club": "AZ Alkmaar", "external_id": "wc26-jpn-yukinari-sugawara"},
    {"shirt_number": 26, "first_name": "Shion", "last_name": "Homma", "position": Player.Position.FORWARD, "club": "Albirex Niigata", "external_id": "wc26-jpn-shion-homma"},
]


SWEDEN_PLAYERS = [
    {"shirt_number": 1, "first_name": "Robin", "last_name": "Olsen", "position": Player.Position.GOALKEEPER, "club": "Aston Villa", "external_id": "wc26-swe-robin-olsen"},
    {"shirt_number": 12, "first_name": "Kristoffer", "last_name": "Nordfeldt", "position": Player.Position.GOALKEEPER, "club": "AIK", "external_id": "wc26-swe-kristoffer-nordfeldt"},
    {"shirt_number": 23, "first_name": "Viktor", "last_name": "Johansson", "position": Player.Position.GOALKEEPER, "club": "Rotherham United", "external_id": "wc26-swe-viktor-johansson"},

    {"shirt_number": 2, "first_name": "Emil", "last_name": "Krafth", "position": Player.Position.DEFENDER, "club": "Newcastle United", "external_id": "wc26-swe-emil-krafth"},
    {"shirt_number": 3, "first_name": "Victor", "last_name": "Lindelöf", "position": Player.Position.DEFENDER, "club": "Manchester United", "external_id": "wc26-swe-victor-lindelof"},
    {"shirt_number": 4, "first_name": "Hjalmar", "last_name": "Ekdal", "position": Player.Position.DEFENDER, "club": "Burnley", "external_id": "wc26-swe-hjalmar-ekdal"},
    {"shirt_number": 5, "first_name": "Ludwig", "last_name": "Augustinsson", "position": Player.Position.DEFENDER, "club": "Anderlecht", "external_id": "wc26-swe-ludwig-augustinsson"},
    {"shirt_number": 13, "first_name": "Gabriel", "last_name": "Gudmundsson", "position": Player.Position.DEFENDER, "club": "Lille", "external_id": "wc26-swe-gabriel-gudmundsson"},
    {"shirt_number": 14, "first_name": "Joakim", "last_name": "Nilsson", "position": Player.Position.DEFENDER, "club": "St. Pauli", "external_id": "wc26-swe-joakim-nilsson"},
    {"shirt_number": 15, "first_name": "Victor", "last_name": "Dahl", "position": Player.Position.DEFENDER, "club": "Malmo FF", "external_id": "wc26-swe-victor-dahl"},

    {"shirt_number": 6, "first_name": "Albin", "last_name": "Ekdal", "position": Player.Position.MIDFIELDER, "club": "Spezia", "external_id": "wc26-swe-albin-ekdal"},
    {"shirt_number": 8, "first_name": "Mattias", "last_name": "Svanberg", "position": Player.Position.MIDFIELDER, "club": "Wolfsburg", "external_id": "wc26-swe-mattias-svanberg"},
    {"shirt_number": 10, "first_name": "Emil", "last_name": "Forsberg", "position": Player.Position.MIDFIELDER, "club": "New York Red Bulls", "external_id": "wc26-swe-emil-forsberg"},
    {"shirt_number": 16, "first_name": "Jens", "last_name": "Cajuste", "position": Player.Position.MIDFIELDER, "club": "Napoli", "external_id": "wc26-swe-jens-cajuste"},
    {"shirt_number": 17, "first_name": "Kristoffer", "last_name": "Olsson", "position": Player.Position.MIDFIELDER, "club": "Midtjylland", "external_id": "wc26-swe-kristoffer-olsson"},
    {"shirt_number": 18, "first_name": "Samuel", "last_name": "Gustafson", "position": Player.Position.MIDFIELDER, "club": "BK Hacken", "external_id": "wc26-swe-samuel-gustafson"},

    {"shirt_number": 7, "first_name": "Dejan", "last_name": "Kulusevski", "position": Player.Position.FORWARD, "club": "Tottenham Hotspur", "external_id": "wc26-swe-dejan-kulusevski"},
    {"shirt_number": 9, "first_name": "Alexander", "last_name": "Isak", "position": Player.Position.FORWARD, "club": "Newcastle United", "external_id": "wc26-swe-alexander-isak"},
    {"shirt_number": 11, "first_name": "Anthony", "last_name": "Elanga", "position": Player.Position.FORWARD, "club": "Nottingham Forest", "external_id": "wc26-swe-anthony-elanga"},
    {"shirt_number": 19, "first_name": "Viktor", "last_name": "Gyökeres", "position": Player.Position.FORWARD, "club": "Sporting CP", "external_id": "wc26-swe-viktor-gyokeres"},
    {"shirt_number": 20, "first_name": "Jesper", "last_name": "Karlsson", "position": Player.Position.FORWARD, "club": "Bologna", "external_id": "wc26-swe-jesper-karlsson"},
    {"shirt_number": 21, "first_name": "Robin", "last_name": "Quaison", "position": Player.Position.FORWARD, "club": "Al Ettifaq", "external_id": "wc26-swe-robin-quaison"},
    {"shirt_number": 22, "first_name": "Zlatan", "last_name": "Ibrahimovic Jr", "position": Player.Position.FORWARD, "club": "Malmo FF", "external_id": "wc26-swe-zlatan-ibrahimovic-jr"},
    {"shirt_number": 24, "first_name": "Patrik", "last_name": "Karlsson", "position": Player.Position.FORWARD, "club": "IFK Goteborg", "external_id": "wc26-swe-patrik-karlsson"},
    {"shirt_number": 25, "first_name": "Benjamin", "last_name": "Nygren", "position": Player.Position.FORWARD, "club": "Genk", "external_id": "wc26-swe-benjamin-nygren"},
    {"shirt_number": 26, "first_name": "Isac", "last_name": "Lidberg", "position": Player.Position.FORWARD, "club": "Go Ahead Eagles", "external_id": "wc26-swe-isac-lidberg"},
]


TUNISIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Aymen", "last_name": "Dahmen", "position": Player.Position.GOALKEEPER, "club": "Rennes", "external_id": "wc26-tun-aymen-dahmen"},
    {"shirt_number": 12, "first_name": "Bechir", "last_name": "Ben Said", "position": Player.Position.GOALKEEPER, "club": "US Monastir", "external_id": "wc26-tun-bechir-ben-said"},
    {"shirt_number": 23, "first_name": "Ali", "last_name": "Jelassi", "position": Player.Position.GOALKEEPER, "club": "Esperance", "external_id": "wc26-tun-ali-jelassi"},

    {"shirt_number": 2, "first_name": "Mohamed", "last_name": "Drager", "position": Player.Position.DEFENDER, "club": "Luzern", "external_id": "wc26-tun-mohamed-drager"},
    {"shirt_number": 3, "first_name": "Montassar", "last_name": "Talbi", "position": Player.Position.DEFENDER, "club": "Lorient", "external_id": "wc26-tun-montassar-talbi"},
    {"shirt_number": 4, "first_name": "Dylan", "last_name": "Bronn", "position": Player.Position.DEFENDER, "club": "Salernitana", "external_id": "wc26-tun-dylan-bronn"},
    {"shirt_number": 5, "first_name": "Ali", "last_name": "Maaloul", "position": Player.Position.DEFENDER, "club": "Al Ahly", "external_id": "wc26-tun-ali-maaloul"},
    {"shirt_number": 13, "first_name": "Nader", "last_name": "Ghandri", "position": Player.Position.DEFENDER, "club": "Club Africain", "external_id": "wc26-tun-nader-ghandri"},
    {"shirt_number": 14, "first_name": "Wajdi", "last_name": "Kechrida", "position": Player.Position.DEFENDER, "club": "Atromitos", "external_id": "wc26-tun-wajdi-kechrida"},
    {"shirt_number": 15, "first_name": "Mohamed", "last_name": "Ali Ben Romdhane", "position": Player.Position.DEFENDER, "club": "Ferencvaros", "external_id": "wc26-tun-mohamed-ali-ben-romdhane"},

    {"shirt_number": 6, "first_name": "Ellyes", "last_name": "Skhiri", "position": Player.Position.MIDFIELDER, "club": "Eintracht Frankfurt", "external_id": "wc26-tun-ellyes-skhiri"},
    {"shirt_number": 8, "first_name": "Aissa", "last_name": "Laidouni", "position": Player.Position.MIDFIELDER, "club": "Union Berlin", "external_id": "wc26-tun-aissa-laidouni"},
    {"shirt_number": 10, "first_name": "Youssef", "last_name": "Msakni", "position": Player.Position.MIDFIELDER, "club": "Al Arabi", "external_id": "wc26-tun-youssef-msakni"},
    {"shirt_number": 16, "first_name": "Hannibal", "last_name": "Mejbri", "position": Player.Position.MIDFIELDER, "club": "Sevilla", "external_id": "wc26-tun-hannibal-mejbri"},
    {"shirt_number": 17, "first_name": "Ferjani", "last_name": "Sassi", "position": Player.Position.MIDFIELDER, "club": "Al Duhail", "external_id": "wc26-tun-ferjani-sassi"},
    {"shirt_number": 18, "first_name": "Mohamed", "last_name": "Ben Slimane", "position": Player.Position.MIDFIELDER, "club": "Brondby", "external_id": "wc26-tun-mohamed-ben-slimane"},

    {"shirt_number": 7, "first_name": "Wahbi", "last_name": "Khazri", "position": Player.Position.FORWARD, "club": "Montpellier", "external_id": "wc26-tun-wahbi-khazri"},
    {"shirt_number": 9, "first_name": "Seifeddine", "last_name": "Jaziri", "position": Player.Position.FORWARD, "club": "Zamalek", "external_id": "wc26-tun-seifeddine-jaziri"},
    {"shirt_number": 11, "first_name": "Naïm", "last_name": "Sliti", "position": Player.Position.FORWARD, "club": "Al Ahli", "external_id": "wc26-tun-naim-sliti"},
    {"shirt_number": 19, "first_name": "Anis", "last_name": "Ben Slimane", "position": Player.Position.FORWARD, "club": "Sheffield United", "external_id": "wc26-tun-anis-ben-slimane"},
    {"shirt_number": 20, "first_name": "Issam", "last_name": "Jebali", "position": Player.Position.FORWARD, "club": "Gamba Osaka", "external_id": "wc26-tun-issam-jebali"},
    {"shirt_number": 21, "first_name": "Haythem", "last_name": "Jouini", "position": Player.Position.FORWARD, "club": "Kuwait SC", "external_id": "wc26-tun-haythem-jouini"},
    {"shirt_number": 22, "first_name": "Saif", "last_name": "Ghezal", "position": Player.Position.FORWARD, "club": "Esperance", "external_id": "wc26-tun-saif-ghezal"},
    {"shirt_number": 24, "first_name": "Ali", "last_name": "Houni", "position": Player.Position.FORWARD, "club": "Al Ahli Tripoli", "external_id": "wc26-tun-ali-houni"},
    {"shirt_number": 25, "first_name": "Yassine", "last_name": "Chikhaoui", "position": Player.Position.FORWARD, "club": "Etoile Sahel", "external_id": "wc26-tun-yassine-chikhaoui"},
    {"shirt_number": 26, "first_name": "Khalil", "last_name": "Khelifi", "position": Player.Position.FORWARD, "club": "Club Africain", "external_id": "wc26-tun-khalil-khelifi"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo F del Mundial 2026"

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
            netherlands = Team.objects.get(fifa_code="NED")
            japan = Team.objects.get(fifa_code="JPN")
            sweden = Team.objects.get(fifa_code="SWE")
            tunisia = Team.objects.get(fifa_code="TUN")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo F en la base de datos: {exc}")

        results = []

        results.append(("Netherlands", *self.load_players_for_team(netherlands, NETHERLANDS_PLAYERS)))
        results.append(("Japan", *self.load_players_for_team(japan, JAPAN_PLAYERS)))
        results.append(("Sweden", *self.load_players_for_team(sweden, SWEDEN_PLAYERS)))
        results.append(("Tunisia", *self.load_players_for_team(tunisia, TUNISIA_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo F completada."))