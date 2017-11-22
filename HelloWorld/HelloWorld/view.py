from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['huyyily'] = 'Hello husnily!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello world!")


def index(request):
    return HttpResponse("Workcome to Django!")