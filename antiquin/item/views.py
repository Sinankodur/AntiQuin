from django.shortcuts import render
from item.models import Category,Product
from django.http import JsonResponse


def detail(request,pk):
    product = Product.objects.get(pk=pk)
    category = Category.objects.all()

    related_items = Product.objects.filter(category=product.category, is_sold = False).exclude(pk=pk)[0:4]

    return render(request, 'item/details.html', {
        'product': product, 
        'category': category,
        "related_items": related_items
    })

def searchProduct(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        category = Category.objects.all()

    return render(request, 'item/searchProducts.html' ,{
        'searched': searched,
        'products': products,
        'category': category,
    })