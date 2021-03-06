from django.db import models

# Create your models here.
# It's a blueprint of database, 
# template which tells how we're going to store data for this app


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.artist + '-' + self.album_title

class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_fav = models.BooleanField(default = False)
   
    def __str__(self):
        return self.song_title

