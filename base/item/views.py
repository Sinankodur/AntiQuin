from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


def detail(request,pk):
    product = get_object_or_404(Products, pk=pk)
    

    return render(request, 'details.html', {'product': product})
