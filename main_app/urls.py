from django.urls import path
from .views import index
from .views import GetTvShows

urlpatterns = [
    path("", index),
    path('api/tv-shows/', GetTvShows.as_view(), name='Tv Shows get api endpoint'),
]

