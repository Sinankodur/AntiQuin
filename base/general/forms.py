from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'form-control mb-3',
        'id': 'username',
        'aria-describedby':"inputGroup-sizing-sm"
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email address',
        'class' : 'form-control mb-3',
        'id' : 'email',
        'aria-describedby':"inputGroup-sizing-sm"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class' : 'form-control mb-3',
        'id' : 'password1',
        'aria-describedby':"inputGroup-sizing-sm"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm your password',
        'class' : 'form-control',
        'id' : 'password2',
        'aria-describedby':"inputGroup-sizing-sm"
    }))