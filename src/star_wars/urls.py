from django.urls import path

from src.star_wars.views import get_characters_csv

urlpatterns = [
    path("async/", get_characters_csv),
]
