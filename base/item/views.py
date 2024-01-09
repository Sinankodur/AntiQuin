from django.shortcuts import render, get_object_or_404
from .models import Products,Category

# Create your views here.


def detail(request,pk):
    product = Products.objects.get(pk=pk)
    category = Category.objects.all()

    return render(request, 'details.html', {'product': product, 'category': category})
