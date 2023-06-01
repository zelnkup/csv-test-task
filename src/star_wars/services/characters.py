import asyncio
from math import ceil

from src.integrations.sw_api.client import ClientMode, StarWarsClient


class GetCharactersService:
    def count_characters_pages(self) -> int:
        response = StarWarsClient({"page": 1}).get_characters()
        return ceil(response["count"] / len(response["results"]))

    async def get_characters(self):
        pages_count = self.count_characters_pages()
        tasks = [
            StarWarsClient({"page": page}, mode=ClientMode.ASYNC).get_characters()
            for page in range(1, pages_count + 1)
        ]

        return await asyncio.gather(*tasks)
