from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('blurb', 'recipe_content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)