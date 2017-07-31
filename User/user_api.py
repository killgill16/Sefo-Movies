from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from .models import *
from django.http.response import HttpResponse
import json
import datetime



'''==================='''
'''===REVIEW DETAIL==='''
'''==================='''	

@api_view(['GET','POST'])					
def user_review_detail(request):
	try:
		rev_obj = Review.objects.all()	
		review_detail = []
		for obj in rev_obj:
			review = {}
			review['movie_title'] = obj.name
			review['review_title'] = func1(obj.known_for.all())
			review['user'] = obj.slug
			review['rating'] = obj.date_of_birth
			review['content'] = func1(obj.category.all())
			review['timestamp'] = obj.feat_photos
					
			review_detail.append(review)

			
		data = {'status_code':200,'movie_detail': review_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details")	



'''==================='''
'''===REVIEW LIST====='''
'''==================='''	
@api_view(['GET'])					
def user_review_list(request):
	try:
		rev_obj = Review.objects.all()	
		review_detail = []
		for obj in rev_obj:
			review = {}
			review['user'] = obj.user
			review['rating'] = obj.rating
			review['content'] = obj.rating
			review['timestamp'] = obj.timestamp
			review['movie_title'] = obj.movie_title
			review['review_title'] = obj.review_title
					
			review_detail.append(review)

		data = {'status_code':200,'movie_detail': review_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details")			


'''==================='''
'''===COLLECTION====='''
'''==================='''	

@api_view(['GET'])					
def user_collections(request):
	try:
		collection_object = Collection.objects.all()	
		collection_detail = []
		for obj in collection_object:
			collection = {}
			collection['collection_name'] = obj.collection_name
			collection['name'] = obj.name
			collection['description'] = obj.description
			collection['user'] = obj.feat_photos
			collection['timestamp'] = obj.timestamp
					
			collection_detail.append(collection)

		data = {'status_code':200,'movie_detail': review_detail}		
		return Response(data, status=status.HTTP_201_CREATED)

	except Exception as ex:
		print ex
		return HttpResponse("Exception while fetching details")			


'''==================='''
'''===REVIEW SAVE==='''
'''==================='''	

@api_view(['POST'])					
def user_review_save(request):
	try:
		load = json.loads(request.body)
		rating = load.get('rating')
		device_id = load.get('device_id')
		content = load.get('content')
		review_title = load.get('review_title')
		movie_title = load.get('movie_title')

		user_obj = UserProfile.objects.get(device_id = device_id)
		movie_obj = Movie.objects.get(title = movie_title)
	
		
		s, review_obj = Review.objects.get_or_create(
				
			review_title = review_title ,
			content = content, 
			rating = rating,
			user = user_obj,
			movie_title = movie_obj,
			)

		return Response("Data Posted", status=status.HTTP_201_CREATED)			

	except Exception as ex:
		print ex
		return HttpResponse("Exception while posting details")



