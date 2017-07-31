import os, sys
import json
from info.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import string
import re
import datetime


'''==================='''
'''====READ CAST======'''
'''==================='''
@api_view(['GET','POST'])

def read_cast(request):							#read CASTTT

	
	import ipdb; ipdb.set_trace()


	f = open('/Users/paramvirgill/desktop/castfinal.json', 'r')	

	counter = 0					
	json_string = f.read()																
	f.close()
	data = json.loads(json_string)
	profile_picture = None
	feat_photoss = None
	
	for item in data:
		counter+=1
		print counter
		for key in item:
			if key == 'category':
				d1 = item[key]
				cat_list = []
				for i in d1:
					c1 = i.encode('utf-8')
					s1 = c1[1:]
					cat_list.append(s1)	
							
			elif key == 'bio':
				d2 = str(item[key])
				d13 = d2.replace("u'","").replace("', u'\\n']","").replace("[u\\n","").replace("\\n","").replace("[u","").strip("[").strip()

				bioo = d13[:-7].lstrip()

			elif key == 'sun_sign':
				d3 = str(item[key])
				sun_signn = d3[3:-2]

			elif key == 'name':
				d4 = item[key]

				try:
					namee = d4[0].encode('ascii','ignore')     
				except:
					namee = d4

			elif key =='feat_photos':
				d5 = str(item[key])
				d15 = d5.replace("[u'","").replace("']","")
				feat_photoss = d15

			elif key =='height':
				d6 = str(item[key])
				d11 = d6.replace("u'n            ', u'n","").replace("xa0","").replace("[u'","").replace("']","").replace("',","").rstrip('\n').strip().replace("\\","").replace("x","").replace("b","").replace("d","").replace("c","")
				c11 = d11.lstrip()
				e11 = re.findall(r'\d.\d.',c11)
				x11 = str(e11)[2:-8]
				heightt = x11.replace("\\","").strip(",").strip("'")

			elif key =='date_of_birth':
				d7 = str(item[key])
				
				try:
					d19 = d7.replace("[u'","").replace("' u'","").replace("']","").replace("u'","").strip("'").replace("'","")
					date_of_birthh = d19
					date_of_birthh = datetime.datetime.strptime(d19,'%B %d, %Y')
				except:
					
					date_of_birthh = None

			elif key =='place_of_birth':
				d8 = str(item[key])
				d12 = d8.replace("[u","").replace("']","").strip("'")
				place_of_birthh = d12

			
			elif key == 'feat_photo_file':
				print '================FOUND FEAT-PHOTO-FILE'
				for value in item[key]:
					print value
					for microvalue in value:
						if microvalue =='path':
							print '=============FOUND PATHH==========='
							g1 = value[microvalue]
							print "==============micro value=",g1
							profile_picture = g1				
				
	
		try:
				art_obj=Artist.objects.get(name=namee)
		except:
				s, art_obj=Artist.objects.get_or_create(
					name=namee,
					bio=bioo,
					date_of_birth=date_of_birthh, 
					sun_sign=sun_signn,
					height=heightt, 
					feat_photos=feat_photoss,
					place_of_birth=place_of_birthh,
					profile_pic = profile_picture,
					
					)
				art_obj=Artist.objects.get(name=namee)

				if cat_list:
					art_obj.category.clear()
					for i in cat_list:
						try:
							cat_obj = Category.objects.get(name = i)
							art_obj.category.add(cat_obj)

						except:
							print"   "



			
	return Response({'message':'Products saved succesfully', 'status':200})		


'''==================='''
'''====READ MOVIE======'''
'''==================='''

