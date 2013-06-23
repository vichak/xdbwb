from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render, get_object_or_404
from lib.forms import SearchMovie
from lib.models import Movie, Writerlinkmovie, Genre, Files, Path, Streamdetails
from random import randint
import os

context = {}

@login_required
def movie_index(request):
    nb_movie = Movie.objects.count()
    context["nb_movie"] = nb_movie
    return render(request, 'movies/index.html', context)

def paginator_movie_list(request, movie_list):
    paginator = Paginator(movie_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    context["movie_list"] = movies
    return context

@login_required
def movie_all(request):
    movie_list = Movie.objects.all()
    context = paginator_movie_list(request, movie_list)
    return render(request,
                  'movies/movie_list.html',
                  context)

@login_required
def genres(request):
    context["genre_list"] = Genre.objects.all().order_by('strgenre')
    return render(request,
                  'movies/genre_list.html',
                  context)   

@login_required
def genre(request, genre):
    movie_list = get_list_or_404(Movie, genre__contains=genre)
    context = paginator_movie_list(request, movie_list)
    return render(request,
                  'movies/movie_list.html',
                  context)

@login_required
def years(request):
    context["year_list"] = Movie.objects.values_list('yearreleased', flat=True).order_by('-yearreleased').distinct()
    return render(request,
                  'movies/year_list.html',
                  context)

@login_required
def year(request, year):
    movie_list = get_list_or_404(Movie, yearreleased=year)
    context = paginator_movie_list(request, movie_list)
    return render(request,
                  'movies/movie_list.html',
                  context)
    
def get_movie_context(idmovie):
    movie = get_object_or_404(Movie, idmovie=idmovie)
    streamdetails = Streamdetails.objects.filter(idfile=movie.idfile)
    context["movie"] = movie
    context["streamdetails"] = streamdetails
    return context

@login_required
def movie(request, idmovie):
    context = get_movie_context(idmovie)
    return render(request,
                  'movies/movie.html',
                  context)
    
@login_required   
def random(request):
    context = get_movie_context(randint(1, len(Movie.objects.all())))
    return render(request,
                  'movies/movie.html',
                  context)

@login_required  
def download(request, idfile):
    f = get_object_or_404(Files, idfile=idfile)
    path = get_object_or_404(Path, idpath=f.idpath)
    filepath = os.path.join(path.strpath, f.strfilename)
    wrapper = FileWrapper(file(filepath))
    response = HttpResponse(wrapper, content_type='application/octet-stream')
    response['Content-Length'] = os.path.getsize(filepath)
    response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(filepath)
    return response
