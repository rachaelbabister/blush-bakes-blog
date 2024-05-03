from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

User = get_user_model()

# Create your models here.

class Recipe(models.Model):
    """
    Stores a single blog post entry related to a user.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=205, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    difficulty_rating = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    favourite_recipes = models.ManyToManyField(User, related_name='favourite_recipes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}. Added by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to a recipe and user.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.content} by {self.author}"