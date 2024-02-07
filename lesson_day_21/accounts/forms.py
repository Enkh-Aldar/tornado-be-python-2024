from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    tailwind_class = """w-full border-2 border-ch-gray-light 
        bg-ch-gray-dark rounded-lg 
        focus:outline-ch-green-light focus:outline-0 
        focus:outline-offset-0 focus:border-2 
        focus:border-woys-purple focus:shadow-none 
        focus:ring-0 focus:shadow-0"
        """
        
    username = forms.CharField(widget=forms.TextInput(attrs={"class": tailwind_class}))

        
    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            "username",
            "email",
            "age",
        ]
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm password'
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )