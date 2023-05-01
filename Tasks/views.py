from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DeleteView
from .models import Todo

def add_task(request):
    if request.method == "POST":
        print(request.POST['about_task'])
        print(request.POST['user'])
        
        # if request.POST.get('title') == "":
        #     return render(request, 'field_empty.html')
        title = request.POST['title']
        detail = request.POST['about_task']
        
        Todo.objects.create(title=title, detail=detail)
        
        return HttpResponseRedirect("/")
    else:
        return render(request, 'add_task.html')
        
    
def task_list(request):
    tasks = Todo.objects.all()
    
    return render(
        request,
        'tasks.html',
        {
            'tasks': tasks,
        })

def update_task(request, pk):
    task = Todo.objects.get(pk=pk)
    
    if request.method == "POST":
        task.title = request.POST['title']
        task.detail = request.POST['about_task']
        task.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'update_task.html', {"task": task})
    
def task_detail(request, pk):
    task = Todo.objects.get(pk=pk)
    return render(request, 'task_detail.html', {'task': task})
    
class DeleteTask(DeleteView):
    model = Todo
    template_name = 'task_delete.html'
    success_url = '/'