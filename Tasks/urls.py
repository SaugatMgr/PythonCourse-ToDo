from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='home'),
    path('add-task', views.add_task, name='add_task'),
]
