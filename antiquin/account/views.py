from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite
from order.models import Order, OrderItem



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

def users_page(request):
    users = User.objects.all()

    return render(request, 'account/users.html', {
        'users' : users
    })

def orders_page(request):
    order_items = OrderItem.objects.all()
    return render(request, 'account/orders.html', {
        'order_items' : order_items
    })

def orders_details(request, pk):
    orders = Order.objects.filter(pk=pk)
    order_items = OrderItem.objects.filter(pk=pk)
    return render(request, 'account/orders_details.html',{
        'orders' : orders,
        'order_items' : order_items
    })

def deliver_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if not order.is_delivered:
        order.mark_as_delivered()
        order.save()
      
        return redirect('/account/delivered')

    return render(request, 'account/orders.html')

def delivered(request):
    orders = Order.objects.filter(is_delivered=True)

    return render(request, 'account/delivered.html', {
            'orders' : orders
        })
    