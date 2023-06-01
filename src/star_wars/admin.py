from django.contrib import admin

from src.star_wars.models import CollectionRequest


@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    pass