@api_view(['GET','POST'])									
def read_movie(request):

	counter = 0
	import ipdb; ipdb.set_trace()
	f = open('/Users/paramvirgill/desktop/moviefinal.json', 'r')						
	json_string = f.read()																
	f.close()
	try:
		data = json.loads(json_string)
		for item in data:
			
			counter +=1
			print counter
			for key in item:


				if key == 'rating':
					d1 = str(item[key])
					c1 = d1.strip("[").replace("u'","").replace("']","").strip("]")
					rating = c1

				# elif key == 'writers':
				# 	d2 = str(item[key])
				# 	writers = d2	

				elif  key == 'language':
					d3 = item[key]
					lang_list = []
					for i in d3:
						c3 = i.encode('utf-8')
						lang_list.append(c3)

				elif key =='cast':
					d13 = item[key]
					cast_list = []	
					for i in d13:
						c13 = i.encode('utf-8')	
						cast_list.append(c13)

				elif key == 'actors':
					d20 = item[key]
					actor_list = []
					for i in d20:
						c20 = i.encode('utf-8')						
						actor_list.append(c20)



				elif key == 'name':
					d4 = item[key]
					try:
						name = d4[0].encode('ascii','ignore')
					except:
						name = d4	

			

				elif key =='boxofficecollection':
					d5 = item[key]
					try:
						boxofficecollection = str(d5[1]).lstrip()
					except:
						boxofficecollection = str(d5).lstrip()

					if not boxofficecollection:
						boxofficecollection = ""	
																		
				elif key =='short_desc':
					
					d6 = str(item[key])
					c6 = d6.replace("[u'","").replace("']","").strip(" ").replace('\n','')
					c7 = d6[5:-2]
					try:
						value = c7.index('\n')
						short_desc = c7[:value].lstrip()
					except:
						short_desc = c7.lstrip()	

				
				elif key =='feat_video':
					d7 = str(item[key])
					feat_video = d7.replace("[u'","").replace("']","")


				elif key =='year':
					d8 = str(item[key])
					c4 = d8.strip("[").replace("u'","").replace("']","")
					yearr = c4

				elif key == 'storyline':
					d9 = str(item[key])
					
					a10 = d9.replace("[u'","").replace("']","").replace("<p>","").replace("</p>","").replace("\\","").strip("]")

					try:
						val = a10.index("<em")
						storyline = a10[1:val]
					except:
						storyline = a10[1:]		


				elif key =='director':
					d10 = str(item[key])
					director = d10
					d111 = item[key]
					director_list = []	
					for i in d111:
						c111 = i.encode('utf-8')	
						director_list.append(c111)	

				elif key =='writers':

					d11 = str(item[key])
					writers = d11
					d11 = item[key]
					writer_list = []	
					for i in d11:
						c11 = i.encode('utf-8')	
						writer_list.append(c11)	

				elif key =='duration':
					d12 = str(item[key])					
					c12 = d12.replace("[u'","").replace("']","").strip(" ").strip('\n')
					c13  = c12[2:]
					c14= c13[:-2]
					duration = c14.lstrip()

					if not duration:
						duration = ""

				elif key =='genre':
					d14 = item[key]
					
					gen_list = []
					for i in d14:
						c14 = i.encode('utf-8')
						gen_list.append(c14)

				elif key =='releaseDate':
					d15 = str(item[key])
					try:
						x = re.findall('\d+',d15)
						start = d15.index(x[0])
						end = d15.index(x[1])+3
						new_releaseDate = d15[start:end+1]
						releaseDate = datetime.datetime.strptime(new_releaseDate,'%d %B %Y')
						print releaseDate
					except:
						new_releaseDate = ''	

				elif key =='duration':
					d16 = item[key]
					duration = d16.replace("[u'","").replace("']","").strip(" ")

					if not duration:
						duration = ""
					
				elif key =='feat_photo':
					d17 = str(item[key])
					feat_photo = d17.replace("[u'","").replace("']","")
			

				elif key == 'certificate':

					d19 = str(item[key])

					certificate = d19.replace("[u'","").replace("']","")		

					if not certificate:
						certificate = ""

				elif key == 'feat_photo_file':
					print '================FOUND FEAT-PHOTO-FILE'
					for value in item[key]:
						print value
						for microvalue in value:
							if microvalue =='path':
								print '=============FOUND PATHH==========='
								g1 = value[microvalue]
								print "==============micro value=",g1
								profile_picture = g1


		
			
			try:
				
				prod_obj=Movie.objects.get(title = name)

			except:
				
				s, prod_obj = Movie.objects.get_or_create(
						
					title = name ,
					year = yearr ,
					rating = rating,
					short_desc = short_desc,	
					storyline = storyline,
					duration = duration,
					release_date = releaseDate ,
					boxoffice_collection = boxofficecollection,
					feat_photos = feat_photo, 
					feat_video = feat_video, 	
					certificate = certificate,
					profile_pic = profile_picture,
									)
				prod_obj=Movie.objects.get(title = name)

				if lang_list:
					prod_obj.lang.clear()
					for i in lang_list:
						try:
							lang_obj = Language.objects.get(name=i)
							prod_obj.lang.add(lang_obj)
						except:
							print""

				if gen_list:
					prod_obj.genre.clear()
					for i in gen_list:
						try:

							genre_obj = Genre.objects.get(name = i)

							prod_obj.genre.add(genre_obj)
						except:
							print""

				if cast_list:
					prod_obj.cast.clear()
					for i in cast_list:
						try:

							cast_obj = Artist.objects.get(name = i)
						
							prod_obj.cast.add(cast_obj)
						except:
							print"   "

				if actor_list:
					prod_obj.actors.clear()
					for i in actor_list:
						try:

							cast_obj = Artist.objects.get(name = i)
						
							prod_obj.actors.add(cast_obj)
						except:
							print"   "


				if director_list:
					prod_obj.director.clear()
					for i in director_list:
						try:

							cast_obj = Artist.objects.get(name = i)
						
							prod_obj.director.add(cast_obj)
						except:
							print"   "
				
				if writer_list:
					prod_obj.writers.clear()
					for i in writer_list:
						try:

							cast_obj = Artist.objects.get(name = i)
						
							prod_obj.writers.add(cast_obj)
						except:
							print"   "						

	except Exception as e:
		print "=====Excption=========", e
	

	return Response({'message': 'Prodcuts save successfully', 'status':200})					
					

