from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from .models import *
from django.http.response import HttpResponse
from django.forms.models import model_to_dict   
from datetime import date, timedelta 
import datetime
from django.db.models import Q



def func1(parameter):				#to get unicode from many to many models
	val = parameter
	list1=[]
	for i in val:
		list1.append(i.name)
	return list1	


'''==================='''
'''===MOVIE API==='''
'''==================='''	

@api_view(['GET','POST'])	
def movie_detail(request):				
	try:
		namee = request.GET['name']
		print "============",namee
		if not namee:
			return HttpBadRequest("Enter name")

		mov_obj = Movie.objects.filter(title__startswith = namee)
		movie_detail = []
		for obj in mov_obj:
			x = func1(obj.genre.all())
			movie = {}
			movie['title'] = obj.title
			movie['year'] = obj.year
			movie['rating'] = obj.rating
			movie['short_desc'] = obj.short_desc
			movie['storyline'] = obj.storyline
			movie['category'] = obj.category
			movie['picture']  = obj.feat_photos
			movie['language'] = func1(obj.lang.all())
			movie['genre'] = func1(obj.genre.all())
			movie['release_date'] = obj.release_date
			movie['cast'] = func1(obj.cast.all())
			movie['director'] = func1(obj.director.all())
			movie['writer'] = func1(obj.writers.all())
			movie['boxofficecollection'] = obj.boxoffice_collection
			movie['certificate'] = obj.certificate
			movie['slug'] = obj.slug


			movie_detail.append(movie)

		review_obj = Reviwe	
			
		data = {'status_code':200,'movie_detail': movie_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		
		print ex
		return HttpResponse("Exception while fetching details") 	

'''==================='''
'''===MOVIE LIST==='''
'''==================='''	

@api_view(['GET','POST'])					
def movie_list(request):
	try:
		try:
			genree = request.GET['genre']
			mov_obj = Movie.objects.filter(genre__name__startswith = genree).order_by('release_date')
		except:
			namee = request.GET['name']
			mov_obj = Movie.objects.filter(title__startswith = namee).order_by('release_date')

		movie_detail = []
		for obj in mov_obj:
			movie = {}
			movie['title'] = obj.title
			movie['slug'] = obj.slug
			movie['picture']  = obj.feat_photos
			movie['rating'] = obj.rating

			movie_detail.append(movie)			
			print movie_detail

		data = {'status_code':200,'movie_detail': movie_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 


'''==================='''
'''===ARTIST LIST==='''
'''==================='''

@api_view(['GET','POST'])					
def artist_list(request):
	try:
		art_obj = Artist.objects.filter( category__name__contains = "Actor")
		artist_detail = []
		for obj in art_obj:
			artist = {}
			artist['name'] = obj.name
			artist['slug'] = obj.slug

			artist_detail.append(artist)
			print artist_detail

		data = {'status_code':200,'movie_detail': artist_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 					
		

'''==================='''
'''===ARTIST DETAIL==='''
'''==================='''	'''reverse query not workin'''

@api_view(['GET','POST'])					
def artist_detail(request):
	try:
		namee = request.GET['name']
		print "============",namee
		if not namee:
			return HttpBadRequest("Enter name")

		art_obj = Artist.objects.filter(name__startswith = namee)

		artist_detail = []
		for obj in art_obj:
			artist = {}
			artist['name'] = obj.name
			artist['slug'] = obj.slug
			artist['bio'] = obj.bio
			artist['date_of_birth'] = obj.date_of_birth
			artist['category'] = func1(obj.category.all())
			artist['height'] = obj.height
			artist['feat_photos'] = obj.feat_photos
			artist['place_of_birth'] = obj.place_of_birth
			# artist['movies'] = obj.movie_set.all		#REVERSE QUERY NOT WORKING

			artist_detail.append(artist)

		data = {'status_code':200,'movie_detail': artist_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		
		print ex
		return HttpResponse("Exception while fetching details") 			
	 
'''==================='''
'''===NEWS==='''
'''==================='''	
@api_view(['GET','POST'])					
def news(request):
	try:
		news_obj = News.objects.all()
		news_detail = []
		for obj in news_obj:
			news = {}
			news['title'] = obj.title
			news['content'] = obj.content
			news['source_url'] = obj.source_url
			news['image_url'] = obj.source_url
			news['timestamp'] = obj.timestamp

			news_detail.append(news)
			print news_detail

		data = {'status_code':200,'news_detail': news_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 

'''==================='''
'''===ARTIST BIRTH==='''
'''==================='''	
@api_view(['GET','POST'])					# ARTIST BIRTHDAY
def artist_birth(request):

	try:
		
		today = date.today()
		# forty_days = today-datetime.timedelta(days=)

		# art_obj = Artist.objects.filter(Q(date_of_birth__day__range = [forty_days.day, today.day]) and Q(date_of_birth__month__range =[forty_days.month, today.month])) 
		art_obj = Artist.objects.filter( Q(date_of_birth__day = today.day) and Q(date_of_birth__month =today.month) ) 

		artist_detail = []
		for obj in art_obj:

			artist = {}
			artist['name'] = obj.name
			artist['slug'] = obj.slug
			artist['bio'] = obj.bio
			artist['date_of_birth'] = obj.date_of_birth
			artist['category'] = func1(obj.category.all())
			artist['height'] = obj.height
			artist['feat_photos'] = obj.feat_photos
			artist['place_of_birth'] = obj.place_of_birth
			artist_detail.append(artist)

		
		data = {'status_code':200,'movie_detail': artist_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		
		print ex
		return HttpResponse("Exception while fetching details")		

'''==================='''
'''===MOVIE TO BE RELEASED==='''
'''==================='''	
@api_view(['GET','POST'])							
def movie_tobereleased(request):
	try:
		today = datetime.date.today()
		# r_date = today.year,"-",today.month+3,"-",today.date
		# mov_obj = Movie.objects.filter(release_date__month__range = [today__month , today__month+3])  
		current_year = today.year
		current_month = today.month
		current_day = today.day
		mov_obj = Movie.objects.filter(release_date__range = [today+datetime.timedelta(days=45), today] )
		movie_detail = []
		for obj in mov_obj:
			
			movie = {}
			movie['title'] = obj.title
			movie['slug'] = obj.slug
			movie['picture']  = obj.feat_photos
			movie['rating'] = obj.rating
			movie_detail.append(movie)

		data = {'status_code':200,'movie_detail': movie_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 

'''==================='''
'''===MOVIE IN THEATHRE==='''
'''==================='''	

@api_view(['GET','POST'])							
def movie_intheatre(request):
	try:
		today = datetime.date.today()
		mov_obj = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today])
		movie_detail = []
		for obj in mov_obj:
			movie = {}
			movie['title'] = obj.title
			movie['slug'] = obj.slug
			movie['picture']  = obj.feat_photos
			movie['rating'] = obj.rating
			movie_detail.append(movie)
			print movie_detail

		data = {'status_code':200,'movie_detail': movie_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 


'''==================='''
'''===DIRECTOR LIST==='''
'''==================='''	

@api_view(['GET','POST'])					
def director_list(request):
	try:
		art_obj = Artist.objects.filter( category__name__contains = "Director")			
		artist_detail = []
		for obj in art_obj:
			artist = {}
			artist['name'] = obj.name
			artist['slug'] = obj.slug
			artist['feat_photos'] = obj.feat_photos
			artist_detail.append(artist)

			data = {'status_code':200,'movie_detail': artist_detail}		
			return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details")		

@api_view(['GET','POST'])					
def director_detail(request):

		try:
			art_obj = Artist.objects.filter( category__name__contains = "Director")			
			artist_detail = []
			for obj in art_obj:
					artist = {}
					artist['name'] = obj.name
					artist['known_for'] = func1(obj.known_for.all())
					artist['slug'] = obj.slug
					artist['bio'] = obj.bio
					artist['date_of_birth'] = obj.date_of_birth
					artist['category'] = func1(obj.category.all())
					artist['feat_photos'] = obj.feat_photos
					artist['place_of_birth'] = obj.place_of_birth
					artist_detail.append(artist)

			data = {'status_code':200,'movie_detail': artist_detail}		
			return Response(data, status=status.HTTP_201_CREATED)

		except Exception as ex:
			print ex
			return HttpResponse("Exception while fetching details")



'''==================='''
'''===POPULAR MOVIE==='''
'''==================='''	

@api_view(['GET','POST'])							
def movie_popular(request):
		try:
			today = datetime.date.today()

			mov_obj = Movie.objects.filter(release_date__range = [today-datetime.timedelta(days=21), today]).order_by('rating')
			
			movie_detail = []
			for obj in mov_obj:
				
				movie = {}
				movie['title'] = obj.title
				movie['slug'] = obj.slug
				movie['picture']  = obj.feat_photos
				movie['rating'] = obj.rating
				movie_detail.append(movie)
				print movie_detail

			data = {'status_code':200,'movie_detail': movie_detail}		
			return Response(data, status=status.HTTP_201_CREATED)

		except Exception as ex:
			
			print ex
			return HttpResponse("Exception while fetching details") 

'''==================='''
'''===MOVIE SLUG==='''
'''==================='''	

@api_view(['GET','POST'])					
def movie_slug(request):
	try:
		namee = request.GET['slug']
		mov_obj = Movie.objects.filter(slug = namee)

		movie_detail = []
		for obj in mov_obj:
			movie = {}
			movie['title'] = obj.title
			movie['slug'] = obj.slug
			movie['picture']  = obj.feat_photos
			movie['rating'] = obj.rating

			movie_detail.append(movie)			
			print movie_detail

		data = {'status_code':200,'movie_detail': movie_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details") 










