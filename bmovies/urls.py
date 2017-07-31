"""bmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from info import read_api,movie_api
from User import user_api
from info import api
from info.views import MyLoginView, MySignupView
#from . import api


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/signup', MySignupView.as_view(), name = "signup"),
    url(r'^accounts/login', MyLoginView.as_view(), name = "login"),

    url(r'^read_cast/', read_api.read_cast, name = 'read_file'),
    url(r'^read_director/', read_api.read_director, name = 'read_file'),
    url(r'^read_news/', read_api.read_news, name = 'read_news'),
    url(r'^read_movie/', read_api.read_movie, name = 'read_file1'),
    url(r'^read_castimg/', read_api.read_castimg, name = 'read_file2'),
    url(r'^read_soundtrack/', read_api.read_soundtrack, name = 'read_file3'),
    
    
    url(r'^movie_list/', movie_api.movie_list, name = 'movie_list'),
    url(r'^movie_intheatre/', movie_api.movie_intheatre, name = 'movie_intheatre'),
    url(r'^movie_upcoming/', movie_api.movie_tobereleased, name = 'movie_listt'),
    url(r'^artist_birth/', movie_api.artist_birth, name = 'artist_birthdayy'),
    url(r'^artist_list/', movie_api.artist_list, name = 'artist_list'),
    url(r'^artist_detail/', movie_api.artist_detail, name = 'artist_detail'),
    url(r'^movie_detail/', movie_api.movie_detail, name = 'movie_detail'),
    url(r'^movie_popular/', movie_api.movie_popular, name = 'movie_popular'),
    url(r'^movie_slug/', movie_api.movie_slug, name = 'movie_popular'),

    url(r'^user_review_detail/', user_api.user_review_detail, name = 'user_review_detail'),
    url(r'^user_review_list/', user_api.user_review_list, name = 'user_review_list'),
    url(r'^user_review_save/', user_api.user_review_save, name = 'user_review_save'),


    url(r'^newss/', movie_api.news, name = 'news_detail'),

    url(r'^',include('info.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
