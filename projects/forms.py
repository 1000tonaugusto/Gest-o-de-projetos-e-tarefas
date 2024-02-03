from django.forms import ModelForm
from django.forms import DateInput

from .models import Task, Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'due_date': DateInput(format=('%d-%m-%Y'),
                   attrs={'type': 'date'}),
                   }