from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from apps.blog.models import Recipe

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('A Username is required')
        if not full_name:
            raise ValueError('You need to fill in your Full Name')
        if not email:
            raise ValueError('An Email address is required')

        username = self.model(username=username, full_name=full_name, email=email)
        user-set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password=None):
        user = self.create_user(username, full_name, email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    member_since = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(Recipe, related_name='favourited_by', blank=True)

    def __str__(self):
        return self.user.user
