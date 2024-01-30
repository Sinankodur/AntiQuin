from django.shortcuts import render, get_object_or_404
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
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

@csrf_exempt
def payment_handler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                order = get_object_or_404(Order, id=razorpay_order_id)

                try:
                    razorpay_client.payment.capture(payment_id, order.paid_amount * 100)

                    order.paid = True
                    order.save()
                    return render(request, 'paymentsuccess.html')
                except:
                    return render(request, 'paymentfail.html')
            else:
                return render(request, 'paymentfail.html')
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
