from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.simple_register, name='register'),
    path('login/', views.simple_login, name='login'),
    path('logout/', views.simple_logout, name='logout'),
]