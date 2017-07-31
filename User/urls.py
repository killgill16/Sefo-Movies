from django.conf.urls import include,url
from . import views

urlpatterns = [

    url(r'^edit_profile/$', views.edit_profile, name = 'edit_profile'),
    url(r'^view_profile/$', views.view_profile, name = 'view_profile'),

    url(r'^add_to_watchlist/$', views.add_to_watchlist, name = 'add_to_watchlist'),
    url(r'^get_user_watchlist/$', views.get_user_watchlist, name = 'get_user_watchlist'),

    url(r'^add_review/$', views.add_review, name = 'add_review'), # provide a movie as param with a rating
    url(r'^get_user_reviews/$', views.get_user_reviews, name = 'get_user_ratings'),


   ]