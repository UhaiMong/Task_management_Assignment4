from django.shortcuts import render
from . forms import AddTaskForm
# Create your views here.


def AddTask(request):
    tasks = AddTaskForm()
    return render(request, 'mytask.html', {'form': tasks})
