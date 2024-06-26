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

    def get_queryset(self):
        sort_param = self.request.GET.get('sort')
        queryset = super().get_queryset()

        if sort_param == 'updated_at':
            queryset = queryset.order_by('updated_at')
        elif sort_param == 'due_date':
            queryset = queryset.order_by('due_date')
        elif sort_param == 'priority':
            queryset = queryset.order_by('priority')

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('TaskApp:list')

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
        return reverse_lazy('TaskApp:detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('TaskApp:list')


class HomeView(TemplateView):
    template_name = ('home.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = reverse_lazy('UserApp:login')

        return context
