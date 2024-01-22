from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    
    path('',views.view_orders,name='view_orders'),
]
