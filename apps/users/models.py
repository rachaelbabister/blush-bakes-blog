from django.contrib.auth.models import User
from django.db import models
from apps.blog.models import Recipe

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    member_since = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(Recipe, related_name='favourited_by', blank=True)

    def __str__(self):
        return self.user.username