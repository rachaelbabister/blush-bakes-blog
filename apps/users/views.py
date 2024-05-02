from django.shortcuts import render, redirect
from django.contrib import messages
# from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm, UpdateUserForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


def profile_view(request, username):
    user = User.objects.get(username=username)
    user_profile = user.profile
    return render(request, 'profile.html', {'user': user, 'user_profile': user_profile})       


@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.full_name = form.cleaned_data['full_name']
            user.profile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users-profile')
    else:
        form = UpdateUserForm()
    return render(request, 'users/profile.html', {'form': form})