from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('start-order/',views.start_order, name='start_order')
]