from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

from music.models import Music



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
        'name_p': pesnya.name,
        'autor': pesnya.autor,
        'p_id':pesnya.pk
        }
    return render(request, 'music/song.html', data)


def update_ocenka(p_id, value):
    Music.objects.filter(id=p_id).update(
        sum_ocenok=F('sum_ocenok') + value,
        quantity_ocenok=F('quantity_ocenok') + 1,
    )
    
    
@csrf_exempt
def submit_single_rating(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            category = data.get("category", "")
            value = int(data.get("value", ""))
            p_id = int(data.get("pesnya_id"))
            
            print("=== ПОЛУЧЕНЫ ДАННЫЕ НА СЕРВЕРЕ ===")
            print(f"Категория: {category}")
            print(f"Значение: {value}")
            print("===================================")
            update_ocenka(p_id, value)
            if category and value:
                # Здесь можно сохранить в БД
                # Rating.objects.create(category=category, value=value)
                """Нужно дописать сюда редирект на главную"""
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"error": "Missing data"}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
    return JsonResponse({"error": "Invalid method"}, status=405)