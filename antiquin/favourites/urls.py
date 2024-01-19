from django.urls import path
from . import views

app_name = 'favourites'

urlpatterns = [
    path('add_to_favourites/<int:product_id>',views.add_to_favourites, name='add_to_favourites'),
    path('favourites/',views.view_favourites, name="favourites"),
]
