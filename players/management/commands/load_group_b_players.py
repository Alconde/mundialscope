from django.core.management.base import BaseCommand, CommandError
from players.models import Player
from teams.models import Team


CANADA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Dayne", "last_name": "St. Clair", "position": Player.Position.GOALKEEPER, "club": "Inter Miami CF", "external_id": "wc26-can-dayne-st-clair"},
    {"shirt_number": 12, "first_name": "Maxime", "last_name": "Crepeau", "position": Player.Position.GOALKEEPER, "club": "Orlando City SC", "external_id": "wc26-can-maxime-crepeau"},
    {"shirt_number": 23, "first_name": "Owen", "last_name": "Goodman", "position": Player.Position.GOALKEEPER, "club": "Barnsley", "external_id": "wc26-can-owen-goodman"},

    {"shirt_number": 2, "first_name": "Alistair", "last_name": "Johnston", "position": Player.Position.DEFENDER, "club": "Celtic", "external_id": "wc26-can-alistair-johnston"},
    {"shirt_number": 3, "first_name": "Alfie", "last_name": "Jones", "position": Player.Position.DEFENDER, "club": "Middlesbrough", "external_id": "wc26-can-alfie-jones"},
    {"shirt_number": 4, "first_name": "Luc", "last_name": "de Fougerolles", "position": Player.Position.DEFENDER, "club": "FCV Dender", "external_id": "wc26-can-luc-de-fougerolles"},
    {"shirt_number": 5, "first_name": "Joel", "last_name": "Waterman", "position": Player.Position.DEFENDER, "club": "Chicago Fire", "external_id": "wc26-can-joel-waterman"},
    {"shirt_number": 13, "first_name": "Derek", "last_name": "Cornelius", "position": Player.Position.DEFENDER, "club": "Rangers", "external_id": "wc26-can-derek-cornelius"},
    {"shirt_number": 14, "first_name": "Moise", "last_name": "Bombito", "position": Player.Position.DEFENDER, "club": "Nice", "external_id": "wc26-can-moise-bombito"},
    {"shirt_number": 15, "first_name": "Alphonso", "last_name": "Davies", "position": Player.Position.DEFENDER, "club": "Bayern Munich", "external_id": "wc26-can-alphonso-davies"},
    {"shirt_number": 16, "first_name": "Richie", "last_name": "Laryea", "position": Player.Position.DEFENDER, "club": "Toronto FC", "external_id": "wc26-can-richie-laryea"},
    {"shirt_number": 22, "first_name": "Niko", "last_name": "Sigur", "position": Player.Position.DEFENDER, "club": "Hajduk Split", "external_id": "wc26-can-niko-sigur"},

    {"shirt_number": 6, "first_name": "Mathieu", "last_name": "Choiniere", "position": Player.Position.MIDFIELDER, "club": "LAFC", "external_id": "wc26-can-mathieu-choiniere"},
    {"shirt_number": 7, "first_name": "Stephen", "last_name": "Eustaquio", "position": Player.Position.MIDFIELDER, "club": "LAFC", "external_id": "wc26-can-stephen-eustaquio"},
    {"shirt_number": 8, "first_name": "Ismael", "last_name": "Kone", "position": Player.Position.MIDFIELDER, "club": "Sassuolo", "external_id": "wc26-can-ismael-kone"},
    {"shirt_number": 17, "first_name": "Liam", "last_name": "Millar", "position": Player.Position.MIDFIELDER, "club": "Hull City", "external_id": "wc26-can-liam-millar"},
    {"shirt_number": 18, "first_name": "Jacob", "last_name": "Shaffelburg", "position": Player.Position.MIDFIELDER, "club": "LAFC", "external_id": "wc26-can-jacob-shaffelburg"},
    {"shirt_number": 19, "first_name": "Jonathan", "last_name": "Osorio", "position": Player.Position.MIDFIELDER, "club": "Toronto FC", "external_id": "wc26-can-jonathan-osorio"},
    {"shirt_number": 20, "first_name": "Nathan", "last_name": "Saliba", "position": Player.Position.MIDFIELDER, "club": "Anderlecht", "external_id": "wc26-can-nathan-saliba"},
    {"shirt_number": 21, "first_name": "Marcelo", "last_name": "Flores", "position": Player.Position.MIDFIELDER, "club": "Tigres", "external_id": "wc26-can-marcelo-flores"},

    {"shirt_number": 9, "first_name": "Cyle", "last_name": "Larin", "position": Player.Position.FORWARD, "club": "Southampton", "external_id": "wc26-can-cyle-larin"},
    {"shirt_number": 10, "first_name": "Jonathan", "last_name": "David", "position": Player.Position.FORWARD, "club": "Juventus", "external_id": "wc26-can-jonathan-david"},
    {"shirt_number": 11, "first_name": "Tani", "last_name": "Oluwaseyi", "position": Player.Position.FORWARD, "club": "Villarreal", "external_id": "wc26-can-tani-oluwaseyi"},
    {"shirt_number": 24, "first_name": "Tajon", "last_name": "Buchanan", "position": Player.Position.FORWARD, "club": "Villarreal", "external_id": "wc26-can-tajon-buchanan"},
    {"shirt_number": 25, "first_name": "Ali", "last_name": "Ahmed", "position": Player.Position.FORWARD, "club": "Norwich City", "external_id": "wc26-can-ali-ahmed"},
    {"shirt_number": 26, "first_name": "Promise", "last_name": "David", "position": Player.Position.FORWARD, "club": "Union Saint-Gilloise", "external_id": "wc26-can-promise-david"},
]


