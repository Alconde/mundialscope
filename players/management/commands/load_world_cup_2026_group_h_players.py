from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


SPAIN_PLAYERS = [
    {"shirt_number": 1, "first_name": "David", "last_name": "Raya", "position": Player.Position.GOALKEEPER, "club": "Arsenal", "external_id": "wc26-esp-david-raya"},
    {"shirt_number": 13, "first_name": "Joan", "last_name": "Garcia", "position": Player.Position.GOALKEEPER, "club": "Barcelona", "external_id": "wc26-esp-joan-garcia"},
    {"shirt_number": 23, "first_name": "Unai", "last_name": "Simon", "position": Player.Position.GOALKEEPER, "club": "Athletic Club", "external_id": "wc26-esp-unai-simon"},

    {"shirt_number": 2, "first_name": "Marc", "last_name": "Pubill", "position": Player.Position.DEFENDER, "club": "Atletico Madrid", "external_id": "wc26-esp-marc-pubill"},
    {"shirt_number": 3, "first_name": "Alejandro", "last_name": "Grimaldo", "position": Player.Position.DEFENDER, "club": "Bayer Leverkusen", "external_id": "wc26-esp-alejandro-grimaldo"},
    {"shirt_number": 4, "first_name": "Eric", "last_name": "Garcia", "position": Player.Position.DEFENDER, "club": "Barcelona", "external_id": "wc26-esp-eric-garcia"},
    {"shirt_number": 5, "first_name": "Marcos", "last_name": "Llorente", "position": Player.Position.DEFENDER, "club": "Atletico Madrid", "external_id": "wc26-esp-marcos-llorente"},
    {"shirt_number": 12, "first_name": "Pedro", "last_name": "Porro", "position": Player.Position.DEFENDER, "club": "Tottenham Hotspur", "external_id": "wc26-esp-pedro-porro"},
    {"shirt_number": 14, "first_name": "Aymeric", "last_name": "Laporte", "position": Player.Position.DEFENDER, "club": "Athletic Club", "external_id": "wc26-esp-aymeric-laporte"},
    {"shirt_number": 22, "first_name": "Pau", "last_name": "Cubarsi", "position": Player.Position.DEFENDER, "club": "Barcelona", "external_id": "wc26-esp-pau-cubarsi"},
    {"shirt_number": 24, "first_name": "Marc", "last_name": "Cucurella", "position": Player.Position.DEFENDER, "club": "Chelsea", "external_id": "wc26-esp-marc-cucurella"},

    {"shirt_number": 6, "first_name": "Mikel", "last_name": "Merino", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-esp-mikel-merino"},
    {"shirt_number": 8, "first_name": "Fabian", "last_name": "Ruiz", "position": Player.Position.MIDFIELDER, "club": "Paris Saint-Germain", "external_id": "wc26-esp-fabian-ruiz"},
    {"shirt_number": 9, "first_name": "Gavi", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Barcelona", "external_id": "wc26-esp-gavi"},
    {"shirt_number": 10, "first_name": "Dani", "last_name": "Olmo", "position": Player.Position.MIDFIELDER, "club": "Barcelona", "external_id": "wc26-esp-dani-olmo"},
    {"shirt_number": 16, "first_name": "Rodri", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Manchester City", "external_id": "wc26-esp-rodri"},
    {"shirt_number": 18, "first_name": "Martin", "last_name": "Zubimendi", "position": Player.Position.MIDFIELDER, "club": "Arsenal", "external_id": "wc26-esp-martin-zubimendi"},
    {"shirt_number": 20, "first_name": "Pedri", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Barcelona", "external_id": "wc26-esp-pedri"},

    {"shirt_number": 7, "first_name": "Ferran", "last_name": "Torres", "position": Player.Position.FORWARD, "club": "Barcelona", "external_id": "wc26-esp-ferran-torres"},
    {"shirt_number": 11, "first_name": "Yeremy", "last_name": "Pino", "position": Player.Position.FORWARD, "club": "Crystal Palace", "external_id": "wc26-esp-yeremy-pino"},
    {"shirt_number": 15, "first_name": "Alex", "last_name": "Baena", "position": Player.Position.FORWARD, "club": "Atletico Madrid", "external_id": "wc26-esp-alex-baena"},
    {"shirt_number": 17, "first_name": "Nico", "last_name": "Williams", "position": Player.Position.FORWARD, "club": "Athletic Club", "external_id": "wc26-esp-nico-williams"},
    {"shirt_number": 19, "first_name": "Lamine", "last_name": "Yamal", "position": Player.Position.FORWARD, "club": "Barcelona", "external_id": "wc26-esp-lamine-yamal"},
    {"shirt_number": 21, "first_name": "Mikel", "last_name": "Oyarzabal", "position": Player.Position.FORWARD, "club": "Real Sociedad", "external_id": "wc26-esp-mikel-oyarzabal"},
    {"shirt_number": 25, "first_name": "Victor", "last_name": "Munoz", "position": Player.Position.FORWARD, "club": "Osasuna", "external_id": "wc26-esp-victor-munoz"},
    {"shirt_number": 26, "first_name": "Borja", "last_name": "Iglesias", "position": Player.Position.FORWARD, "club": "Celta Vigo", "external_id": "wc26-esp-borja-iglesias"},
]

URUGUAY_PLAYERS = [
    {"shirt_number": 1, "first_name": "Sergio", "last_name": "Rochet", "position": Player.Position.GOALKEEPER, "club": "Internacional", "external_id": "wc26-uru-sergio-rochet"},
    {"shirt_number": 12, "first_name": "Santiago", "last_name": "Mele", "position": Player.Position.GOALKEEPER, "club": "Monterrey", "external_id": "wc26-uru-santiago-mele"},
    {"shirt_number": 23, "first_name": "Fernando", "last_name": "Muslera", "position": Player.Position.GOALKEEPER, "club": "Estudiantes", "external_id": "wc26-uru-fernando-muslera"},

    {"shirt_number": 2, "first_name": "Ronald", "last_name": "Araujo", "position": Player.Position.DEFENDER, "club": "Barcelona", "external_id": "wc26-uru-ronald-araujo"},
    {"shirt_number": 3, "first_name": "Jose Maria", "last_name": "Gimenez", "position": Player.Position.DEFENDER, "club": "Atletico Madrid", "external_id": "wc26-uru-jose-maria-gimenez"},
    {"shirt_number": 4, "first_name": "Santiago", "last_name": "Bueno", "position": Player.Position.DEFENDER, "club": "Wolverhampton Wanderers", "external_id": "wc26-uru-santiago-bueno"},
    {"shirt_number": 5, "first_name": "Sebastian", "last_name": "Caceres", "position": Player.Position.DEFENDER, "club": "America", "external_id": "wc26-uru-sebastian-caceres"},
    {"shirt_number": 6, "first_name": "Mathias", "last_name": "Olivera", "position": Player.Position.DEFENDER, "club": "Napoli", "external_id": "wc26-uru-mathias-olivera"},
    {"shirt_number": 13, "first_name": "Guillermo", "last_name": "Varela", "position": Player.Position.DEFENDER, "club": "Flamengo", "external_id": "wc26-uru-guillermo-varela"},
    {"shirt_number": 16, "first_name": "Matias", "last_name": "Vina", "position": Player.Position.DEFENDER, "club": "River Plate", "external_id": "wc26-uru-matias-vina"},
    {"shirt_number": 18, "first_name": "Joaquin", "last_name": "Piquerez", "position": Player.Position.DEFENDER, "club": "Palmeiras", "external_id": "wc26-uru-joaquin-piquerez"},
    {"shirt_number": 21, "first_name": "Juan Manuel", "last_name": "Sanabria", "position": Player.Position.DEFENDER, "club": "Real Salt Lake", "external_id": "wc26-uru-juan-manuel-sanabria"},

    {"shirt_number": 7, "first_name": "Federico", "last_name": "Valverde", "position": Player.Position.MIDFIELDER, "club": "Real Madrid", "external_id": "wc26-uru-federico-valverde"},
    {"shirt_number": 8, "first_name": "Rodrigo", "last_name": "Bentancur", "position": Player.Position.MIDFIELDER, "club": "Tottenham Hotspur", "external_id": "wc26-uru-rodrigo-bentancur"},
    {"shirt_number": 10, "first_name": "Giorgian", "last_name": "De Arrascaeta", "position": Player.Position.MIDFIELDER, "club": "Flamengo", "external_id": "wc26-uru-giorgian-de-arrascaeta"},
    {"shirt_number": 11, "first_name": "Nicolas", "last_name": "De La Cruz", "position": Player.Position.MIDFIELDER, "club": "Flamengo", "external_id": "wc26-uru-nicolas-de-la-cruz"},
    {"shirt_number": 14, "first_name": "Manuel", "last_name": "Ugarte", "position": Player.Position.MIDFIELDER, "club": "Manchester United", "external_id": "wc26-uru-manuel-ugarte"},
    {"shirt_number": 15, "first_name": "Emiliano", "last_name": "Martinez", "position": Player.Position.MIDFIELDER, "club": "Palmeiras", "external_id": "wc26-uru-emiliano-martinez"},
    {"shirt_number": 17, "first_name": "Rodrigo", "last_name": "Zalazar", "position": Player.Position.MIDFIELDER, "club": "Sporting CP", "external_id": "wc26-uru-rodrigo-zalazar"},
    {"shirt_number": 19, "first_name": "Agustin", "last_name": "Canobbio", "position": Player.Position.MIDFIELDER, "club": "Fluminense", "external_id": "wc26-uru-agustin-canobbio"},
    {"shirt_number": 20, "first_name": "Maximiliano", "last_name": "Araujo", "position": Player.Position.MIDFIELDER, "club": "Sporting CP", "external_id": "wc26-uru-maximiliano-araujo"},
    {"shirt_number": 22, "first_name": "Brian", "last_name": "Rodriguez", "position": Player.Position.MIDFIELDER, "club": "America", "external_id": "wc26-uru-brian-rodriguez"},
    {"shirt_number": 24, "first_name": "Facundo", "last_name": "Pellistri", "position": Player.Position.MIDFIELDER, "club": "Panathinaikos", "external_id": "wc26-uru-facundo-pellistri"},

    {"shirt_number": 9, "first_name": "Darwin", "last_name": "Nunez", "position": Player.Position.FORWARD, "club": "Al Hilal", "external_id": "wc26-uru-darwin-nunez"},
    {"shirt_number": 25, "first_name": "Federico", "last_name": "Vinas", "position": Player.Position.FORWARD, "club": "Real Oviedo", "external_id": "wc26-uru-federico-vinas"},
    {"shirt_number": 26, "first_name": "Rodrigo", "last_name": "Aguirre", "position": Player.Position.FORWARD, "club": "Tigres", "external_id": "wc26-uru-rodrigo-aguirre"},
]

CAPE_VERDE_PLAYERS = [
    {"shirt_number": 1, "first_name": "Vozinha", "last_name": "", "position": Player.Position.GOALKEEPER, "club": "Chaves", "external_id": "wc26-cpv-vozinha"},
    {"shirt_number": 12, "first_name": "Marcio", "last_name": "Rosa", "position": Player.Position.GOALKEEPER, "club": "Montana", "external_id": "wc26-cpv-marcio-rosa"},
    {"shirt_number": 23, "first_name": "CJ", "last_name": "Dos Santos", "position": Player.Position.GOALKEEPER, "club": "San Diego", "external_id": "wc26-cpv-cj-dos-santos"},

    {"shirt_number": 2, "first_name": "Logan", "last_name": "Costa", "position": Player.Position.DEFENDER, "club": "Villarreal", "external_id": "wc26-cpv-logan-costa"},
    {"shirt_number": 3, "first_name": "Roberto", "last_name": "Lopes", "position": Player.Position.DEFENDER, "club": "Shamrock Rovers", "external_id": "wc26-cpv-roberto-lopes"},
    {"shirt_number": 4, "first_name": "Stopira", "last_name": "", "position": Player.Position.DEFENDER, "club": "Torreense", "external_id": "wc26-cpv-stopira"},
    {"shirt_number": 5, "first_name": "Steven", "last_name": "Moreira", "position": Player.Position.DEFENDER, "club": "Columbus Crew", "external_id": "wc26-cpv-steven-moreira"},
    {"shirt_number": 13, "first_name": "Joao", "last_name": "Paulo", "position": Player.Position.DEFENDER, "club": "Oliveirense", "external_id": "wc26-cpv-joao-paulo"},
    {"shirt_number": 14, "first_name": "Diney", "last_name": "", "position": Player.Position.DEFENDER, "club": "Nacional", "external_id": "wc26-cpv-diney"},
    {"shirt_number": 15, "first_name": "Deroy", "last_name": "Duarte", "position": Player.Position.DEFENDER, "club": "Fortuna Sittard", "external_id": "wc26-cpv-deroy-duarte"},
    {"shirt_number": 16, "first_name": "Sidny", "last_name": "Cabral", "position": Player.Position.DEFENDER, "club": "Boavista", "external_id": "wc26-cpv-sidny-cabral"},
    {"shirt_number": 22, "first_name": "Willy", "last_name": "Semedo", "position": Player.Position.DEFENDER, "club": "Al-Faisaly", "external_id": "wc26-cpv-willy-semedo"},

    {"shirt_number": 6, "first_name": "Kevin", "last_name": "Pina", "position": Player.Position.MIDFIELDER, "club": "Gil Vicente", "external_id": "wc26-cpv-kevin-pina"},
    {"shirt_number": 8, "first_name": "Jamiro", "last_name": "Monteiro", "position": Player.Position.MIDFIELDER, "club": "PEC Zwolle", "external_id": "wc26-cpv-jamiro-monteiro"},
    {"shirt_number": 10, "first_name": "Kenny", "last_name": "Rocha", "position": Player.Position.MIDFIELDER, "club": "Standard Liege", "external_id": "wc26-cpv-kenny-rocha"},
    {"shirt_number": 17, "first_name": "Bebeto", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Viborg", "external_id": "wc26-cpv-bebeto"},
    {"shirt_number": 18, "first_name": "Patrick", "last_name": "Andrade", "position": Player.Position.MIDFIELDER, "club": "Karvina", "external_id": "wc26-cpv-patrick-andrade"},
    {"shirt_number": 19, "first_name": "Lisandro", "last_name": "Semedo", "position": Player.Position.MIDFIELDER, "club": "Al Bataeh", "external_id": "wc26-cpv-lisandro-semedo"},
    {"shirt_number": 20, "first_name": "Ilano", "last_name": "Silva Timas", "position": Player.Position.MIDFIELDER, "club": "Sparta Rotterdam", "external_id": "wc26-cpv-ilano-timas"},
    {"shirt_number": 21, "first_name": "Cuca", "last_name": "", "position": Player.Position.MIDFIELDER, "club": "Casa Pia", "external_id": "wc26-cpv-cuca"},

    {"shirt_number": 7, "first_name": "Ryan", "last_name": "Mendes", "position": Player.Position.FORWARD, "club": "Fatih Karagumruk", "external_id": "wc26-cpv-ryan-mendes"},
    {"shirt_number": 9, "first_name": "Benchimol", "last_name": "", "position": Player.Position.FORWARD, "club": "Oliveirense", "external_id": "wc26-cpv-benchimol"},
    {"shirt_number": 11, "first_name": "Dailon", "last_name": "Livramento", "position": Player.Position.FORWARD, "club": "Casa Pia", "external_id": "wc26-cpv-dailon-livramento"},
    {"shirt_number": 24, "first_name": "Jovane", "last_name": "Cabral", "position": Player.Position.FORWARD, "club": "Salernitana", "external_id": "wc26-cpv-jovane-cabral"},
    {"shirt_number": 25, "first_name": "Hergino", "last_name": "Tavares", "position": Player.Position.FORWARD, "club": "Farense", "external_id": "wc26-cpv-hergino-tavares"},
    {"shirt_number": 26, "first_name": "Helio", "last_name": "Varela", "position": Player.Position.FORWARD, "club": "Maccabi Tel Aviv", "external_id": "wc26-cpv-helio-varela"},
]

SAUDI_ARABIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Mohammed", "last_name": "Al-Owais", "position": Player.Position.GOALKEEPER, "club": "Al-Ula", "external_id": "wc26-ksa-mohammed-al-owais"},
    {"shirt_number": 12, "first_name": "Nawaf", "last_name": "Al-Aqidi", "position": Player.Position.GOALKEEPER, "club": "Al-Nassr", "external_id": "wc26-ksa-nawaf-al-aqidi"},
    {"shirt_number": 23, "first_name": "Ahmed", "last_name": "Alkassar", "position": Player.Position.GOALKEEPER, "club": "Al-Qadsiah", "external_id": "wc26-ksa-ahmed-alkassar"},

    {"shirt_number": 2, "first_name": "Saud", "last_name": "Abdulhamid", "position": Player.Position.DEFENDER, "club": "Lens", "external_id": "wc26-ksa-saud-abdulhamid"},
    {"shirt_number": 3, "first_name": "Hassan", "last_name": "Kadesh", "position": Player.Position.DEFENDER, "club": "Al-Ittihad", "external_id": "wc26-ksa-hassan-kadesh"},
    {"shirt_number": 4, "first_name": "Ali", "last_name": "Lajami", "position": Player.Position.DEFENDER, "club": "Al-Hilal", "external_id": "wc26-ksa-ali-lajami"},
    {"shirt_number": 5, "first_name": "Abdulelah", "last_name": "Al-Amri", "position": Player.Position.DEFENDER, "club": "Al-Nassr", "external_id": "wc26-ksa-abdulelah-al-amri"},
    {"shirt_number": 6, "first_name": "Hassan", "last_name": "Tambakti", "position": Player.Position.DEFENDER, "club": "Al-Hilal", "external_id": "wc26-ksa-hassan-tambakti"},
    {"shirt_number": 13, "first_name": "Jehad", "last_name": "Thikri", "position": Player.Position.DEFENDER, "club": "Al-Qadsiah", "external_id": "wc26-ksa-jehad-thikri"},
    {"shirt_number": 14, "first_name": "Mohammed", "last_name": "Abu Al Shamat", "position": Player.Position.DEFENDER, "club": "Al-Qadsiah", "external_id": "wc26-ksa-mohammed-abu-al-shamat"},
    {"shirt_number": 15, "first_name": "Ali", "last_name": "Majrashi", "position": Player.Position.DEFENDER, "club": "Al-Ahli", "external_id": "wc26-ksa-ali-majrashi"},
    {"shirt_number": 16, "first_name": "Moteb", "last_name": "Al-Harbi", "position": Player.Position.DEFENDER, "club": "Al-Hilal", "external_id": "wc26-ksa-moteb-al-harbi"},
    {"shirt_number": 24, "first_name": "Nawaf", "last_name": "Boushal", "position": Player.Position.DEFENDER, "club": "Al-Nassr", "external_id": "wc26-ksa-nawaf-boushal"},
    {"shirt_number": 25, "first_name": "Sultan", "last_name": "Al-Ghannam", "position": Player.Position.DEFENDER, "club": "Al-Nassr", "external_id": "wc26-ksa-sultan-al-ghannam"},

    {"shirt_number": 7, "first_name": "Mohammed", "last_name": "Kanno", "position": Player.Position.MIDFIELDER, "club": "Al-Hilal", "external_id": "wc26-ksa-mohammed-kanno"},
    {"shirt_number": 8, "first_name": "Abdullah", "last_name": "Al-Khaibari", "position": Player.Position.MIDFIELDER, "club": "Al-Nassr", "external_id": "wc26-ksa-abdullah-al-khaibari"},
    {"shirt_number": 10, "first_name": "Salem", "last_name": "Al-Dawsari", "position": Player.Position.MIDFIELDER, "club": "Al-Hilal", "external_id": "wc26-ksa-salem-al-dawsari"},
    {"shirt_number": 17, "first_name": "Ziyad", "last_name": "Al-Johani", "position": Player.Position.MIDFIELDER, "club": "Al-Ahli", "external_id": "wc26-ksa-ziyad-al-johani"},
    {"shirt_number": 18, "first_name": "Nasser", "last_name": "Al-Dawsari", "position": Player.Position.MIDFIELDER, "club": "Al-Hilal", "external_id": "wc26-ksa-nasser-al-dawsari"},
    {"shirt_number": 19, "first_name": "Musab", "last_name": "Al-Juwayr", "position": Player.Position.MIDFIELDER, "club": "Al-Qadsiah", "external_id": "wc26-ksa-musab-al-juwayr"},
    {"shirt_number": 20, "first_name": "Alaa", "last_name": "Al-Hajji", "position": Player.Position.MIDFIELDER, "club": "Neom", "external_id": "wc26-ksa-alaa-al-hajji"},
    {"shirt_number": 21, "first_name": "Khalid", "last_name": "Al-Ghannam", "position": Player.Position.MIDFIELDER, "club": "Al-Ettifaq", "external_id": "wc26-ksa-khalid-al-ghannam"},
    {"shirt_number": 22, "first_name": "Ayman", "last_name": "Yahya", "position": Player.Position.MIDFIELDER, "club": "Al-Nassr", "external_id": "wc26-ksa-ayman-yahya"},

    {"shirt_number": 9, "first_name": "Firas", "last_name": "Al-Buraikan", "position": Player.Position.FORWARD, "club": "Al-Ahli", "external_id": "wc26-ksa-firas-al-buraikan"},
    {"shirt_number": 11, "first_name": "Saleh", "last_name": "Al-Shehri", "position": Player.Position.FORWARD, "club": "Al-Ittihad", "external_id": "wc26-ksa-saleh-al-shehri"},
    {"shirt_number": 26, "first_name": "Abdullah", "last_name": "Al-Hamdan", "position": Player.Position.FORWARD, "club": "Al-Nassr", "external_id": "wc26-ksa-abdullah-al-hamdan"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo H del Mundial 2026"

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
            spain = Team.objects.get(fifa_code="ESP")
            cape_verde = Team.objects.get(fifa_code="CPV")
            saudi_arabia = Team.objects.get(fifa_code="KSA")
            uruguay = Team.objects.get(fifa_code="URU")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo H en la base de datos: {exc}")

        results = []

        results.append(("Spain", *self.load_players_for_team(spain, SPAIN_PLAYERS)))
        results.append(("Cape Verde", *self.load_players_for_team(cape_verde, CAPE_VERDE_PLAYERS)))
        results.append(("Saudi Arabia", *self.load_players_for_team(saudi_arabia, SAUDI_ARABIA_PLAYERS)))
        results.append(("Uruguay", *self.load_players_for_team(uruguay, URUGUAY_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo H completada."))