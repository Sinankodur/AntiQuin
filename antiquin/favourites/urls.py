from django.urls import path
from . import views

app_name = 'favourites'

urlpatterns = [
    path('add_to_favourites/<int:product_id>',views.add_to_favourites, name='add_to_favourites'),
    path('',views.view_favourites, name="favourites"),
    path('delete-item/<int:product_id>/',views.delete_item, name='delete_item'),
    path('move-to-cart/<int:product_id>/',views.move_to_cart, name='move_to_cart'),
]
