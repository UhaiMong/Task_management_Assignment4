from django.urls import path
from . import views
urlpatterns = [
    path('category/', views.AddCategory, name='add_category')
]
