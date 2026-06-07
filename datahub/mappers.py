from datetime import date

from django.utils.dateparse import parse_datetime

from matches.models import Match, Tournament
from teams.models import Team
from django.db import IntegrityError, transaction


CONFEDERATION_BY_AREA = {
    "Argentina": Team.Confederation.CONMEBOL,
    "Brazil": Team.Confederation.CONMEBOL,
    "Uruguay": Team.Confederation.CONMEBOL,
    "Colombia": Team.Confederation.CONMEBOL,
    "Ecuador": Team.Confederation.CONMEBOL,
    "Paraguay": Team.Confederation.CONMEBOL,
    "Chile": Team.Confederation.CONMEBOL,
    "Peru": Team.Confederation.CONMEBOL,
    "Bolivia": Team.Confederation.CONMEBOL,
    "Venezuela": Team.Confederation.CONMEBOL,

    "Mexico": Team.Confederation.CONCACAF,
    "United States": Team.Confederation.CONCACAF,
    "USA": Team.Confederation.CONCACAF,
    "Canada": Team.Confederation.CONCACAF,
    "Costa Rica": Team.Confederation.CONCACAF,
    "Panama": Team.Confederation.CONCACAF,
    "Jamaica": Team.Confederation.CONCACAF,
    "Honduras": Team.Confederation.CONCACAF,
    "El Salvador": Team.Confederation.CONCACAF,
    "Guatemala": Team.Confederation.CONCACAF,
    "Trinidad and Tobago": Team.Confederation.CONCACAF,
    "Haiti": Team.Confederation.CONCACAF,
    "Curacao": Team.Confederation.CONCACAF,
    "Curaçao": Team.Confederation.CONCACAF,

    "England": Team.Confederation.UEFA,
    "Spain": Team.Confederation.UEFA,
    "France": Team.Confederation.UEFA,
    "Germany": Team.Confederation.UEFA,
    "Portugal": Team.Confederation.UEFA,
    "Italy": Team.Confederation.UEFA,
    "Netherlands": Team.Confederation.UEFA,
    "Belgium": Team.Confederation.UEFA,
    "Croatia": Team.Confederation.UEFA,
    "Denmark": Team.Confederation.UEFA,
    "Switzerland": Team.Confederation.UEFA,
    "Serbia": Team.Confederation.UEFA,
    "Poland": Team.Confederation.UEFA,
    "Czech Republic": Team.Confederation.UEFA,
    "Czechia": Team.Confederation.UEFA,
    "Austria": Team.Confederation.UEFA,
    "Sweden": Team.Confederation.UEFA,
    "Norway": Team.Confederation.UEFA,
    "Ukraine": Team.Confederation.UEFA,
    "Scotland": Team.Confederation.UEFA,
    "Turkey": Team.Confederation.UEFA,
    "Wales": Team.Confederation.UEFA,
    "Romania": Team.Confederation.UEFA,
    "Slovakia": Team.Confederation.UEFA,
    "Slovenia": Team.Confederation.UEFA,
    "Hungary": Team.Confederation.UEFA,

    "Japan": Team.Confederation.AFC,
    "South Korea": Team.Confederation.AFC,
    "Korea Republic": Team.Confederation.AFC,
    "Australia": Team.Confederation.AFC,
    "Iran": Team.Confederation.AFC,
    "Saudi Arabia": Team.Confederation.AFC,
    "Qatar": Team.Confederation.AFC,
    "United Arab Emirates": Team.Confederation.AFC,
    "Iraq": Team.Confederation.AFC,
    "Uzbekistan": Team.Confederation.AFC,
    "Jordan": Team.Confederation.AFC,
    "Oman": Team.Confederation.AFC,
    "China PR": Team.Confederation.AFC,
    "China": Team.Confederation.AFC,

    "Morocco": Team.Confederation.CAF,
    "Senegal": Team.Confederation.CAF,
    "Nigeria": Team.Confederation.CAF,
    "Tunisia": Team.Confederation.CAF,
    "Algeria": Team.Confederation.CAF,
    "Egypt": Team.Confederation.CAF,
    "Cameroon": Team.Confederation.CAF,
    "Ghana": Team.Confederation.CAF,
    "Ivory Coast": Team.Confederation.CAF,
    "Côte d'Ivoire": Team.Confederation.CAF,
    "South Africa": Team.Confederation.CAF,
    "Mali": Team.Confederation.CAF,

    "New Zealand": Team.Confederation.OFC,
}


STAGE_MAPPING = {
    "GROUP_STAGE": Match.Stage.GROUP,
    "LAST_32": Match.Stage.ROUND_OF_32,
    "LAST_16": Match.Stage.ROUND_OF_16,
    "QUARTER_FINALS": Match.Stage.QUARTERFINAL,
    "SEMI_FINALS": Match.Stage.SEMIFINAL,
    "THIRD_PLACE": Match.Stage.THIRD_PLACE,
    "FINAL": Match.Stage.FINAL,
}

