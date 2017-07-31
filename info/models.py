from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.files.images import ImageFile
from autoslug import AutoSlugField
# from django_autoslug.fields import AutoSlugField
# from User.models import *


class Genre(models.Model):
	name = models.CharField(max_length = 100, blank = True)		

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length = 100, blank = True)		

	def __str__(self):
		return self.name		

class Category(models.Model):
	name = models.CharField(max_length = 100, blank = True)	

	def __str__(self):
		return self.name

		

class SunSign(models.Model):

	name = models.CharField(max_length = 100, blank = True)	

	def __str__(self):
		return self.name		

		

class News(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	source_url = models.CharField(max_length = 200)
	timestamp = models.CharField(max_length = 200)
	image_url = models.CharField(max_length = 200)
	category = models.CharField(max_length = 200)

	def __str__(self):
		return self.title


class Artist(models.Model):
	name = models.CharField(max_length = 50)
	bio = models.TextField()
	date_of_birth = models.DateField(null = True, blank = True)
	# known_for = models.ManyToManyField(movie_set.all())
	# CATEGORY = (
	# 	('AR','ACTOR'),
	# 	('AS','ACTRESS'),
	# 	('W','WRITER'),
	# 	('S','SOUNDTRACK'),
	# 	('PR','PRODUCER'),
	# 	('DR','DIRECTOR'),
	# 
	# 	)
	category = models.ManyToManyField(Category)	

	# SUN_SIGN = (
	# 	('A','Aries'),
	# 	('T','Tarus'),
	# 	('G','Gemini'),
	# 	('C','Cancer'),
	# 	('L','Leo'),
	# 	('V','Virgo'),
	# 	('L','Libra'),
	# 	('S','Scorpio'),
	# 	('SA','Sagittarius'),
	# 	('C','Capricon'),
	# 	('P','Pisces'),
	# 	('AQ','Aquarius')
	# # 	)
	# sun_sign = models.ForeignKey(SunSign, on_delete = models.CASCADE)	
	sun_sign = models.CharField(max_length = 100, blank = True, null = True)				 
	height = models.CharField(max_length = 200, blank = True, null = True)
	# movies = models.ManyToManyField(Movie, related_name = "art_movie")
	feat_photos = models.CharField(max_length = 200, null = True, blank = True)
	profile_pic = models.ImageField(blank = True, null = True)
	place_of_birth = models.CharField(max_length = 200, blank = True, null = True)
	slug = AutoSlugField(populate_from='name', null=True)	
	did_trivia = models.CharField(max_length = 400, blank = True)

	def __str__(self):
		return self.name

	def get_movies(self):
		return Movie.objects.filter(actors = self)	


		
class Movie(models.Model):	
	title = models.CharField(max_length = 200)
	year = models.CharField(max_length = 150, blank = True)
	rating = models.CharField(max_length = 100, blank = True)
	short_desc = models.CharField(max_length = 400, blank = True)
	storyline = models.TextField()
	actors = models.ManyToManyField(Artist, blank = True, related_name = 'actor+')
	CATEGORY = (
		('M','Movie'),
		('TV','TV Series'),
		('D','Documentary'),
		('W','Web episode'),
		('WE','Web Series')
				)
	category = models.CharField(max_length=100,choices=CATEGORY, default='Movie')
	lang = models.ManyToManyField(Language, blank = True)
	genre = models.ManyToManyField(Genre, blank = True)
	cast = models.ManyToManyField(Artist, blank = True)
	director = models.ManyToManyField(Artist, blank = True, related_name = 'director+')
	writers = models.ManyToManyField(Artist , blank = True , related_name = 'writer+')
	boxoffice_collection = models.CharField(max_length = 150 , blank = True)
	duration = models.CharField(max_length = 150, blank = True)
	release_date = models.DateField(null = True , blank = True, max_length = 100)
	feat_photos = models.CharField(max_length = 500, blank = True, null = True)
	profile_pic = models.ImageField(null = True, blank = True)	
	feat_video = models.CharField(max_length = 500, blank = True)
	video_thumbnail = models.CharField(max_length = 200, blank = True)
	viewsonyoutbe = models.CharField(max_length = 100,   blank = True)
	certificate = models.CharField(max_length = 100, blank = True)
	slug = AutoSlugField(populate_from='title', null=True)	
	total_rating = models.CharField(max_length = 200 , blank = True)
	filming_location = models.CharField(max_length = 200, blank = True)
	budget = models.CharField(max_length = 200, blank = True)
	opening_week = models.CharField(max_length = 200, blank = True)
	nomination = models.CharField(max_length = 300,blank = True)
	production = models.CharField(max_length = 500 , blank = True)
	did_goofs = models.CharField(max_length = 500, blank = True)
	did_trivia = models.CharField(max_length = 500, blank = True)


	def __str__(self):
		return self.title

class Featured(models.Model):
	name = models.ForeignKey(Movie, on_delete = models.CASCADE)		

	def __unicode__(self):
		return unicode(self.name)
		

class Soundtrack(models.Model):	
	# name_movie = models.ForeignKey(Movie, on_delete = models.CASCADE, blank = True, null = True) 
	name_movie = models.CharField(max_length = 200, blank = True, null = True)
	name = models.CharField(max_length = 200, blank =True)
	singer = models.CharField(max_length = 200,blank = True)


	def __str__(self):
		return self.name 


class ArtistImage(models.Model):
	img = models.CharField(max_length = 1000, null = True)
	name = models.CharField(max_length = 200, null = True)			

	def __str__(self):
		return self.name


class MovieImage(models.Model):										#scrapped
	img = models.CharField(max_length = 100)
	name = models.ForeignKey(Movie, on_delete = models.CASCADE)

	def __str__(self):
		return self.name





class Episode(models.Model):
	title = models.ForeignKey(Movie,on_delete = models.CASCADE)
	episode_name = models.CharField(max_length = 300)
	season_number = models.IntegerField()
	duration = models.IntegerField()
	plot = models.TextField(max_length = 200)
	release_date = models.DateField(default = timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.name


# class MovieVideo(models.Model):
# 	vid = models.CharField(max_length = 100)
# 	name = models.ForeignKey(Movie, on_delete  = models.CASCADE)



# class Award(models.Model):
# 	award_show = models.CharField(max_length = 200 )
# 	award_name = models.CharField(max_length = 200)
# 	AWARD_STATUS = (
# 		('N','Nominated'),
# 		('W','Won')
# 		)
# 	award_status = models.CharField(max_length = 1, choices = AWARD_STATUS)
# 	artist = models.ManyToManyField(Artist)
# 	year = models.IntegerField()
# 	title = models.ForeignKey(Movie,on_delete = models.CASCADE)

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()
		
# 	def __str__(self):
# 		return self.award_show

































	

	



