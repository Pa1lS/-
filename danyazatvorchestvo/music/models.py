from django.db import models
from django.urls import reverse

# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    photo = models.TextField(blank=True)
    time_create = models.CharField()
    name_slug = models.SlugField(unique=True, db_index=True)
    sum_ocenok = models.IntegerField(default=0) # сумма всех поставленных оценок для песни 
    quantity_ocenok = models.IntegerField(default=0) # кол-во поставленных оценок для песни
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pesnya", kwargs={"pesnya_slug": self.name_slug})
    
    def get_sred_ocenka(self):
        sum_ocenok = self.sum_ocenok
        quantity_ocenok = self.quantity_ocenok
        if quantity_ocenok != 0 and sum_ocenok != 0:
            return sum_ocenok // quantity_ocenok
        elif sum_ocenok == 0 and quantity_ocenok == 0:
            return 0
        