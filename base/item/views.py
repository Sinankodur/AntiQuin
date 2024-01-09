from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


def detail(request,pk):
    product = Products.objects.get(pk=pk)

    return render(request, 'details.html', {'product': product})
