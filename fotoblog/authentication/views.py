from django.conf import settings
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from authentication.models import User

from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def upload_profile_picture(request):
    user = User.objects.get(id=request.user.id) 
     
    form = forms.UploadProfilePhotoForm(instance=user) 

    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.UploadProfilePhotoForm(request.FILES, instance=user)

    return render(request, 'authentication/upload_profile_picture.html', context={'form': form})
