from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Order


@login_required
def view_orders(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-order_date')

    return render(request, 'orders/orders.html', {'user_orders': user_orders})