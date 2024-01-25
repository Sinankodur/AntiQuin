from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite


@login_required
def account(request):
    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()

    user_cart, created = Cart.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(cart=user_cart)
    product_count = cart_items.count()
    total = sum(item.product.price * item.quantity for item in cart_items)

    favourites = Favourite.objects.filter(user=user)
    fav_count = favourites.count()

    return render(request, 'account/profile.html', {
        'categories': categories,
        'products': products,
        'total': total,
        'product_count': product_count,
        'fav_count': fav_count,
    })

def add_address(request):
    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()

    user_cart, created = Cart.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(cart=user_cart)
    product_count = cart_items.count()
    total = sum(item.product.price * item.quantity for item in cart_items)

    favourites = Favourite.objects.filter(user=user)
    fav_count = favourites.count()

    return render(request, 'account/delivery_contact.html', {
        'categories': categories,
        'products': products,
        'total': total,
        'product_count': product_count,
        'fav_count': fav_count,
    })
