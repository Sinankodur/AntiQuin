from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem, Product
from item.models import Category
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    categories = Category.objects.all()

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, 'cart/add_confirm.html', {
        'categories' : categories,
    })

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})
