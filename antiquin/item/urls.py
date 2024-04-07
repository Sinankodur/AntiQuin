from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('search/', views.searchProduct, name='search'), 
    path('new/', views.add_items,name='new'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
