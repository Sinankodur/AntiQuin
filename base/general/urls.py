from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('',views.home),
    path('<int:pk>/', views.detail, name='details'),
    path('sign-up/',views.sign_up, name='sign_up'),
]