BOSNIA_PLAYERS = [
    {"shirt_number": 1, "first_name": "Nikola", "last_name": "Vasilj", "position": Player.Position.GOALKEEPER, "club": "St. Pauli", "external_id": "wc26-bih-nikola-vasilj"},
    {"shirt_number": 12, "first_name": "Mladen", "last_name": "Jurkas", "position": Player.Position.GOALKEEPER, "club": "Borac Banja Luka", "external_id": "wc26-bih-mladen-jurkas"},
    {"shirt_number": 23, "first_name": "Martin", "last_name": "Zlomislic", "position": Player.Position.GOALKEEPER, "club": "Rijeka", "external_id": "wc26-bih-martin-zlomislic"},

    {"shirt_number": 2, "first_name": "Nihad", "last_name": "Mujakic", "position": Player.Position.DEFENDER, "club": "Gaziantep", "external_id": "wc26-bih-nihad-mujakic"},
    {"shirt_number": 3, "first_name": "Dennis", "last_name": "Hadzikadunic", "position": Player.Position.DEFENDER, "club": "Sampdoria", "external_id": "wc26-bih-dennis-hadzikadunic"},
    {"shirt_number": 4, "first_name": "Tarik", "last_name": "Muharemovic", "position": Player.Position.DEFENDER, "club": "Sassuolo", "external_id": "wc26-bih-tarik-muharemovic"},
    {"shirt_number": 5, "first_name": "Sead", "last_name": "Kolasinac", "position": Player.Position.DEFENDER, "club": "Atalanta", "external_id": "wc26-bih-sead-kolasinac"},
    {"shirt_number": 13, "first_name": "Amar", "last_name": "Dedic", "position": Player.Position.DEFENDER, "club": "Benfica", "external_id": "wc26-bih-amar-dedic"},
    {"shirt_number": 14, "first_name": "Stjepan", "last_name": "Radeljic", "position": Player.Position.DEFENDER, "club": "Rijeka", "external_id": "wc26-bih-stjepan-radeljic"},
    {"shirt_number": 15, "first_name": "Nikola", "last_name": "Katic", "position": Player.Position.DEFENDER, "club": "Schalke 04", "external_id": "wc26-bih-nikola-katic"},
    {"shirt_number": 21, "first_name": "Nidal", "last_name": "Celik", "position": Player.Position.DEFENDER, "club": "Lens", "external_id": "wc26-bih-nidal-celik"},

    {"shirt_number": 6, "first_name": "Benjamin", "last_name": "Tahirovic", "position": Player.Position.MIDFIELDER, "club": "Brondby", "external_id": "wc26-bih-benjamin-tahirovic"},
    {"shirt_number": 8, "first_name": "Armin", "last_name": "Gigovic", "position": Player.Position.MIDFIELDER, "club": "Young Boys", "external_id": "wc26-bih-armin-gigovic"},
    {"shirt_number": 10, "first_name": "Amir", "last_name": "Hadziahmetovic", "position": Player.Position.MIDFIELDER, "club": "Hull City", "external_id": "wc26-bih-amir-hadziahmetovic"},
    {"shirt_number": 16, "first_name": "Ivan", "last_name": "Basic", "position": Player.Position.MIDFIELDER, "club": "Astana", "external_id": "wc26-bih-ivan-basic"},
    {"shirt_number": 17, "first_name": "Ivan", "last_name": "Sunjic", "position": Player.Position.MIDFIELDER, "club": "Pafos", "external_id": "wc26-bih-ivan-sunjic"},
    {"shirt_number": 18, "first_name": "Amar", "last_name": "Memic", "position": Player.Position.MIDFIELDER, "club": "Viktoria Plzen", "external_id": "wc26-bih-amar-memic"},
    {"shirt_number": 22, "first_name": "Dzenis", "last_name": "Burnic", "position": Player.Position.MIDFIELDER, "club": "Karlsruher", "external_id": "wc26-bih-dzenis-burnic"},
    {"shirt_number": 24, "first_name": "Ermin", "last_name": "Mahmic", "position": Player.Position.MIDFIELDER, "club": "Slovan Liberec", "external_id": "wc26-bih-ermin-mahmic"},

    {"shirt_number": 7, "first_name": "Samed", "last_name": "Bazdar", "position": Player.Position.FORWARD, "club": "Jagiellonia", "external_id": "wc26-bih-samed-bazdar"},
    {"shirt_number": 9, "first_name": "Ermedin", "last_name": "Demirovic", "position": Player.Position.FORWARD, "club": "Stuttgart", "external_id": "wc26-bih-ermedin-demirovic"},
    {"shirt_number": 11, "first_name": "Edin", "last_name": "Dzeko", "position": Player.Position.FORWARD, "club": "Schalke 04", "external_id": "wc26-bih-edin-dzeko"},
    {"shirt_number": 19, "first_name": "Haris", "last_name": "Tabakovic", "position": Player.Position.FORWARD, "club": "Borussia Monchengladbach", "external_id": "wc26-bih-haris-tabakovic"},
    {"shirt_number": 20, "first_name": "Kerim", "last_name": "Alajbegovic", "position": Player.Position.FORWARD, "club": "RB Salzburg", "external_id": "wc26-bih-kerim-alajbegovic"},
    {"shirt_number": 25, "first_name": "Esmir", "last_name": "Bajraktarevic", "position": Player.Position.FORWARD, "club": "PSV", "external_id": "wc26-bih-esmir-bajraktarevic"},
    {"shirt_number": 26, "first_name": "Jovo", "last_name": "Lukic", "position": Player.Position.FORWARD, "club": "Universitatea Cluj", "external_id": "wc26-bih-jovo-lukic"},
]


