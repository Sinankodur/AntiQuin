from django.shortcuts import redirect, render, get_object_or_404
from .models import Products, Category
from .forms import SignupForm

# Create your views here.


def home(request):
    products = Products.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()

    return render(request,"index.html",{'products': products,'category': categories})


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login/')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form' : form})


def detail(request,pk):
    product = get_object_or_404(Products, pk=pk)
    

    return render(request, 'details.html', {'product': product})