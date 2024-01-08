from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.detail, name='details'),
]
