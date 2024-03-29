from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favourite
from item.models import Category
from cart.models import Cart, CartItem

@login_required
def add_to_favourites(request, product_id):
    product_id = int(product_id)
    user = request.user
    
    if not Favourite.objects.filter(user=user, product_id=product_id).exists():
        favourites = Favourite(user=user, product_id=product_id)
        favourites.save()

    return redirect('/favourites')

@login_required
def view_favourites(request):
    cart_items = None
    favourites = None
    
    if request.user.is_authenticated:
        user = request.user
        favourites = Favourite.objects.filter(user=user)
        fav_count = favourites.count()

        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = CartItem.objects.filter(cart=cart).count()
        total = sum(item.product.price * item.quantity for item in cart_items)
        categories = Category.objects.all()

    return render(request, 'favourites/favourites.html', {
        'favourites' : favourites,
        'fav_count' : fav_count,
        'product_count' : product_count,
        'total' : total,
        'categories' : categories
    })

@login_required
def delete_item(request, product_id):
    product = get_object_or_404(Favourite, id=product_id, user=request.user)
    product.delete()
    return redirect('/favourites')

@login_required
def move_to_cart(request, product_id):
    favourite = get_object_or_404(Favourite, product_id=product_id, user=request.user)

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=favourite.product)

    favourite.delete()

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')