from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddTask, name='add_task'),
    path('edit/<int:id>', views.EditTask, name='edit_post'),
    path('delete/<int:id>', views.DeleteTask, name='delete_post')
]