STATUS_MAPPING = {
    "SCHEDULED": Match.Status.SCHEDULED,
    "TIMED": Match.Status.SCHEDULED,
    "IN_PLAY": Match.Status.LIVE,
    "PAUSED": Match.Status.LIVE,
    "FINISHED": Match.Status.FINISHED,
    "POSTPONED": Match.Status.POSTPONED,
    "SUSPENDED": Match.Status.POSTPONED,
    "CANCELLED": Match.Status.CANCELLED,
}


def normalize_fifa_code(team_name, tla):
    if tla:
        return tla[:10]

    cleaned = "".join(ch for ch in team_name.upper() if ch.isalpha())
    return cleaned[:3] if cleaned else "UNK"


def map_confederation(team_data):
    area = team_data.get("area") or {}
    area_name = (area.get("name") or "").strip()

    return CONFEDERATION_BY_AREA.get(area_name, Team.Confederation.UEFA)


def get_or_create_world_cup_2026():
    tournament, _ = Tournament.objects.update_or_create(
        name="FIFA World Cup",
        year=2026,
        defaults={
            "host_country": "United States, Mexico, Canada",
            "tournament_type": Tournament.TournamentType.WORLD_CUP,
            "start_date": date(2026, 6, 11),
            "end_date": date(2026, 7, 19),
            "is_active": True,
        },
    )
    return tournament


def map_team(team_data):
    if not team_data:
        return None

    team_name = (team_data.get("name") or "").strip()
    external_id = str(team_data.get("id")) if team_data.get("id") else None
    tla = (team_data.get("tla") or "").strip()

    if not team_name:
        return None

    fifa_code = normalize_fifa_code(team_name, tla)
    confederation = map_confederation(team_data)

    team = None

    if external_id:
        team = Team.objects.filter(external_id=external_id).first()

    if team is None:
        team = Team.objects.filter(name=team_name).first()

    if team is not None:
        team.external_id = external_id or team.external_id
        team.fifa_code = fifa_code or team.fifa_code
        team.confederation = confederation or team.confederation
        team.is_active = True
        team.save()
        return team

    base_code = fifa_code or "UNK"
    final_code = base_code
    counter = 1

    while Team.objects.filter(fifa_code=final_code).exclude(name=team_name).exists():
        suffix = str(counter)
        final_code = f"{base_code[:max(1, 10 - len(suffix))]}{suffix}"
        counter += 1

    try:
        with transaction.atomic():
            team = Team.objects.create(
                name=team_name,
                fifa_code=final_code,
                confederation=confederation,
                is_active=True,
                external_id=external_id,
            )
        return team
    except IntegrityError:
        existing_team = Team.objects.filter(name=team_name).first()
        if existing_team:
            existing_team.external_id = external_id or existing_team.external_id
            existing_team.fifa_code = final_code or existing_team.fifa_code
            existing_team.confederation = confederation or existing_team.confederation
            existing_team.is_active = True
            existing_team.save()
            return existing_team
        raise

def extract_group_value(group_raw):
    if not group_raw:
        return ""

    group_raw = str(group_raw).strip()

    if group_raw.startswith("GROUP_") and len(group_raw) >= 7:
        return group_raw[-1]

    if len(group_raw) == 1:
        return group_raw

    return ""


def map_match(match_data, tournament):
    home_team_data = match_data.get("homeTeam") or {}
    away_team_data = match_data.get("awayTeam") or {}

    home_team = map_team(home_team_data)
    away_team = map_team(away_team_data)

    if home_team is None or away_team is None:
        return None

    score_data = match_data.get("score", {})
    full_time = score_data.get("fullTime", {}) or {}

    external_id = str(match_data.get("id"))
    utc_date_str = match_data.get("utcDate")
    utc_date = parse_datetime(utc_date_str) if utc_date_str else None

    if utc_date is None:
        return None

    stage_raw = match_data.get("stage")
    status_raw = match_data.get("status")
    group_raw = match_data.get("group") or ""

    venue = match_data.get("venue") or ""
    area = match_data.get("area") or {}
    city = area.get("name", "") if isinstance(area, dict) else ""

    match, _ = Match.objects.update_or_create(
        external_id=external_id,
        defaults={
            "tournament": tournament,
            "home_team": home_team,
            "away_team": away_team,
            "stage": STAGE_MAPPING.get(stage_raw, Match.Stage.GROUP),
            "group": extract_group_value(group_raw),
            "match_date": utc_date,
            "stadium": venue[:120],
            "city": city[:100],
            "status": STATUS_MAPPING.get(status_raw, Match.Status.SCHEDULED),
            "home_score": full_time.get("home") if full_time.get("home") is not None else 0,
            "away_score": full_time.get("away") if full_time.get("away") is not None else 0,
        },
    )
    return match