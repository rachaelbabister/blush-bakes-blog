from django import forms
from django.contrib.auth.models import User
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            UserProfile.objects.create(user=user, full_name=form.cleaned_data['full_name'], email=form.cleaned_data['email'])
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email']