from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from authentification.models import User

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name','last_name','role')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)        