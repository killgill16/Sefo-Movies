from django.conf.urls import url

# from .views import MovieListView
from . import api
from . import views
from django.views.generic import ListView,DetailView
from . models import News


urlpatterns = [
    
       url(r'^$', views.home, name = 'home_list'),
       

       url(r'^genre/(?P<slug>[\w-]+)/$', views.list_movie_genre, name = 'action_list'),
       url(r'^language/(?P<slug>[\w-]+)/$', views.list_movie_lang, name = 'action_lang'),
       url(r'^now_showing/', views.now_showing, name = 'now_showing'),
       url(r'^upcoming/', views.upcoming_movie, name = 'upcoming_movie'),
       url(r'^popular/', views.popular_movies, name = 'popular_movie'),
       url(r'^theatre/', views.movies_theatre, name = 'theatre_movie'),

       url(r'^news_list/', views.news_list, name = 'news_list'),
       url(r'^celebs/', views.celeb, name = 'celeb_list'),
       url(r'^movies/', views.movie, name = 'movie_list'),

       url(r'^movie_detaill/(?P<slug>[\w-]+)/$', views.movie_detail, name = 'movie_detail'),
       url(r'^artist_detaill/(?P<slug>[\w-]+)/$', views.celeb_detail, name = 'celeb_detail'),
       url(r'^results/$', views.search, name='results'),

       # url(r'^(?P<pk>\d+)$', DetailView.as_view(model = News, template_name = "info/news-details.html")),
       url(r'^news/(?P<id>\d+)$', views.news_detaill , name = 'news_detaill'),
       
      ]