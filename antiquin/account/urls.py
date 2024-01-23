from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('address',views.address, name='address'),
]
