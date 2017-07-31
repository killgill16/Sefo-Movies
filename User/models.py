from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from info.models import *


_APP_NAME ='core'

# class UserProfile(base_models.UserProfile):
	 
		
#     class Meta(base_models.UserProfile.Meta):
#         app_label = _APP_NAME


class IntegerRangeField(models.IntegerField):
	def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
			self.min_value, self.max_value = min_value, max_value
			models.IntegerField.__init__(self, verbose_name, name, **kwargs)
	
	def formfield(self, **kwargs):
			defaults = {'min_value': self.min_value, 'max_value':self.max_value}
			defaults.update(kwargs)
			return super(IntegerRangeField, self).formfield(**defaults)

	def set_user_pic_path(instance, filename):
		return '{0}/{1}/user'.format(settings.ENV, settings.BRAND)


class BaseModel(models.Model):
	"""
	Base model contains created date and modified date
	"""
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
			abstract = True


class UserProfile(BaseModel):
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	device_id = models.CharField(max_length=50, unique=True, null=True)
	address = models.TextField(blank=True, null=True)
	state = models.CharField(max_length=255, null=True, blank=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	pincode = models.CharField(max_length=15, null=True, blank=True)
	date_of_birth = models.DateTimeField(null=True, blank=True)
	is_email_verified = models.BooleanField(default=False)
	is_phone_verified = models.BooleanField(default=False)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True,related_name='core_users')
	# interests_category = models.ManyToManyField(Category)
	
	image_url = models.ImageField(upload_to='user-images',max_length=200, null=True, blank=True)
	# GENDER_CHOICES = (
	# 		('M', 'Male'),
	# 		('F', 'Female'),
	# 		('X', 'Other'),
	# )
	# gender = models.CharField(max_length=2, choices=GENDER_CHOICES,blank=True, null=True)

class Meta:
	db_table = "bn_userprofile"
	verbose_name_plural = "User Profile"
	abstract = True

	def __unicode__(self):
		return str(self.phone_number or '') + ' ' + self.user.username


class Review(BaseModel):
	movie_title = models.ForeignKey(Movie,on_delete = models.CASCADE)
	review_title = models.CharField(max_length = 30)
	user = models.ForeignKey(UserProfile,on_delete = models.CASCADE)
	rating = models.FloatField(max_length = 10, default = 0)
	content = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.review_title      

class Watchlist(BaseModel):
	movie_title = models.ManyToManyField(Movie)
	user = models.ForeignKey(UserProfile,on_delete = models.CASCADE)
		
	def __str__(self):
		return self.movie_title      


class Collection(models.Model):
	collection_name = models.CharField(max_length = 20)
	# rating = fields.IntegerRangeField(min_value=1, max_value=5)
	rating = models.IntegerField(blank = True,default = 0)
	name_movie = models.ManyToManyField(Movie)  
	description = models.TextField(blank = True,null=True)
	user = models.ForeignKey(UserProfile,on_delete = models.CASCADE)
	timestamp = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.name    



