from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('book:index')
    template_name = 'users/signup.html'


class LogoutView(CreateView):
    form_class = CreationForm
    succes_url = reverse_lazy('users/logged_out.html')
    template_name = 'users/logged_out.html'


class LoginView(CreateView):
    form_class = CreationForm
    succes_url = reverse_lazy('book:index')
    template_name = 'users/login.html'
