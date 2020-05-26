from django import forms
from .models import *


class TodoForm(forms.ModelForm):

    class Meta(object):
        model = Todo
        fields = ['title']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'textiput',
                    'placeholder': 'Enter Task here'
                }
            )
        }