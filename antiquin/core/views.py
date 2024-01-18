from django.shortcuts import render, redirect
from item.models import Category, Product
from cart.models import CartItem
from .forms import SignupForm


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)[0:8]
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request,'core/index.html',{
        'categories' : categories,
        'products' : products,
        'total' : total,
    })

def searchfilter(request, category_id):
    category = Category.objects.filter('')

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