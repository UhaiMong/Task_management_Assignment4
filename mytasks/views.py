from django.shortcuts import render, redirect
from . forms import AddTaskForm
from .models import TaskModel
# Create your views here.


def AddTask(request):
    if request.method == 'POST':
        tasks = AddTaskForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            redirect('homepage')
    else:
        tasks = AddTaskForm()
    return render(request, 'mytask.html', {'form': tasks})


def EditTask(request, id):
    edit_task = TaskModel.objects.get(pk=id)
    tasks = AddTaskForm(instance=edit_task)
    print(edit_task)
    if request.method == 'POST':
        tasks = AddTaskForm(request.POST, instance=edit_task)
        if tasks.is_valid():
            tasks.save()
            redirect('homepage')
    return render(request, 'mytask.html', {'form': tasks})


def DeleteTask(request, id):
    delete_task = TaskModel.objects.get(pk=id)
    delete_task.delete()
    return redirect('homepage')
