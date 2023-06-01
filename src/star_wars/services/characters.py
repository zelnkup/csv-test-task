import asyncio
import uuid
from dataclasses import dataclass
from math import ceil

import petl as etl
from django.core.files.base import ContentFile
from petl import MemorySource

from src.integrations.sw_api.client import ClientMode, StarWarsClient
from src.star_wars.models import CollectionRequest

__all__ = ("GetCharactersService", "SaveCharactersToCSVService")


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


@dataclass
class SaveCharactersToCSVService:
    characters: dict
    memory_source = MemorySource()

    def __call__(self) -> CollectionRequest:
        self.table = self._generate_table()
        return self.create_collection()

    def _generate_table(self):
        table = etl.fromdicts(self.characters)
        return etl.tocsv(table, source=self.memory_source)

    def get_file_name(self) -> str:
        return uuid.uuid4().hex + ".csv"

    def create_collection(self):
        content_file = ContentFile(
            self.memory_source.getvalue(), name=self.get_file_name()
        )
        return CollectionRequest.objects.create(file=content_file)
