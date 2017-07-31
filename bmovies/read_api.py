import os, sys
import json
from info.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# @api_view(['GET','POST'])

# def read_file(request):

# 	def json_load_byteified(file_handle):

#     		return _byteify(
#       	  	json.load(file_handle, object_hook=_byteify),
#        	 	ignore_dicts=True
#    	 		)

# 	def json_loads_byteified(json_text):
#     		return _byteify(
#         	json.loads(json_text, object_hook=_byteify),
#         	ignore_dicts=True
#     		)

# 	def _byteify(data, ignore_dicts = False):

#     # if this is a unicode string, return its string representation
#     		if isinstance(data, unicode):
#         		return data.encode('utf-8')
#     # if this is a list of values, return list of byteified values
#     		if isinstance(data, list):
#         		return [ _byteify(item, ignore_dicts=True) for item in data ]
#     # if this is a dictionary, return dictionary of byteified keys and values
#     # but only if we haven't already byteified it
#    			if isinstance(data, dict) and not ignore_dicts:

#         			return {
#             	_byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
#             	for key, value in data.iteritems()
#         }
#     # if it's anything else, return it in its original form
#    			return data

#     # json_load_byteified(open('somefile.json'))
	# import ipdb; ipdb.set_trace()

	# f = open('/Users/paramvirgill/desktop/artist.json', 'r')						
	# json_string = f.read()																
	# f.close()
	# data = json.loads(json_string)
	# # data = json_load_byteified(open('artist.json'))
	# for item in data:
	# 	print "#############  ITEM   #############",item
	# 	for key in item:

	# 		# if key == 'category':
	# 		# 	d1 = item[key]
	# 		# 	# cat_list = []
	# 		# 	# for i in d1:
	# 		# 	# 	c1 = i.encode('utf-8')
	# 		# 	# 	s1 = c1.strip("#")
	# 		# 	# 	print s1
	# 		# 	# 	cat_list.append(s1)					


	# 		if key == 'bio':
	# 			d2 = str(item[key])
	# 			d13 = d2.replace("u'","").replace("', u'\n']","").replace("[u\\n","")
	# 			bioo = d13

	# 		if key == 'sun_sign':
	# 			d3 = item[key]
	# 			sun_signn = d3

	# 		if key == 'name':
	# 			d4 = item[key]

	# 			# namee = d4
	# 			try:
	# 				namee = d4[0].encode('ascii','ignore')     #changed index from 0 to 1
	# 			except:
	# 				namee = d4

	# 		if key =='feat_photos':
	# 			d5 = str(item[key])
	# 			d15 = d5.replace("[u'","").replace("']","")
	# 			feat_photoss = d15

	# 		if key =='height':
	# 			d6 = str(item[key])
	# 			d11 = d6.replace("u'n            ', u'n","").replace("xa0","").strip(" ")
	# 			heightt = d11

	# 		if key =='date_of_birth':
	# 			d7 = str(item[key])
	# 			d19 = d7.replace("[u'","").replace("' u'","").replace("']","").replace("u'","").strip("'")
	# 			date_of_birthh = d19

	# 		if key =='place_of_birth':
	# 			d8 = str(item[key])
	# 			d12 = d8.replace("[u","").replace("']","").strip("'")
	# 			place_of_birthh = d12

	
	# 	try:
	# 			art_obj=Artist.objects.get(name=namee)
	# 			# print"====In side try"
	# 			# prod_obj=Movie.objects.get(name = namee)
	# 	except:
	# 			s, art_obj=Artist.objects.get_or_create(
	# 				name=namee,
	# 				bio=bioo,
	# 				date_of_birth=date_of_birthh, 
	# 				# category=c1, 
	# 				sun_sign=sun_signn,
	# 				height=heightt, 
	# 				feat_photos=feat_photoss,
	# 				# place_of_birth=place_of_birthh,
					
	# 				)
	# 		# 	prod_obj=Artist.objects.get(name=namee)


			
	# return Response({'message':'Products saved succesfully', 'status':200})		

