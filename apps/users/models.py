from django.contrib.auth.models import User
from django.db import models
from apps.blog.models import Recipe

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=200)
    member_since = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(Recipe, related_name='favourited_by', blank=True)

    USERNAME_FIELD = 'user'

    def __str__(self):
        if self.user:
            return self.user.username
        return "No User"