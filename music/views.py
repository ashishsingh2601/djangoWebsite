#from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Album, song
#from django.template import loader



# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {         #information that your template needs
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)

def details(request, album_id):
  #  try:
   #     album = Album.objects.get(id=album_id)
    #except Album.DoesNotExist:
     #   raise Http404("Album Unavailable!")

    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album})

def favorite(request, album_id):
    
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, song.DoesNotExist):
        return render(request, 'music/details.html', { 
            'album':album,
            'error_msg': "You didn't selected a valid song! Please select to continue."
            })

    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})
