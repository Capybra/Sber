from django.db import models
from django.contrib.auth.models import User
import uuid, os

def get_upload_path(instance, filename):
    filename = instance.user.username + '.' + filename.split('.')[1]  
    return os.path.join('profile_images/', filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload_path, default="profile_images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
 
    def __str__(self):
        return str(self.name)
 
    class Meta:
        ordering = ('name',)
