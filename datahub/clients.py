

    
import requests

from django.conf import settings

from .exceptions import DataSyncError


class FootballDataClient:
    def __init__(self):
        if not settings.ENABLE_EXTERNAL_DATA_SYNC:
            raise DataSyncError("La sincronización externa está desactivada.")
        if not settings.FOOTBALL_DATA_API_KEY:
            raise DataSyncError("FOOTBALL_DATA_API_KEY no está configurada.")

        self.base_url = settings.FOOTBALL_DATA_BASE_URL
        self.headers = {
            "X-Auth-Token": settings.FOOTBALL_DATA_API_KEY,
        }

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        response = requests.get(url, headers=self.headers, params=params or {}, timeout=30)

        if response.status_code >= 400:
            raise DataSyncError(
                f"Error en API football-data.org: {response.status_code} - {response.text}"
            )

        return response.json()