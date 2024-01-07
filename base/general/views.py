from django.shortcuts import redirect, render
from .models import Products
from .forms import SignupForm

# Create your views here.



def home(request):
    data = Products.objects.all()
    return render(request,"index.html",{"details" : data})

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form' : form})