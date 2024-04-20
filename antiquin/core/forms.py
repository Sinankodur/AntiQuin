from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control mb-3',
        'id': 'username',
        'aria-describedby':"inputGroup-sizing-sm",
        'autofocus' : True
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class' : 'form-control mb-3',
        'id' : 'email',
        'aria-describedby':"inputGroup-sizing-sm"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'form-control mb-3',
        'id' : 'password1',
        'aria-describedby':"inputGroup-sizing-sm"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class' : 'form-control',
        'id' : 'password2',
        'aria-describedby':"inputGroup-sizing-sm"
    }))


class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control mb-4',
        'id': 'username',
        'autofocus' : True
    }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class' : 'form-control mb-3',
        'id' : 'password1'
    }))