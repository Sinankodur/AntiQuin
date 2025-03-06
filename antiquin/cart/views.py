from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Cart, CartItem, Product
from item.models import Category
from favourites.models import Favourite


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
        )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')

@login_required
def update_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    cart = Cart.objects.get(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove' and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()

    return redirect('/cart/')


@login_required
def view_cart(request):
    cart_items = None
    favourites = None
    
    if request.user.is_authenticated:
        user = request.user

        cart, created = Cart.objects.get_or_create(user=user)
        
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = CartItem.objects.filter(cart=cart).count()
        total = sum(item.product.price * item.quantity for item in cart_items)
        categories = Category.objects.all()
        product = Product.objects.all()

        for item in cart_items:
            item.subtotal = item.product.price * item.quantity

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

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('/cart/')

@login_required
def move_to_favourites(request, product_id):
    product_id = int(product_id)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)

    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()

    if not Favourite.objects.filter(user=user, product_id=product_id).exists():
        favourite = Favourite(user=user, product_id=product_id)
        favourite.save()

    return redirect('/favourites')
