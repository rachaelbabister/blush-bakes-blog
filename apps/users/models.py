from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    profile_picture = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True)
    member_since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
