from django.shortcuts import render, redirect
from item.models import Category, Product
from cart.models import CartItem, Cart
from .forms import SignupForm


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)[0:8]
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    product_count = CartItem.objects.filter(cart=cart).count()
    total = sum(item.product.price * item.quantity for item in cart_items)


    return render(request,'core/index.html',{
        'categories' : categories,
        'products' : products,
        'total' : total,
        'product_count' : product_count
    })


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/success/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form' : form})

def success(request):
    return render(request, 'core/success.html')