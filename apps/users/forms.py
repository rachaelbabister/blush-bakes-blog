from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = UserProfile
        fields = ['username', 'full_name', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email']