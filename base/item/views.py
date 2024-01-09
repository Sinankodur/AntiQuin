from django.shortcuts import render, get_object_or_404
from .models import Products,Category

# Create your views here.


def detail(request,pk):
    product = Products.objects.get(pk=pk)
    category = Category.objects.all()

    related_items = Products.objects.filter(category=product.category, is_sold = False).exclude(pk=pk)[0:4]

    return render(request, 'details.html', {
        'product': product, 
        'category': category,
        "related_items": related_items
    })
