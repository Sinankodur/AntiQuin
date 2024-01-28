from django.shortcuts import render, redirect, get_object_or_404


from cart.models import CartItem,Cart
from order.models import Order, OrderItem
from item.models import Product, Category
from favourites.models import Favourite

def checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)
        
    cart_items = CartItem.objects.filter(cart=cart)
    product_count = cart_items.count()
    total = sum(item.product.price * item.quantity for item in cart_items)
    categories = Category.objects.all()
    product = Product.objects.all()

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    favourites = Favourite.objects.filter(user=user)
    fav_count = favourites.count()

    order = Order.objects.all()

    return render(request, 'order/checkout.html', {
        'cart_items' : cart_items,
        'total': total,
        'categories' : categories,
        'product' : product,
        'product_count' : product_count,
        'fav_count' : fav_count,
        'order' : order
    })


def start_order(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
            address=address, pincode=pincode, place=place, phone=phone
        )

        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            price = product.price * quantity

            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

        cart_items.delete()

        return redirect('/account/') 

    return redirect('/cart/')

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if not order.is_cancelled:
        order.delete()

    return redirect('/account/') 
