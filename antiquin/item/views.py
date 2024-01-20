from django.shortcuts import render
from item.models import Category,Product
from cart.models import CartItem, Cart
from favourites.models import Favourite
from django.contrib.auth.decorators import login_required
from .forms import NewProductForm

def detail(request,pk):
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    related_items = Product.objects.filter(category=product.category, is_sold = False).exclude(pk=pk)[0:4]
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    product_count = CartItem.objects.filter(cart=cart).count()
    total = sum(item.product.price * item.quantity for item in cart_items)

    fav_count = Favourite.objects.filter(user=user).count()

    return render(request, 'item/details.html', {
        'product': product, 
        'categories': categories,
        "related_items": related_items,
        'total' : total,
        'product_count' : product_count,
        'fav_count' : fav_count
    })

def searchProduct(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains=searched)
        categories = Category.objects.all()

        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = cart_items.count()
        total = sum(item.product.price * item.quantity for item in cart_items)

        fav_count = Favourite.objects.filter(user=user).count()

    return render(request, 'item/searchProducts.html' ,{
        'searched': searched,
        'products': products,
        'categories': categories,
        'total' : total,
        'product_count' : product_count,
        'fav_count' : fav_count
    })


@login_required
def add_items(request):
    form = NewProductForm()

    return render(request, 'item/form.html', { 
        'form' : form,
        'title' : 'Add Items',
        
    })