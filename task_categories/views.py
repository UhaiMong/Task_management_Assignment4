from django.shortcuts import render
from .forms import CategoryForm

# Create your views here.


def AddCategory(request):
    cats = CategoryForm()
    return render(request, 'task_categories.html', {'form': cats})