QATAR_PLAYERS = [
    {"shirt_number": 1, "first_name": "Meshaal", "last_name": "Barsham", "position": Player.Position.GOALKEEPER, "club": "Al-Sadd", "external_id": "wc26-qat-meshaal-barsham"},
    {"shirt_number": 12, "first_name": "Saad", "last_name": "Al-Sheeb", "position": Player.Position.GOALKEEPER, "club": "Al-Sadd", "external_id": "wc26-qat-saad-al-sheeb"},
    {"shirt_number": 23, "first_name": "Yousef", "last_name": "Hassan", "position": Player.Position.GOALKEEPER, "club": "Al-Gharafa", "external_id": "wc26-qat-yousef-hassan"},

    {"shirt_number": 2, "first_name": "Pedro", "last_name": "Miguel", "position": Player.Position.DEFENDER, "club": "Al-Sadd", "external_id": "wc26-qat-pedro-miguel"},
    {"shirt_number": 3, "first_name": "Homam", "last_name": "Ahmad", "position": Player.Position.DEFENDER, "club": "Al-Gharafa", "external_id": "wc26-qat-homam-ahmad"},
    {"shirt_number": 4, "first_name": "Bassam", "last_name": "Al-Rawi", "position": Player.Position.DEFENDER, "club": "Al-Duhail", "external_id": "wc26-qat-bassam-al-rawi"},
    {"shirt_number": 5, "first_name": "Boualem", "last_name": "Khoukhi", "position": Player.Position.DEFENDER, "club": "Al-Sadd", "external_id": "wc26-qat-boualem-khoukhi"},
    {"shirt_number": 13, "first_name": "Abdelkarim", "last_name": "Hassan", "position": Player.Position.DEFENDER, "club": "Al-Arabi", "external_id": "wc26-qat-abdelkarim-hassan"},
    {"shirt_number": 14, "first_name": "Ismail", "last_name": "Mohammed", "position": Player.Position.DEFENDER, "club": "Al-Duhail", "external_id": "wc26-qat-ismail-mohammed"},
    {"shirt_number": 15, "first_name": "Musab", "last_name": "Khodir", "position": Player.Position.DEFENDER, "club": "Al-Sadd", "external_id": "wc26-qat-musab-khodir"},

    {"shirt_number": 6, "first_name": "Karim", "last_name": "Boudiaf", "position": Player.Position.MIDFIELDER, "club": "Al-Duhail", "external_id": "wc26-qat-karim-boudiaf"},
    {"shirt_number": 8, "first_name": "Abdulaziz", "last_name": "Hatem", "position": Player.Position.MIDFIELDER, "club": "Al-Rayyan", "external_id": "wc26-qat-abdulaziz-hatem"},
    {"shirt_number": 10, "first_name": "Akram", "last_name": "Afif", "position": Player.Position.MIDFIELDER, "club": "Al-Sadd", "external_id": "wc26-qat-akram-afif"},
    {"shirt_number": 16, "first_name": "Abdullah", "last_name": "Al-Ahrak", "position": Player.Position.MIDFIELDER, "club": "Al-Duhail", "external_id": "wc26-qat-abdullah-al-ahrak"},
    {"shirt_number": 17, "first_name": "Ali", "last_name": "Asad", "position": Player.Position.MIDFIELDER, "club": "Al-Sadd", "external_id": "wc26-qat-ali-asad"},
    {"shirt_number": 18, "first_name": "Tarek", "last_name": "Sallam", "position": Player.Position.MIDFIELDER, "club": "Al-Arabi", "external_id": "wc26-qat-tarek-sallam"},

    {"shirt_number": 7, "first_name": "Almoez", "last_name": "Ali", "position": Player.Position.FORWARD, "club": "Al-Duhail", "external_id": "wc26-qat-almoez-ali"},
    {"shirt_number": 9, "first_name": "Mohammed", "last_name": "Muntari", "position": Player.Position.FORWARD, "club": "Al-Duhail", "external_id": "wc26-qat-mohammed-muntari"},
    {"shirt_number": 11, "first_name": "Hasan", "last_name": "Al-Haydos", "position": Player.Position.FORWARD, "club": "Al-Sadd", "external_id": "wc26-qat-hasan-al-haydos"},
    {"shirt_number": 19, "first_name": "Yusuf", "last_name": "Abdurisag", "position": Player.Position.FORWARD, "club": "Al-Sadd", "external_id": "wc26-qat-yusuf-abdurisag"},
    {"shirt_number": 20, "first_name": "Ahmed", "last_name": "Alaaeldin", "position": Player.Position.FORWARD, "club": "Al-Gharafa", "external_id": "wc26-qat-ahmed-alaaeldin"},
    {"shirt_number": 21, "first_name": "Ismaeel", "last_name": "Mohammed", "position": Player.Position.FORWARD, "club": "Al-Duhail", "external_id": "wc26-qat-ismaeel-mohammed"},
    {"shirt_number": 22, "first_name": "Naif", "last_name": "Al-Hadhrami", "position": Player.Position.FORWARD, "club": "Al-Rayyan", "external_id": "wc26-qat-naif-al-hadhrami"},
    {"shirt_number": 24, "first_name": "Jassem", "last_name": "Gabriel", "position": Player.Position.FORWARD, "club": "Al-Arabi", "external_id": "wc26-qat-jassem-gabriel"},
    {"shirt_number": 25, "first_name": "Khalid", "last_name": "Mubarak", "position": Player.Position.FORWARD, "club": "Al-Gharafa", "external_id": "wc26-qat-khalid-mubarak"},
    {"shirt_number": 26, "first_name": "Mahdi", "last_name": "Salem", "position": Player.Position.FORWARD, "club": "Al-Rayyan", "external_id": "wc26-qat-mahdi-salem"},
]


