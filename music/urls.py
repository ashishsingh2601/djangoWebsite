from django.conf.urls import url
from . import views

app_name = 'music'  #namespacing the url
urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),
    #/music/69/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name="details"),
]
