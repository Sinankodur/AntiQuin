
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite
from order.models import Order


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

    orders = Order.objects.filter(user=user)
    
    return render(request, 'account/profile.html', {
        'categories': categories,
        'products': products,
        'total': total,
        'product_count': product_count,
        'fav_count': fav_count,
        'orders' : orders,
    })

def edit_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('/account/')
    return render(request, 'account/edit_account.html')
