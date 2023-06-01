import asyncio
from itertools import chain

from django.http import JsonResponse

from src.star_wars.services.characters import GetCharactersService


def get_characters_csv(request):
    async def async_view():
        results = await GetCharactersService().get_characters()
        return JsonResponse(list(chain.from_iterable(results)), safe=False)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        response = loop.run_until_complete(async_view())
    finally:
        loop.close()

    return response
