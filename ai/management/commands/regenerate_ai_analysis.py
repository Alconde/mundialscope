from django.core.management.base import BaseCommand

from matches.models import Match
from matches.report_services import generate_match_report
from teams.models import Team
from teams.report_services import generate_team_report


class Command(BaseCommand):
    help = "Regenera informes automáticos con capa IA para partidos y selecciones."

    def handle(self, *args, **options):
        finished_matches = Match.objects.filter(status=Match.Status.FINISHED)
        teams = Team.objects.filter(is_active=True)

        match_count = 0
        team_count = 0

        for match in finished_matches:
            generate_match_report(match)
            match_count += 1

        for team in teams:
            generate_team_report(team)
            team_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Informes regenerados correctamente: {match_count} partidos y {team_count} selecciones."
            )
        )