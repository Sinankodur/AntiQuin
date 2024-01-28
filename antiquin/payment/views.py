import razorpay
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from cart.models import CartItem
from order.models import Order, OrderItem


def pay_now(request):
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

        client = razorpay.Client(auth=("rzp_test_irphkDgn8Na7V5", "20FQicfgG7rcFmlv4hIxvly8"))
        order_amount = int(order.get_total_amount() * 100)
        order_currency = 'INR'
        order_receipt = f'order_{order.id}'

        razorpay_order = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt))

        messages.info(request, 'You will be redirected to payment page')
        return render(request, 'payment/payment_page.html', {'razorpay_order': razorpay_order})
    
    messages.info(request, 'Your password has been changed successfully!')
    return HttpResponseRedirect('/account/')