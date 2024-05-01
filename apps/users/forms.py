from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password', 'password_confirm']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email']


