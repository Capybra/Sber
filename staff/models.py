from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150)
    id = models.AutoField(primary_key=True)
    

class Staff(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    staff_id = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        # Хэширование пароля перед сохранением
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email