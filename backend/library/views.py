from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):    # HttpRequest
    return HttpResponse("<h1>ГЛАВНАЯ СТРАНИЦА</h1>")


def index_library(request):  # HttpRequest
    return HttpResponse("<h1>главная страница приложения 'library'</h1>")


def categories(request):  # HttpRequest
    return HttpResponse("<h1>Книги по категориям</h1>")
