from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.


def AddCategory(request):
    if request.method == 'POST':
        cats = CategoryForm(request.POST)
        if cats.is_valid():
            cats.save()
            redirect('homepage')
    else:
        cats = CategoryForm()
    return render(request, 'task_categories.html', {'form': cats})
