from django.shortcuts import render, redirect
from item.models import Category, Product
from .forms import SignupForm


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)[0:8]

    return render(request,'item/index.html',{
        'categories' : categories,
        'products' : products,
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