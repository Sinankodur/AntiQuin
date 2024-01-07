from django.shortcuts import render
from .models import Products
from .forms import SignupForm

# Create your views here.



def home(request):
    data = Products.objects.all()
    return render(request,"index.html",{"details" : data})

def sign_up(request):
    form = SignupForm()
    return render(request, 'sign_up.html', {'form' : form})