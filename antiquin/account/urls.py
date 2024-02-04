from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('',views.account,name='account'),
    path('edit/',views.edit_account, name='edit'),
    path('users/',views.users_page, name='users_page'),
    path('orders/',views.orders_page, name='orders_page'),

]
