from django.urls import path
from . import views as sigma
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        sigma.SignUp.as_view(),
        name='signup'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
            next_page='book:index'
        ),
        name='login'
    ),
]
