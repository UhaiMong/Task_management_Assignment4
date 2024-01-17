from django.shortcuts import render

# Create your views here.


def AddCategory(request):
    return render(request, 'task_categories.html')
