from django.conf.urls import patterns, url
from django.views.generic import ListView
from lib.models import Movie, Genre

urlpatterns = patterns('lib.movie.views',
                       url(r'^$',
                           'movie_index', 
                           name='movie_index'),
                       url(r'^all/$',
                           'movie_all',
                           name='movie_all'),
                       url(r'^years/$',
                           'years',
                           name='years'),
                       url(r'^year/(?P<year>\w+)/$',
                           'year',
                           name='year'),
                       url(r'^genres/$',
                           'genres',
                           name='genres'),
                       url(r'^genre/(?P<genre>[\w|\W]+)/$',
                           'genre',
                           name='genre'),
                       url(r'^movie/(?P<idmovie>\w+)/$',
                           'movie',
                           name='movie'),
                       url(r'random/$',
                           'random',
                           name='random'),
                       url(r'download/(?P<idfile>\w+)$',
                           'download',
                           name='download'),
                       )
