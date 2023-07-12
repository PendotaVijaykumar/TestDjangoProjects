from django.contrib import admin
from testapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['ReleaseDate','MovieName','Hero','Heroine','Rating',]

admin.site.register(Movie,MovieAdmin)
