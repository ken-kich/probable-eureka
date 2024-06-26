from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class UserLoginView(BaseLoginView):
    template_name = 'UserApp/templates/userapp/login.html'
    success_url = reverse_lazy('taskapp:list')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'UserApp/templates/userapp/signup.html'
    success_url = reverse_lazy('userapp:login')


class LogoutView(BaseLogoutView):
    pass
