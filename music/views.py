from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from . models import Album
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
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Unavailable!")
    return render(request, 'music/details.html', {'album': album})
