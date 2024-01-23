from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>',views.add_to_cart, name='add_to_cart'),
    path('',views.view_cart, name="view_cart"),
    path('delete-item/<int:item_id>/',views.delete_item, name='delete_item'),
    path('update-cart/<int:product_id>/',views.update_cart, name='update_cart')
]
