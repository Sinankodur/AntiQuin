from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect

from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite
from .forms import SignupForm, LoginForm


def home(request):
    cart_items = None
    favourites = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)

    if request.user.is_authenticated:
        user = request.user

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


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', reverse('home'))
                return HttpResponseRedirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {
        'form' : form
    })


def success(request):
    return render(request, 'core/success.html')

def sign_out(request):
    logout(request)
    return redirect('home')
