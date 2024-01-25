from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/',views.detail, name='detail'),
    path('search/',views.searchProduct, name='search'), 
    path('new/',views.add_items,name='new'),
    path('delete/<int:pk>',views.delete, name='delete'),
    path('edit/<int:pk>',views.edit, name='edit'),
]
