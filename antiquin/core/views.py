from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite
from .forms import SignupForm


def home(request):
    cart_items = None
    favourites = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)[:8]

    if request.user.is_authenticated:
        user = request.user
        categories = Category.objects.all()
        products = Product.objects.filter(is_sold=False)[:8]

        user_cart, created = Cart.objects.get_or_create(user=user)

        cart_items = CartItem.objects.filter(cart=user_cart)
        product_count = cart_items.count()
        total = sum(item.product.price * item.quantity for item in cart_items)

        favourites = Favourite.objects.filter(user=user)
        fav_count = favourites.count()

        return render(request, 'core/index.html', {
            'categories': categories,
            'products': products,
            'total': total,
            'product_count': product_count,
            'fav_count': fav_count,
        })

    return render(request, 'core/index.html',{
        'categories' : categories,
        'products' : products
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

def logout_user(request):
    logout(request)
    return redirect('home')
