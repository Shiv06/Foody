from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile

class Registration(UserCreationForm):

    class Meta:
        model=get_user_model()
        fields=('username','email','password1','password2')

class UserForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('__all__')
