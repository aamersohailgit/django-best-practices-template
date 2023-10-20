from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('user_profile:edit_profile')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_profile:edit_profile')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, 'profile/edit.html', {'user_form': user_form})
