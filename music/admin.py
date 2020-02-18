from django.contrib import admin

# Register your models here.

from . models import Album, song

admin.site.register(Album)
admin.site.register(song)