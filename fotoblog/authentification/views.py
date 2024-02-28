from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from authentification.models import User
from authentification.forms import UserForm

from . import forms

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')

def change_user_password(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect('logout')
    else:
        form = UserForm(instance=user)

        return render(request,'authentification/password_change.html',{'form':form})
    