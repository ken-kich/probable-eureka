from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView, TemplateView)
from django.urls import reverse_lazy
from .models import Task, Priority
from .forms import TaskCreateForm, TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(ListView):
    template_name = 'taskapp/task_list.html'
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'taskapp/task_create.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskapp/task_detail.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'taskapp/task_update.html'
    fields = ('task_name', 'task_detail', 'due_date', 'is_completed', 'priority')
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdateView, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['priority'].queryset = Priority.objects.all()
        form.fields['priority'].empty_label = None
        return form


class TaskDeleteView(DeleteView):
    model = Task
    templete_name = 'taskapp/task_delete.html'
    success_url = reverse_lazy('list')


class HomeView(TemplateView):
    template_name = 'taskapp/home.html'
