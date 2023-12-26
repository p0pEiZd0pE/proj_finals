from django.urls import path, include
from .views import Titles, Genres, Studios

urlpatterns = [
    path('genre/', Genres.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('genre/<int:pk>/', Genres.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('studio/', Studios.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('studio/<int:pk>/', Studios.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('', Titles.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('<int:pk>/', Titles.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]