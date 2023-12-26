from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import GenreSerializer, StudioSerializer, AnimeSerializer
from .models import Anime, Genre, Studio

class GenreViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'
    
class StudioViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'

class AnimeViewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    page_query_param = 'p'

class Genres(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = GenreViewPagination

class Studios(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    pagination_class = StudioViewPagination

class Titles(ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    pagination_class = AnimeViewPagination
