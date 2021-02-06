from django.shortcuts import HttpResponse, render


def hello1(request):
    return HttpResponse("Hello")


def hello2(request):
    return HttpResponse("<html><body><h1>hello2</h1></body></html>")


def hello3(request):
    return render(request, 'templates/hello.html')


def new1(request):
    return render(request, 'templates/new.html')
