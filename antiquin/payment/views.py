from django.shortcuts import render

def payment_home(request):
    return render(request, 'payment_home.html')
