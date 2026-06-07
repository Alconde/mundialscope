from .clients import FootballDataClient
from .mappers import get_or_create_world_cup_2026, map_match
from .exceptions import DataSyncError


WORLD_CUP_COMPETITION_CODE = "WC"


def import_world_cup_2026_matches():
    client = FootballDataClient()
    tournament = get_or_create_world_cup_2026()

    data = client.get(f"/competitions/{WORLD_CUP_COMPETITION_CODE}/matches")

    matches = data.get("matches", [])
    imported = 0

    for match_data in matches:
        season = match_data.get("season", {})
        if season.get("startDate", "").startswith("2026") or season.get("endDate", "").startswith("2026"):
            map_match(match_data, tournament)
            imported += 1

    return {
        "imported_matches": imported,
        "competition_code": WORLD_CUP_COMPETITION_CODE,
    }