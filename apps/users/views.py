from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from .forms import ProfileForm
from .models import UserProfile


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'users/profile.html', {'form': form})