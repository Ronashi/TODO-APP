from django.forms import ModelForm
from .models import Todo

class Todo_form():
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']