from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return self.username