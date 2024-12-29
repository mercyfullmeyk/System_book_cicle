
from django.urls import path
from django.contrib.auth import views as reset
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

    path(
        'password_change/',
        reset.PasswordChangeView.as_view(
            template_name='users/password_change_form.html'),
        name='password_change'
    ),

    path(
        'password_change/done/',
        reset.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    ),

    path(
        'password_reset/',
        reset.PasswordResetView.as_view(
            template_name='users/password_reset_form.html'),
        name='password_reset'
    ),

    path(
        'password_reset/done/',
        reset.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        reset.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        reset.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
