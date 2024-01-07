from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control',
        'id': 'username'
    }))
    
    email = forms.CharField(widget=forms.EmailField(attrs={
        'placeholder': 'Your email address',
        'class' : 'form-control',
        'id' : 'email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class' : 'form-control',
        'id' : 'email'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class' : 'form-control',
        'id' : 'email'
    }))