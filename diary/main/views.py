from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Тест</h4>")

def about(request):
    return HttpResponse("<h4>Тест2</h4>")

# Create your views here.
