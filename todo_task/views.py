from django.shortcuts import render
from mytasks.models import TaskModel


def home(request):
    tasks = TaskModel.objects.all()
    return render(request, 'home.html', {'tasks': tasks})
