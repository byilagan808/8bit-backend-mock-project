from django.urls import path
from .views import index
from .views import GetTvShows
from .views import index,GetTvShows,GetTvShowsPagination


urlpatterns = [
    path("", index),
    path('api/tv-shows/', GetTvShows.as_view(), name='Tv Shows get api endpoint'),
    path('api/tv-shows/pagination/', GetTvShowsPagination.as_view(), name='Tv Shows pagination get api endpoint')
]

