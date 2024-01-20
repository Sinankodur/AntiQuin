from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from item.models import Category, Product
from cart.models import CartItem, Cart
from favourites.models import Favourite
from .forms import SignupForm


# def home(request):
#     categories = Category.objects.all()
#     products = Product.objects.filter(is_sold=False)[0:8]
#     user = request.user
    
#     cart = Cart.objects.get(user=user)
#     cart_items = CartItem.objects.filter(cart=cart)
#     product_count = cart_items.count()
#     total = sum(item.product.price * item.quantity for item in cart_items)

#     fav_count = Favourite.objects.filter(user=user).count()

#     return render(request,'core/index.html',{
#       'categories' : categories,
#       'products' : products,
#       'total' : total,
#       'product_count' : product_count,
#       'fav_count' : fav_count,
#     })

from django.http import HttpResponse
def home(request):
    if request.user.is_authenticated:
        user = request.user.id

        categories = Category.objects.all()
        products = Product.objects.filter(is_sold=False)[0:8]
        
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = cart_items.count()
        total = sum(item.product.price * item.quantity for item in cart_items)

        fav_count = Favourite.objects.filter(user=user).count()

        return render(request,'core/index.html',{
        'categories' : categories,
        'products' : products,
        'total' : total,
        'product_count' : product_count,
        'fav_count' : fav_count,
        })
    
    else:

        categories = Category.objects.all()
        products = Product.objects.filter(is_sold=False)[0:8]
        return render(request,'core/index.html',{
            'categories' : categories,
            'products' : products,
        })


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/success/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form' : form})

def success(request):
    return render(request, 'core/success.html')