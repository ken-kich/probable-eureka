from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    success_url = reverse_lazy('list')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'userapp/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        return valid