SWITZERLAND_PLAYERS = [
    {"shirt_number": 1, "first_name": "Yann", "last_name": "Sommer", "position": Player.Position.GOALKEEPER, "club": "Inter Milan", "external_id": "wc26-sui-yann-sommer"},
    {"shirt_number": 12, "first_name": "Gregor", "last_name": "Kobel", "position": Player.Position.GOALKEEPER, "club": "Borussia Dortmund", "external_id": "wc26-sui-gregor-kobel"},
    {"shirt_number": 23, "first_name": "Yvon", "last_name": "Mvogo", "position": Player.Position.GOALKEEPER, "club": "Lorient", "external_id": "wc26-sui-yvon-mvogo"},

    {"shirt_number": 2, "first_name": "Silvan", "last_name": "Widmer", "position": Player.Position.DEFENDER, "club": "Mainz", "external_id": "wc26-sui-silvan-widmer"},
    {"shirt_number": 3, "first_name": "Manuel", "last_name": "Akanji", "position": Player.Position.DEFENDER, "club": "Manchester City", "external_id": "wc26-sui-manuel-akanji"},
    {"shirt_number": 4, "first_name": "Nico", "last_name": "Elvedi", "position": Player.Position.DEFENDER, "club": "Borussia Monchengladbach", "external_id": "wc26-sui-nico-elvedi"},
    {"shirt_number": 5, "first_name": "Ricardo", "last_name": "Rodriguez", "position": Player.Position.DEFENDER, "club": "Torino", "external_id": "wc26-sui-ricardo-rodriguez"},
    {"shirt_number": 13, "first_name": "Kevin", "last_name": "Mbabu", "position": Player.Position.DEFENDER, "club": "Augsburg", "external_id": "wc26-sui-kevin-mbabu"},
    {"shirt_number": 14, "first_name": "Fabian", "last_name": "Schar", "position": Player.Position.DEFENDER, "club": "Newcastle United", "external_id": "wc26-sui-fabian-schar"},
    {"shirt_number": 15, "first_name": "Ulisses", "last_name": "Garcia", "position": Player.Position.DEFENDER, "club": "Marseille", "external_id": "wc26-sui-ulisses-garcia"},

    {"shirt_number": 6, "first_name": "Granit", "last_name": "Xhaka", "position": Player.Position.MIDFIELDER, "club": "Bayer Leverkusen", "external_id": "wc26-sui-granit-xhaka"},
    {"shirt_number": 8, "first_name": "Remo", "last_name": "Freuler", "position": Player.Position.MIDFIELDER, "club": "Bologna", "external_id": "wc26-sui-remo-freuler"},
    {"shirt_number": 10, "first_name": "Xherdan", "last_name": "Shaqiri", "position": Player.Position.MIDFIELDER, "club": "Chicago Fire", "external_id": "wc26-sui-xherdan-shaqiri"},
    {"shirt_number": 16, "first_name": "Denis", "last_name": "Zakaria", "position": Player.Position.MIDFIELDER, "club": "Monaco", "external_id": "wc26-sui-denis-zakaria"},
    {"shirt_number": 17, "first_name": "Djibril", "last_name": "Sow", "position": Player.Position.MIDFIELDER, "club": "Sevilla", "external_id": "wc26-sui-djibril-sow"},
    {"shirt_number": 18, "first_name": "Michel", "last_name": "Aebischer", "position": Player.Position.MIDFIELDER, "club": "Bologna", "external_id": "wc26-sui-michel-aebischer"},
    {"shirt_number": 20, "first_name": "Fabian", "last_name": "Rieder", "position": Player.Position.MIDFIELDER, "club": "Stade Rennais", "external_id": "wc26-sui-fabian-rieder"},

    {"shirt_number": 7, "first_name": "Breel", "last_name": "Embolo", "position": Player.Position.FORWARD, "club": "Monaco", "external_id": "wc26-sui-breel-embolo"},
    {"shirt_number": 9, "first_name": "Haris", "last_name": "Seferovic", "position": Player.Position.FORWARD, "club": "Galatasaray", "external_id": "wc26-sui-haris-seferovic"},
    {"shirt_number": 11, "first_name": "Ruben", "last_name": "Vargas", "position": Player.Position.FORWARD, "club": "Augsburg", "external_id": "wc26-sui-ruben-vargas"},
    {"shirt_number": 19, "first_name": "Noah", "last_name": "Okafor", "position": Player.Position.FORWARD, "club": "Milan", "external_id": "wc26-sui-noah-okafor"},
    {"shirt_number": 21, "first_name": "Dan", "last_name": "Ndoye", "position": Player.Position.FORWARD, "club": "Bologna", "external_id": "wc26-sui-dan-ndoye"},
    {"shirt_number": 22, "first_name": "Andi", "last_name": "Zeqiri", "position": Player.Position.FORWARD, "club": "Genk", "external_id": "wc26-sui-andi-zeqiri"},
    {"shirt_number": 24, "first_name": "Cedric", "last_name": "Itten", "position": Player.Position.FORWARD, "club": "Young Boys", "external_id": "wc26-sui-cedric-itten"},
    {"shirt_number": 25, "first_name": "Zeki", "last_name": "Amdouni", "position": Player.Position.FORWARD, "club": "Burnley", "external_id": "wc26-sui-zeki-amdouni"},
    {"shirt_number": 26, "first_name": "Renato", "last_name": "Steffen", "position": Player.Position.FORWARD, "club": "Lugano", "external_id": "wc26-sui-renato-steffen"},
]


class Command(BaseCommand):
    help = "Carga jugadores del Grupo B del Mundial 2026"

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
            canada = Team.objects.get(fifa_code="CAN")
            bosnia = Team.objects.get(fifa_code="BIH")
            qatar = Team.objects.get(fifa_code="QAT")
            switzerland = Team.objects.get(fifa_code="SUI")
        except Team.DoesNotExist as exc:
            raise CommandError(f"Falta un equipo del Grupo B en la base de datos: {exc}")

        results = []

        results.append(("Canada", *self.load_players_for_team(canada, CANADA_PLAYERS)))
        results.append(("Bosnia and Herzegovina", *self.load_players_for_team(bosnia, BOSNIA_PLAYERS)))
        results.append(("Qatar", *self.load_players_for_team(qatar, QATAR_PLAYERS)))
        results.append(("Switzerland", *self.load_players_for_team(switzerland, SWITZERLAND_PLAYERS)))

        for team_name, created_count, updated_count in results:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{team_name}: creados {created_count}, actualizados {updated_count}"
                )
            )

        self.stdout.write(self.style.SUCCESS("Carga del Grupo B completada."))