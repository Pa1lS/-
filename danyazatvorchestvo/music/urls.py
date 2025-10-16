from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('music/', views.musics, name='musics'),
    path('pesnya/<slug:pesnya_slug>/', views.show_pesnya, name='pesnya'),
    path('submit_song/<slug:pesnya_slug>/', views.ocenka_pesnyi, name='submit_song'),
    path('submit_rating/', views.submit_single_rating, name='submit_rating'),
    
]
