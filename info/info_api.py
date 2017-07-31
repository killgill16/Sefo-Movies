from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from .models import *
from django.http.response import HttpResponse
from django.forms.models import model_to_dict   
import datetime



@api_view(['GET','POST'])					# ARTIST BIRTHDAY
def user_review(request):

		try:

			
			art_obj = Artist.objects.filter( category__name__contains = "Director")			#manytomany
			
			
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

			
				# print artist_detail

			data = {'status_code':200,'movie_detail': artist_detail}		
			return Response(data, status=status.HTTP_201_CREATED)

		except Exception as ex:
			
			print ex
			return HttpResponse("Exception while fetching details")	
