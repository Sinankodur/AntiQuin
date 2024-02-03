from django.shortcuts import render, get_object_or_404
from django.conf import settings
import razorpay
from order.models import Order

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def payment_home(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    currency = 'INR'
    amount = order.calculate_total() * 100 

    razorpay_order = razorpay_client.order.create(dict(
        amount=amount,
        currency=currency,
        payment_capture='0'
    ))

    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url,
    }

    return render(request, 'payment_home.html', context=context)
