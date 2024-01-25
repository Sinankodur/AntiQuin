from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('',views.account,name='account'),
    path('add-address/',views.add_address, name='add_address'),

]
