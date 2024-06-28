from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView, TemplateView)
from django.urls import reverse_lazy
from .models import Task, Priority
from .forms import TaskCreateForm, TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(ListView):
    template_name = 'task_list.html'
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'task_update.html'

    def get_success_url(self):
        return reverse_lazy("task_detail")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'taskapp/task_delete.html'
    success_url = reverse_lazy('task_list')


class HomeView(TemplateView):
    template_name = ('home.html')
