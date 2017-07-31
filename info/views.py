from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from .models import *
import random
import datetime
import random
import requests
from django.db.models import Q
from allauth.account.views import SignupView, LoginView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class MySignupView(SignupView):
	template_name = 'bitmovies/signup.html'


class MyLoginView(LoginView):
	template_name = 'bitmovies/signin.html'

def home(request):

	image = []
	news = News.objects.filter().order_by('-pk')
	news_feautred = News.objects.filter().order_by('-pk')[4:]
	today = datetime.date.today()
	movies_theatre = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('-release_date')
	popular_movies = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('rating').reverse()
	art_birthday = Artist.objects.filter( Q(date_of_birth__day__range = [today.day, today.day+7 ]) and Q(date_of_birth__month =today.month) )
	feat = Featured.objects.all()
	context = {'news':news , 'popular_movies': popular_movies, 'birthday_artist': art_birthday, 'movies_theatre': movies_theatre,'news_feat': news_feautred,'featured':feat}
	template = 'bitmovies/index.html'	
	
	return render(request, template, context)

def news_list(request):
	news_feautred = News.objects.filter().order_by('-pk')
	paginator = Paginator(news_feautred, 16)
	page = request.GET.get('page')
	try:
		mov_obj = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		mov_obj = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		mov_obj = paginator.page(paginator.num_pages)		
	return render(request, 'bitmovies/news.html', {'news':mov_obj})	

def news_detaill(request,id):
	news = News.objects.filter(id = id)
	context = {'news': news}
	return render(request,'bitmovies/news-details.html', context)

def detail_image(request,slug):

	album = get_object_or_404(Post.image, slug = slug)
	return render(request, 'bitmovies/index.html', {'pics':album})


		
	
def movie_detail(request,slug):
	movie = Movie.objects.filter(slug = slug)
	context = {'movies': movie}
	return render (request,'bitmovies/movies-details.html',context)	


def celeb_detail(request,slug):
	celeb = Artist.objects.filter(slug = slug)
	# celeb_movie = Artist.movie_set.all()
	context = {'artists': celeb}
	return render (request,'bitmovies/celeb-details.html',context)	


def list_movie_genre(request,slug):
	mov = Movie.objects.filter(genre__name__startswith = slug).order_by('-release_date')
	paginator = Paginator(mov, 16)
	page = request.GET.get('page')
	try:
		mov_obj = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		mov_obj = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		mov_obj = paginator.page(paginator.num_pages)	


	context = {"genre":slug.capitalize(), 'movies': mov_obj}
	return render(request,'bitmovies/action.html',context)		

def now_showing(request):
	today = datetime.date.today()
	mov_obj = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today])
	context = {'showing': mov_obj}
	return render (request,'bitmovies/nowshowing.html',context)	

def upcoming_movie(request):
	today = datetime.date.today()
	mov_obj = Movie.objects.filter(release_date__range = [today+datetime.timedelta(days=21), today])
	context = {'upcoming': mov_obj}
	return render (request,'bitmovies/upcoming.html',context)

def popular_movies(request):

	today = datetime.date.today()
	mov_obj = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('-rating')	
	context = {'popular': mov_obj}
	return render (request,'bitmovies/popular.html',context)	

def movies_theatre(request):

	today = datetime.date.today()
	movies_theatre = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('-release_date')	
	context = {'popular': movies_theatre}
	return render (request,'bitmovies/theatre.html',context)	

def list_movie_lang(request,slug):
	mov = Movie.objects.filter(lang__name__startswith = slug).order_by('-release_date')
	paginator = Paginator(mov, 16)
	page = request.GET.get('page')
	try:
		mov_obj = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		mov_obj = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		mov_obj = paginator.page(paginator.num_pages)		
	context = {"genre":slug.capitalize(), 'movies': mov_obj}
	return render (request,'bitmovies/action.html',context)


def popular_actors(request):
	mov_obj = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('rating')	
	art_obj = mov_obj.actors.all
	context = {'popular_actors': art_obj}
	return render (request,'bitmovies/popular.html',context)

def search(request):
	title = "Create"
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		movies = Movie.objects.filter(title__icontains=q)
		artists = Artist.objects.filter(name__icontains = q)
		context = {'movie': movies , 'artists': artists}
		template = 'bitmovies/results.html'
		return render(request, template, context)	
	else:
		template = 'bitmovies/index.html'
		context = {'movie': movies , 'artist': artists}
		return render(request, template, context)	

		
def celeb(request):
	today = datetime.date.today()
	art_birthday = Artist.objects.filter( Q(date_of_birth__day = today.day) and Q(date_of_birth__month =today.month))
	art_popular = Movie.objects.filter(release_date__range = [ today-datetime.timedelta(days=21), today]).order_by('-rating')
	# art_obj = art_popular.actors.all
	context = {'art_birthday': art_birthday, 'art_popular' : art_popular}
	return render(request,'bitmovies/celeb.html', context)

def movie(request):
	today = datetime.date.today()
	movies_theatre = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today])
	popular_movies = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('-rating')
	upcoming_movies = Movie.objects.filter(release_date__range = [today,today+datetime.timedelta(days=21)])
	hindi_movies = Movie.objects.filter(Q(lang__name__startswith = "Hindi") and Q(release_date__range =[today-datetime.timedelta(days=100), today])).order_by('-rating')
	context = {'movies_theatre': movies_theatre, 'popular_movies': popular_movies,'upcoming_movies' :upcoming_movies,'hindi_movie':hindi_movies }
	return render(request, 'bitmovies/movies.html', context)








# def artist(request,slug):

# 	artist  =Artist.objects.filter(slug = slug)
# 	context = {"artists": artist}
# 	return render(request,'bitmovies/celeb.html', context )







		
	
			
		





