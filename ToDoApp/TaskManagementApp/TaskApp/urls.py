from django.urls import path
from .views import (
    TaskListView, TaskDetailView,
    TaskCreateView, TaskDeleteView, TaskUpdateView, HomeView)

app_name = "TaskApp"

urlpatterns = [
    path('list/', TaskListView.as_view(), name='list'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('home/', HomeView.as_view(), name='home'),
]
