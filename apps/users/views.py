from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from .forms import ProfileForm, SignUpForm
from . import models


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = models.UserProfile.objects.create(user=user, full_name=form.cleaned_data['full_name'], email=form.cleaned_data['email'], member_since=timezone.now())
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user_profile, created = models.UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'users/profile.html', {'form': form})


