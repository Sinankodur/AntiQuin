from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('',views.account,name='account'),
    path('edit/',views.edit_account, name='edit_account'),
    path('users/',views.users_page, name='users_page'),
    path('orders/',views.orders_page, name='orders_page'),
    path('orders-details/<int:pk>/',views.orders_details, name='orders_details'),
    path('order-delivered/<int:order_id>',views.deliver_order, name='deliver_order'),
    path('delivered/',views.delivered, name='delivered'),
    path('purchases/',views.delivered_customer, name='delivered_customer'),
    path('delete-user/<int:user_id>/',views.delete_user, name='delete_user'),
]
