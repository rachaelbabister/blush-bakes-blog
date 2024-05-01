from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from apps.blog.models import Recipe

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    member_since = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(Recipe, related_name='favourited_by', blank=True)

    def __str__(self):
        return self.user.username
