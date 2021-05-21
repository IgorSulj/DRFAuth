from django import forms
from django.contrib.auth.models import User

from .models import Product


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

