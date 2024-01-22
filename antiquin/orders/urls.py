from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('order_now/<int:product_id>/',views.order_now,name='order_now'),
    path('',views.view_orders,name='view_orders'),
]
