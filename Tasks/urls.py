from django.urls import path
from . import views
from . views import DeleteTask


urlpatterns = [
    path('', views.task_list, name='home'),
    path('add-task', views.add_task, name='add_task'),
    path('update-task/<int:pk>/', views.update_task, name='update'),
    path('task-detail/<int:pk>/', views.task_detail, name='details'),
    path('del-task/<int:pk>/', DeleteTask.as_view(), name="delete"),
]
