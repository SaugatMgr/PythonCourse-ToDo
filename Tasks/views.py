from django.shortcuts import render, HttpResponseRedirect
from .models import Todo


def task_list(request):
    tasks = Todo.objects.all()
    
    return render(request, 'tasks.html', {'tasks': tasks})

def add_task(request):
    
    if request.method == "GET":
        return render(request, 'add_task.html')
    else:
        print(request.POST)
        title = request.POST['title']
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")