'''==================='''
'''=READ CAST IMAGES=='''
'''==================='''

@api_view(['GET','POST'])									
def read_castimg(request):
	import ipdb; ipdb.set_trace()
	f = open('/Users/paramvirgill/desktop/castimg.json', 'r')						
	json_string = f.read()																
	f.close()
	try:
		data = json.loads(json_string)
		for item in data:
			print"=====ITEM=====",item
			for key in item:
			

				if key == 'name':
					d4 = str(item[key])
					try:
						name = d4[0].encode('ascii','ignore')
					except:
						name = d4
					
				elif key =='image':
					d17 = str(item[key])
					feat_photo = d17.replace("[u'","").replace("']","")

			try:
				
				prod_obj=ArtistImage.objects.get(name = name)

			except:
				
				s, prod_obj = ArtistImage.objects.get_or_create(
						
					name = name ,

					img = feat_photo, 
					
									)
				


	except Exception as e:
		print "=====Excption=========", e
	

	return Response({'message': 'Prodcuts save successfully', 'status':200})

	
'''==================='''
'''====READ NEWS======'''
'''==================='''

@api_view(['GET','POST'])									
def read_news(request):
	import ipdb; ipdb.set_trace()
	import re
	f = open('/Users/paramvirgill/desktop/new.json', 'r')						
	json_string = f.read()																
	f.close()
	try:
		data = json.loads(json_string)
		for item in data:
			print"=====ITEM=====",item
			for key in item:
			

				if key == 'title':
					d1 = str(item[key])
					title = d1[3:-2]
					
				elif key =='description':
					d2 = str(item[key])
					x3 = d2.replace("\\n","").replace("\\","")
					c3 = x3.replace("<BR","").replace("</BR","").replace(">>","").replace("<br>","").replace("<i>","").replace("</i>","")
					description = c3[3:-2]

				elif key =='link':
					d3 = str(item[key])
					link = d3[3:-2]

				elif key =='pubdate':
					d4 = str(item[key])
					
					pubdate = d4[3:-2]

				elif key =='image':
					d5 = str(item[key])
					
					c5 = d5.replace("<url","").replace("</url","").replace("<","")
					image = c5[4:-3]

					

			
			try:
				
				prod_obj=News.objects.get(title = title)

			except:
				
				s, prod_obj = News.objects.get_or_create(
						
					title = title ,

					content = description, 

					source_url = link,

					image_url = image,

					timestamp = pubdate,


					
									)
				


	except Exception as e:
		print "=====Excption=========", e
	

	return Response({'message': 'Prodcuts save successfully', 'status':200})


'''==================='''
'''===READ DIRECTOR==='''
'''==================='''	

@api_view(['GET','POST'])

