from django.shortcuts import render, get_object_or_404
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from order.models import Order

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def payment_home(request, order_id):
    # Retrieve the order or return a 404 if not found
    order = get_object_or_404(Order, id=order_id, user=request.user)

    currency = 'INR'
    amount = order.calculate_total() * 100  # Convert to paise (Razorpay accepts amounts in smallest currency unit)

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

@csrf_exempt
def payment_handler(request):
    if request.method == "POST":
        try:
            # Get the required parameters from the POST request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # Verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                # Retrieve the order based on the Razorpay order ID
                order = get_object_or_404(Order, id=razorpay_order_id)

                try:
                    # Capture the payment
                    razorpay_client.payment.capture(payment_id, order.paid_amount * 100)

                    # Update the order status and render success page on successful capture of payment
                    order.paid = True
                    order.save()
                    return render(request, 'paymentsuccess.html')
                except:
                    # If there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
                # If signature verification fails.
                return render(request, 'paymentfail.html')
        except:
            # If we don't find the required parameters in POST data.
            return HttpResponseBadRequest()
    else:
        # If other than POST request is made.
        return HttpResponseBadRequest()
