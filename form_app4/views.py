from django.shortcuts import render
from .models import Tasks
from django.shortcuts import Http404, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

# Create your views here.
def register(request):
    print(request)
    return render(
        request,
        'form_app4/register.html',
    )


def task_list(request):
    task_title = request.POST.get('task')
    if request.method == 'POST':
        if task_title and not Tasks.objects.filter(task_title=task_title):
            Tasks.objects.create(task_title=task_title)
        return redirect('form_app4:task_list')

    tasks = list(
        Tasks.objects.all()
        .order_by('created_at')
    )

    return render(
        request,
        'form_app4/task-list.html',
        context={
            'tasks': tasks,
        }
    )


def update(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Tasks, id=task_id)
        print('task.task_title: ',task.task_title)
        return render(
            request,
            'form_app4/update.html',
            context={
                'task': task,
            }
        )
    
    if request.method == "POST":
        modified_task = request.POST.get('task')
        if modified_task:
            task = Tasks.objects.filter(pk=task_id).first()
            task.task_title = modified_task
            task.save()
        
        return redirect('form_app4:task_list')
    raise Http404


@require_http_methods(['POST'])
def delete(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('form_app4:task_list')
    