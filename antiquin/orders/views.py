from django.shortcuts import render
from cart.models import Cart

# Create your views here.

def start_order(request):
    cart = Cart(request)

    