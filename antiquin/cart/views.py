from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem, Product
from item.models import Category
from django.contrib.auth.decorators import login_required


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
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    categories= Category.objects.all()
    product = Product.objects.all()

    return render(request, 'cart/view_cart.html', {
        'cart_items': cart_items,
        'total': total,
        'categories' : categories,
        'product' : product
    })
