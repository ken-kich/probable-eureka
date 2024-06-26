from django.urls import path
from .views import BaseLoginView, SignUpView, LogoutView


urlpatterns = [
    path('login/', BaseLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
