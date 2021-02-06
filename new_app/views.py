import datetime

from django.shortcuts import render, HttpResponse
from markupsafe import escape


# Create your views here.
def hello1(request):
    return HttpResponse("Hello")


def hi(request):
    return render(request, 'new_app/hi.html')


def name(request, name):
    sanitize_name = escape(name)
    a_list = [char for char in sanitize_name]
    # random.shuffle(a_list)
    return HttpResponse(f"Witaj, {''.join(a_list).title()}")


def display_name2(request, name):
    return render(
        request=request,
        template_name='new_app/name.html',
        context={'name': name, 'y': 'abc'},
        status=None,
        using=None,
    )


def is_it_newyear(request):
    now = datetime.datetime.now()
    is_new_year = now.day == 31 and now.month == 1
    return render(request, 'new_app/is_it_newyear.html', context={'is_new_year': is_new_year})


def fruits(request):
    """Jinja Loops"""

    fruits = ['jabłko', 'banan', 'winogrona', 'mandarynki']
    return render(
        request,
        'new_app/fruits.html',
        {'fruits': fruits}
    )
