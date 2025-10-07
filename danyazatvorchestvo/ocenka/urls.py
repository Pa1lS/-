from django.urls import path
from . import views

urlpatterns = [
    path('pesnya/<slug:pesnya_slug>/', views.show_pesnya, name='pesnya')
]
