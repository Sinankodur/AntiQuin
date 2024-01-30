from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('',views.payment_home, name='payment_home'),
    path('paymenthandler/', views.payment_handler, name='paymenthandler'),
]
