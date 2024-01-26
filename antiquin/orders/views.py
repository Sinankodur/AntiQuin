from django.shortcuts import render
from cart.models import Cart

def start_order(request):
    cart = Cart(request)

    