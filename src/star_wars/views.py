import asyncio
from itertools import chain

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

from src.star_wars.models import CollectionRequest
from src.star_wars.services.characters import (
    GetCharactersService,
    SaveCharactersToCSVService,
)


def get_characters_csv(request):
    async def async_view():
        results = await GetCharactersService().get_characters()
        return list(chain.from_iterable(results))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        characters = loop.run_until_complete(async_view())
    finally:
        loop.close()
    instance = SaveCharactersToCSVService(characters)()
    return HttpResponseRedirect(reverse("character-detail", args=[instance.pk]))


class CharactersListView(ListView):
    model = CollectionRequest
    template_name = "characters.html"


class CharactersDetailView(DetailView):
    model = CollectionRequest
    template_name = "character.html"
