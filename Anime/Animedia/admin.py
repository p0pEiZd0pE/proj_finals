from django.contrib import admin
from .models import Anime, Genre, Studio


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('genre',)
    list_display = ('genre',)

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    search_fields = ('studio_name',)
    list_display = ('studio_name',)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    search_fields = ('title', 'studios',)
    list_display = ('title', 'studios',)