@api_view(['GET','POST'])
def read_file(request):
	import ipdb; ipdb.set_trace()
	f = open('/Users/paramvirgill/desktop/movie.json', 'r')						
	json_string = f.read()																
	f.close()
	try:
		data = json.loads(json_string)
		for item in data:
			print"=====ITEM=====",item
			for key in item:


				if key == 'rating':
					d1 = str(item[key])
					rating = d1

				elif key == 'writers':
					d2 = str(item[key])
					writers = d2	

				elif  key == 'language':
					d3 = item[key]
					lang_list = []
					for i in d3:
						c3 = i.encode('utf-8')
						lang_list.append(c3)

				# elif key == 'category'		

				elif key =='cast':
					d13 = item[key]
					cast_list = []	
					for i in d13:
						c13 = i.encode('utf-8')	
						cast_list.append(c13)

					# print cast_list	

				elif key == 'name':
					d4 = item[key]
					try:
						name = d4[0].encode('ascii','ignore')
					except:
						name = d4	
# 
			

				elif key =='boxofficecollection':
					d5 = item[key]
					# try:
					# 	boxofficecollection = d5[1]
					# except:
					# 	boxofficecollection = d5

					boxofficecollection = d5	

				
					 						
				
				
				elif key =='short_desc':
					d6 = str(item[key])
					short_desc = d6

				
				elif key =='feat_video':
					d7 = str(item[key])
					feat_video = d7

				elif key =='year':
					d8 = str(item[key])
					c8 = d8.encode('utf-8')
					yearr = c8

				elif key == 'storyline':
					d9 = str(item[key])
					storyline = d9

				elif key =='director':
					d10 = str(item[key])
					director = d10

				elif key =='writers':

					d11 = str(item[key])
					writers = d11

					# d11 = item[key]
					# writer_list = []	
					# for i in d11:
					# 	c11 = i.encode('utf-8')	
					# 	writer_list.append(c11)					

				elif key =='duration':
					d12 = item[key]
					# c12 = d12.encode('ascii','ignore')
					duration = d12

				

				elif key =='genre':
					d14 = item[key]
					
					gen_list = []
					for i in d14:
						c14 = i.encode('utf-8')
						gen_list.append(c14)



					# print gen_list
					# print type(d14)

				elif key =='releaseDate':
					d15 = str(item[key])
					try:
						releaseDate = d15[0]
					except:
						releaseDate = d15	

				elif key =='duration':
					d16 = item[key]
					duration = d16
					
				elif key =='feat_photo':
					d17 = item[key]
					feat_photo = []

					
					for i in d17:
						c17 = i.encode('utf-8') 
						feat_photo.append(c17)
					# print feat_photo[1]	

					for i in feat_photo:

						print i

				elif key =='actors':
					d18 = str(item[key])
					year = d18
			# print"======" ,genre		

				elif key == 'certificate':

					d19 = str(item[key])
					certificate = d19		

					if not certificate:
						certificate = ""
		
		    
			try:
				# print"====In side try"
				prod_obj=Movie.objects.get(title = name)


				#abc = cast.objects.get(name = director)
				# allinterest_data =[model_to_dict(c ,exclude='image_url') for c in Category.objects.all().order_by('id')]
				#use getorcreate in the above function whic will give an object which we feed below

			except:
				# print"====print in excpt"
				s, prod_obj = Movie.objects.get_or_create(
						
					title = name ,
					year = yearr ,
					rating = rating,
					short_desc = short_desc,	
					storyline = storyline,
					# category = 		#,
					# director = director,
					# writers = writers,
					duration = duration,
					# cast = cast,		#
					release_date = releaseDate ,
					boxoffice_collection = boxofficecollection,
					feat_photos = feat_photo, #
					feat_video = feat_video, 	#
					certificate = certificate,
					# actors = actors	,
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



	except Exception as e:
		print "=====Excption=========", e





					# prod_obj.save()

				# for i in xlist:
				# 	prod_im=ProductImage(
				# 		image_url=i,
				# 		product_name=prod_obj 
				# 		)
				# 	prod_im.save()

	# return Response({'message':'Products saved succesfully', 'status':200})		

	return Response({'message': 'Prodcuts save successfully', 'status':200})					
					



	


	


		

