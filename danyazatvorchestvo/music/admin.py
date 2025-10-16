from django.contrib import admin
from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'autor', 'time_create', 'quantity_ocenok')  # что показывать в списке
    list_filter = ('autor', 'time_create')  # фильтры справа
    search_fields = ('name', 'autor')  # поиск по названию и автору
    prepopulated_fields = {'name_slug': ('name',)}  # авто-генерация slug из названия