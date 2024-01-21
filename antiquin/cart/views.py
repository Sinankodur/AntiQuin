from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem, Product
from item.models import Category
from favourites.models import Favourite
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def edit(request):
    if not request.user.is_staff:
        raise PermissionDenied

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/view_cart')

@login_required
def view_cart(request):
    cart_items = None
    favourites = None
    
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = CartItem.objects.filter(cart=cart).count()
        total = sum(item.product.price * item.quantity for item in cart_items)
        categories= Category.objects.all()
        product = Product.objects.all()

        favourites = Favourite.objects.filter(user=user)
        fav_count = favourites.count()

    return render(request, 'cart/view_cart.html', {
        'cart_items': cart_items,
        'total': total,
        'categories' : categories,
        'product' : product,
        'product_count' : product_count,
        'fav_count' : fav_count,
    })