from django.contrib import admin

# Register your models here.
from .models import *



class MovieAdmin(admin.ModelAdmin):
	list_display = ("title", "year","get_genre")
	search_fields = ("title",)

	def get_genre(self, obj):
		return "\n".join([p.name for p in obj.genre.all()])

class ArtistAdmin(admin.ModelAdmin):
	list_display = ("name","date_of_birth", "height")
	search_fields = ("name",)

class SoundtrackAdmin(admin.ModelAdmin):
	list_display = ("name", "name_movie")
	search_fields = ("name","name_movie")	



admin.site.register(Artist,ArtistAdmin)
admin.site.register(Movie,MovieAdmin)
# admin.site.register(Award)
admin.site.register(Episode)
admin.site.register(ArtistImage)
admin.site.register(MovieImage)
# admin.site.register(MovieVideo)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(SunSign)
admin.site.register(News)
admin.site.register(Featured)
admin.site.register(Soundtrack, SoundtrackAdmin)