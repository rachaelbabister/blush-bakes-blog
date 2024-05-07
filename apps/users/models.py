from django.contrib.auth.models import User
from django.db import models
from apps.blog.models import Recipe

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    favourite_recipes = models.ManyToManyField(Recipe, related_name='favourited_by', blank=True)

    def __str__(self):
        if self.user is None:
            return 'No User'
        return self.user.username