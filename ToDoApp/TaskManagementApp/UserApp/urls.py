from django.urls import path, reverse_lazy
from .views import UserLoginView, SignUpView
from django.contrib.auth.views import LogoutView

app_name = 'UserApp'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('TaskApp:home')), name='logout'),
]
