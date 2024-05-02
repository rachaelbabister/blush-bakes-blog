from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile.first_name = self.cleaned_data['full_name']
        if commit:
            user_profile.save()
        return user


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=50, required=True)
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        user_profile = user.profile
        user_profile.first_name = self.cleaned_data['full_name']
        if commit:
            user_profile.save()
        return user


# class UpdateProfileForm(forms.ModelForm):
#     favourites = forms.TextField()

#     class Meta:
#         model = UserProfile
#         fields = ['favourites']