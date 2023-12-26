from rest_framework import serializers
from .models import Anime, Genre, Studio

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class StudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = '__all__'