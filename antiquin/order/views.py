from datetime import time
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import razorpay

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


razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def start_order(request):
    if request.method == "POST":
        # Retrieve the payment method from the form
        payment_method = request.POST.get('payment_method')

        # Retrieve or create an order (you might have to adjust this logic)
        order_id = 1  # Replace with your logic to get the order ID
        order = get_object_or_404(Order, id=order_id, user=request.user)

        if payment_method == 'COD':
            # Handle Cash on Delivery (COD) logic here
            # ...

            return render(request, 'cod_success.html')  # You can create a COD success template

        elif payment_method == 'online':
            # Handle online payment logic here

            currency = 'INR'
            amount = order.calculate_total() * 100  # Convert to paise (Razorpay accepts amounts in the smallest currency unit)

            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                            currency=currency,
                                                            payment_capture='0'))

            # Order ID of the newly created Razorpay order
            razorpay_order_id = razorpay_order['id']
            callback_url = 'paymenthandler/'

            # Pass these details to the frontend
            context = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_merchant_key': settings.RAZOR_KEY_ID,
                'razorpay_amount': amount,
                'currency': currency,
                'callback_url': callback_url,
            }

            return render(request, 'payment_home.html', context=context)

        else:
            # Invalid payment method, handle accordingly
            return HttpResponse("Invalid payment method")

    else:
        # Handle GET request for the initial form rendering
        return render(request, 'checkout.html')





def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if not order.is_cancelled:
        order.delete()

    return redirect('/account/') 


