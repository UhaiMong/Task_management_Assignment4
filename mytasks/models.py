from django.db import models
from task_categories.models import CategoryModel

# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.taskTitle
