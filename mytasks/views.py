from django.shortcuts import render

# Create your views here.


def AddTask(request):
    return render(request, 'mytask.html')
