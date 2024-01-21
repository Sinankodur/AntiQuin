from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

urlpatterns = [
    path('',views.home, name='home'),
    path('sign-up/',views.sign_up, name='sign_up'),
    path('success/',views.success,name='success'),
    path('login/',auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name='login'),
    path('',views.logout_user,name="logout_user"),
]