def read_director(request):							


	import ipdb; ipdb.set_trace()
		
	f = open('/Users/paramvirgill/desktop/writer.json', 'r')						

	json_string = f.read()																
	f.close()
	data = json.loads(json_string)
	
	feat_photoss = None
	profile_picture = None
	for item in data:
		for key in item:

			if key == 'category':
				d1 = item[key]
				cat_list = []
				for i in d1:
					c1 = i.encode('utf-8')
					s1 = c1[1:]
					cat_list.append(s1)	
							
			if key == 'bio':
				d2 = str(item[key])
				d13 = d2.replace("u'","").replace("', u'\\n']","").replace("[u\\n","").replace("\\n","").replace("[u","").strip("[").strip()

				bioo = d13[:-7].lstrip()

			if key == 'sun_sign':
				d3 = str(item[key])
				sun_signn = d3[3:-2]

			if key == 'name':
				d4 = item[key]

				
				try:
					namee = d4[0].encode('ascii','ignore')     
				except:
					namee = d4

			if key =='feat_photos':
				d5 = str(item[key])
				d15 = d5.replace("[u'","").replace("']","")
				feat_photoss = d15

			
			if key =='date_of_birth':
				d7 = str(item[key])
				try:
					d19 = d7.replace("[u'","").replace("' u'","").replace("']","").replace("u'","").strip("'").replace("'","")
					date_of_birthh = d19
					date_of_birthh = datetime.datetime.strptime(d19,'%B %d, %Y')
				except:
					date_of_birthh = None

			if key =='place_of_birth':
				d8 = str(item[key])
				d12 = d8.replace("[u","").replace("']","").strip("'")
				place_of_birthh = d12

			elif key == 'feat_photo_file':
				print '================FOUND FEAT-PHOTO-FILE'
				for value in item[key]:
					print value
					for microvalue in value:
						if microvalue =='path':
							print '=============FOUND PATHH==========='
							g1 = value[microvalue]
							print "==============micro value=",g1
							profile_picture = g1				
				
		try:
				art_obj=Artist.objects.get(name=namee)

		except:
				s, art_obj=Artist.objects.get_or_create(
					name=namee,
					bio=bioo,
					date_of_birth=date_of_birthh, 
					sun_sign=sun_signn,
					feat_photos=feat_photoss,
					place_of_birth=place_of_birthh,
					profile_pic = profile_picture,
					
					)
				art_obj=Artist.objects.get(name=namee)

				if cat_list:
					art_obj.category.clear()
					for i in cat_list:
						try:
							cat_obj = Category.objects.get(name = i)
							print cat_obj
							art_obj.category.add(cat_obj)
						except:
							print"   "



			
	return Response({'message':'Products saved succesfully', 'status':200})		

'''==================='''
'''==READ SOUNDTRACK=='''
'''==================='''


@api_view(['GET','POST'])

def read_soundtrack(request):							#read CASTTT
	import ipdb; ipdb.set_trace()
	f = open('/Users/paramvirgill/desktop/musiccc.json', 'r')	
	counter = 0					
	json_string = f.read()																
	f.close()
	data = json.loads(json_string)
	
	for item in data:
		counter+=1
		print counter
		for key in item:
			if key == 'name_movie':
				d1 = str(item[key])
				c1 = d1[3:-2]
				x = c1.index("(")
				name_mov = c1[:x]
							
			elif key == 'singer':
				d2 = str(item[key])
				singer = d2[3:-2].replace("u'","")

			elif key == 'name_song':
				d3 = str(item[key])
				c3 = d3[3:-2]
				try:				
					y = c3.index("(")
					name_song = c3[:y]
				except:
					name_song = c3	


	
		try:
				art_obj=Soundtrack.objects.get(name=name_song)
		except:
				s, art_obj=Soundtrack.objects.get_or_create(
					name_movie=name_mov,
					singer= singer,
					name = name_song, 
				)

				# art_obj1 = Soundtrack.objects.get(name  = name_song)
				# print "========================", art_obj1
				# # art_obj1.name_movie.clear()
				# try:
				# 	cat_obj = Movie.objects.get(title = name_mov)
				# 	print "====================",cat_obj
				# 	art_obj1.name_movie.add(cat_obj)
				# except:
				# 	print"   "

		




	


		

