from django.db.models import Q
from matches.models import Match, MatchEvent

def get_team_matches_queryset(team):
    return Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        home_team=team
    ) | Match.objects.select_related(
        "tournament",
        "home_team",
        "away_team",
    ).filter(
        away_team=team
    )


def build_team_stats(team):
    matches = get_team_matches_queryset(team).order_by("-match_date")

    finished_matches = [match for match in matches if match.status == Match.Status.FINISHED]
    upcoming_matches = [match for match in matches if match.match_date and match.status != Match.Status.FINISHED]

    played = 0
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0
    points = 0
    recent_form = []

    for match in finished_matches:
        is_home = match.home_team_id == team.id
        scored = match.home_score if is_home else match.away_score
        conceded = match.away_score if is_home else match.home_score

        played += 1
        goals_for += scored
        goals_against += conceded

        if scored > conceded:
            wins += 1
            points += 3
            recent_form.append("W")
        elif scored < conceded:
            losses += 1
            recent_form.append("L")
        else:
            draws += 1
            points += 1
            recent_form.append("D")

    goal_difference = goals_for - goals_against
    recent_form = recent_form[:5]
    recent_form.reverse()

    return {
        "played": played,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goal_difference": goal_difference,
        "points": points,
        "recent_form": recent_form,
        "last_matches": finished_matches[:5],
        "upcoming_matches": sorted(upcoming_matches, key=lambda m: m.match_date)[:5],
    }


def get_team_dashboard_kpis(team):
    mmatches_qs = Match.objects.filter(
        Q(home_team=team) | Q(away_team=team),
        status=Match.Status.FINISHED
    ).distinct().order_by("-match_date")

    total_matches = matches_qs.count()

    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0

    recent_matches = list(matches_qs[:5])
    recent_matches_chronological = list(reversed(recent_matches))

    form_labels = []
    form_points = []
    goals_for_series = []
    goals_against_series = []

    for index, match in enumerate(recent_matches_chronological, start=1):
        if match.home_team_id == team.id:
            gf = match.home_score
            ga = match.away_score
            opponent = match.away_team.name
        else:
            gf = match.away_score
            ga = match.home_score
            opponent = match.home_team.name

        goals_for += gf
        goals_against += ga

        if gf > ga:
            wins += 1
            points = 3
        elif gf == ga:
            draws += 1
            points = 1
        else:
            losses += 1
            points = 0

        form_labels.append(f"J{index} vs {opponent}")
        form_points.append(points)
        goals_for_series.append(gf)
        goals_against_series.append(ga)

    all_matches = list(matches_qs)
    for match in all_matches[5:]:
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
        elif gf == ga:
            draws += 1
        else:
            losses += 1

    yellow_cards = MatchEvent.objects.filter(
        team=team,
        event_type=MatchEvent.EventType.YELLOW_CARD
    ).count()

    red_cards = MatchEvent.objects.filter(
        team=team,
        event_type__in=[
            MatchEvent.EventType.RED_CARD,
            MatchEvent.EventType.SECOND_YELLOW_RED,
        ]
    ).count()

    goals_scored_events = MatchEvent.objects.filter(
        team=team,
        event_type__in=[
            MatchEvent.EventType.GOAL,
            MatchEvent.EventType.PENALTY_GOAL,
            MatchEvent.EventType.OWN_GOAL,
        ]
    ).count()

    return {
        "total_matches": total_matches,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goal_difference": goals_for - goals_against,
        "yellow_cards": yellow_cards,
        "red_cards": red_cards,
        "goals_scored_events": goals_scored_events,
        "recent_matches": recent_matches,
        "form_labels": form_labels,
        "form_points": form_points,
        "goals_for_series": goals_for_series,
        "goals_against_series": goals_against_series,
    }