from matches.models import Match


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