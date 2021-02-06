from django.shortcuts import render


# Create your views here.
def register(request):
    print(request)
    return render(
        request,
        'form_app2/register.html',
    )


def task_list(request):
    with open('tasks.txt', mode='a+', encoding='utf-8') as f:
        if request.POST.get('task'):
            f.write('\n' + request.POST.get('task'))
        f.seek(0)
        tasks = f.readlines()

    return render(
        request,
        'form_app2/task-list.html',
        context={
            'tasks': tasks,
        }
    )
