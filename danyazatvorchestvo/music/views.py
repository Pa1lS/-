from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from music.models import Music


# Create your views here.
def index(request):
    return render(request, 'music/index.html', {'css_file':'music/style.css'})

def musics(request):
    list_p = Music.objects.filter(pk__lte=9)
    data = {'musics_list': list_p,
            'css_file':'music/style.css'}
    return render(request, 'music/musics.html',data )

def show_pesnya(request, pesnya_slug):
    pesnya = get_object_or_404(Music, name_slug=pesnya_slug)
    data = {
        'name': pesnya.name,
        'autor': pesnya.autor,
        }
    return render(request, 'music/song.html', data)