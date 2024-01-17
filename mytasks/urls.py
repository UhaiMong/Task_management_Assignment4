from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddTask, name='add_task')
]
