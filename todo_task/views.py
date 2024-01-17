from django.shortcuts import render
from mytasks.models import TaskModel


def home(request):
    return render(request, 'home.html')


def taskView(request):
    tasks = TaskModel.objects.all()
    return render(request, 'your_template.html', {'tasks': tasks})
