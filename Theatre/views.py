# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu=["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Actors.objects.all()
    context= {
        'posts': posts,
        'menu': menu,
        'title': 'Актеры нашего театра'
    }
    return render(request, 'Theatre/index.html', context=context)

def about(request):
    return render(request, 'Theatre/about.html', {'menu': menu, 'title': 'О сайте'})

def main(request):
    return render(request, 'Theatre/main.html', {'menu': menu, 'title': 'Тестовая'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2 align="center">Упс, страница не найдена или не существует</h2>')