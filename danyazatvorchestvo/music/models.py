from django.db import models
from django.urls import reverse

# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    photo = models.TextField(blank=True)
    time_create = models.CharField()
    name_slug = models.SlugField(unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pesnya", kwargs={"pesnya_slug": self.name_slug})
