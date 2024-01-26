from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('checkout/',views.checkout, name='checkout'),
    path('start-order/',views.start_order, name='start_order'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
