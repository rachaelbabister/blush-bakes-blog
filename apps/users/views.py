from django.shortcuts import render, redirect
from django.contrib import messages
# from django.views import View
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
        

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid(): # Commented out until known if needed (and profile_form.is_valid())
            user_form.save()
            # profile_form.save()
            messages.success(request, 'You have updated your profile successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form}) # commented out until known if needed (profile_form': profile_form)