from django.shortcuts import render
from .models import Products

# Create your views here.



def home(request):
    data = Products.objects.all()
    return render(request,"index.html",{"details" : data})