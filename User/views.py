from django.shortcuts import render
from .models import *
from info.models import Movie

def edit_profile(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user = user_object)
    user.username = request.GET.get('name')
    user.image = request.GET.get('image')
    user.save()
	return render(request, 'bitmovies/profile.html', {'news':news_feautred})	

def view_profile(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user = user_object)
	return render(request, 'bitmovies/profile.html', {'user':user.user.username})	

def add_to_watchlist(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user = user_object)
	movie = Movie.objects.filter(title=request.GET.get('movie_name'))
	user_watchlist = Watchlist(user=user)
	user_watchlist.save()
	user_watchlist.movie_title.add(movie)
	return 

def get_user_watchlist(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user=user_object)
	watchlist = Watchlist.objects.filter(user=user)
	movies_list = watchlist.objects.all()
	return 

def add_review(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user=user_object)
    movie = Movie.objects.filter(title=request.GET.get('movie_name'))
    review = Review(user=user)
    review.movie = movie
    review.rating = request.GET.get('rating')
    review.content = request.GET.get('content')
    review.review_title = request.GET.get('review_title')
    review.save()
    return


def get_user_reviews(request):
	username = None
    if not request.user.is_authenticated():
    	return render(request, 'bitmovies/login.html')     
    else:
    	username = request.user.username

    user_object = User.objects.filter(username=username)
    user = UserProfile.objects.filter(user=user_object)
	reviews = Review.objects.filter(user=user)
	content = dict()
	# for review in reviews:
	# 	review.content
	# 	review.review_title
	# 	review.rating
	return 

