from dataclasses import dataclass
from enum import Enum
from typing import Optional

from django.conf import settings

from src.integrations.sw_api.http import StarWarsAPIHTTP


class ClientMode(Enum):
    ASYNC = "async"
    SYNC = "sync"


@dataclass
class StarWarsClient:
    params: Optional[dict]
    mode: ClientMode = ClientMode.SYNC
    base_url: str = settings.SW_API_URL
    http = StarWarsAPIHTTP()

    def get_characters(self):
        url = self.base_url + "people/"
        match self.mode:
            case ClientMode.SYNC:
                return self.http.get(url, self.params)
            case ClientMode.ASYNC:
                return self.http.async_get(url, self.params)
