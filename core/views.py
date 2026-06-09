from django.views.generic import TemplateView
from matches.dashboard_services import get_dashboard_context
from collections import OrderedDict
from django.db.models import Count, Q, Sum
from django.shortcuts import render
from teams.models import Team
from matches.models import Match
from teams.utils.flags import get_flag_code



class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_dashboard_context())
        return context  





class GroupsView(TemplateView):
    template_name = "core/groups.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teams = (
            Team.objects
            .filter(group__isnull=False)
            .annotate(
                called_up_count=Count(
                    "players",
                    filter=Q(players__is_called_up=True),
                    distinct=True,
                )
            )
            .order_by("group", "name")
        )

        groups = OrderedDict()

        for team in teams:
            standings = self._build_team_standings(team)
            group_key = team.group.upper()

            if group_key not in groups:
                groups[group_key] = []

            groups[group_key].append({
                "team": team,
                "stats": standings,
                "flag_code": get_flag_code(team),
            })

        for group_key, rows in groups.items():
            groups[group_key] = sorted(
                rows,
                key=lambda row: (
                    -row["stats"]["points"],
                    -row["stats"]["goal_difference"],
                    -row["stats"]["goals_for"],
                    row["team"].name,
                )
            )

        context["groups"] = groups
        context["groups_count"] = len(groups)
        context["teams_count"] = teams.count()
        return context

    def _build_team_standings(self, team):
        matches = (
            Match.objects.filter(
                Q(home_team=team) | Q(away_team=team),
                group=team.group,
            )
            .select_related("home_team", "away_team", "tournament")
            .distinct()
            .order_by("match_date")
        )

        played = 0
        wins = 0
        draws = 0
        losses = 0
        goals_for = 0
        goals_against = 0
        form = []

        valid_statuses = {"finished", "completed", "full_time"}

        for match in matches:
            if match.home_score is None or match.away_score is None:
                continue

            if match.status and str(match.status).lower() not in valid_statuses:
                continue

            played += 1

            if match.home_team_id == team.id:
                gf = match.home_score
                ga = match.away_score
            else:
                gf = match.away_score
                ga = match.home_score

            goals_for += gf
            goals_against += ga

            if gf > ga:
                wins += 1
                form.append("W")
            elif gf == ga:
                draws += 1
                form.append("D")
            else:
                losses += 1
                form.append("L")

        points = wins * 3 + draws
        goal_difference = goals_for - goals_against

        return {
            "played": played,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_difference": goal_difference,
            "points": points,
            "form": form[-5:],
        }
    def _get_flag_code(self, team):
        fifa_to_flag_code = {
            "ARG": "ar",
            "AUS": "au",
            "BEL": "be",
            "BIH": "ba",
            "BRA": "br",
            "CAN": "ca",
            "CHI": "cl",
            "CMR": "cm",
            "CPV": "cv",
            "CRO": "hr",
            "CUW": "cw",
            "CZE": "cz",
            "DEN": "dk",
            "ECU": "ec",
            "ENG": "gb-eng",
            "ESP": "es",
            "FRA": "fr",
            "GHA": "gh",
            "IRN": "ir",
            "ITA": "it",
            "JPN": "jp",
            "KOR": "kr",
            "MAR": "ma",
            "MEX": "mx",
            "NED": "nl",
            "NZL": "nz",
            "PAN": "pa",
            "POR": "pt",
            "QAT": "qa",
            "RSA": "za",
            "SCO": "gb-sct",
            "SEN": "sn",
            "SUI": "ch",
            "TUN": "tn",
            "URU": "uy",
            "USA": "us",
        }

        return fifa_to_flag_code.get((team.fifa_code or "").upper())