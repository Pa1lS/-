from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('music/', views.musics, name='musics'),
    path('pesnya/<slug:pesnya_slug>/', views.show_pesnya, name='pesnya'),
]
