from django import forms
from .models import Task, Priority


class TaskCreateForm(forms.ModelForm):
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        empty_label="優先度を選択",
        label="優先度"
    )

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="期限"
    )

    class Meta:
        model = Task
        fields = ['task_name', 'task_detail', 'due_date', 'priority']


class TaskUpdateForm(forms.ModelForm):
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        empty_label="優先度を選択",
        label="優先度")

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label='期限'
    )

    class Meta:
        model = Task
        fields = ['task_name', 'task_detail', 'due_date',
                  'is_completed', 'priority']
