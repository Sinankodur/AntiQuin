from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path('<int:id>'),
    path('sign-up/',views.sign_up, name='sign_up'),
]
