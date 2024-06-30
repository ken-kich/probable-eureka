from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="姓",
        widget=forms.TextInput(
        attrs={'class': 'form-control', },))
    last_name = forms.CharField(
        label="名",
        widget=forms.TextInput(
        attrs={'class': 'form-control', },
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', },
    ))
    birthday = forms.DateField(
        label="誕生日",
        widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd ', 'class': 'form-control',},)
        )
    password1 = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', },
            ))
    password2 = forms.CharField(
        label="パスワード再入力",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', },
            ))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'birthday')
