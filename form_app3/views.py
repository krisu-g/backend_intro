from django.shortcuts import render
from .models import Tasks


# Create your views here.
def register(request):
    print(request)
    return render(
        request,
        'form_app3/register.html',
    )


def task_list(request):
    task_title = request.POST.get('task')
    if task_title and not Tasks.objects.filter(task_title=task_title):
        Tasks.objects.create(task_title=task_title)
    tasks = list(Tasks.objects.all().order_by('id').values_list('task_title', flat=True))

    return render(
        request,
        'form_app3/task-list.html',
        context={
            'tasks': tasks,
        }
    )
