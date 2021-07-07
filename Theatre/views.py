# Create your views here.
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import *
from .models import *
from .utils import *


class Actor(DataMixin, ListView):
    model = Plays
    template_name = 'Theatre/actors.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))

class Actors(DataMixin, ListView):
    model = Actors
    template_name = 'Theatre/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Актеры")
        return dict(list(context.items()) + list(c_def.items()))


def addpage(request):
    if request.method=='POST':
        form=AddActor(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибочка')
    else:
        form = AddActor()
    return render(request, 'Theatre/addpage.html', {'form': form, 'menu': menu, 'title': 'О сайте'})



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2 align="center">Упс, страница не найдена или не существует</h2>')

class Register(DataMixin, CreateView):
    form_class = Registration
    template_name = 'Theatre/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('home')


class Auth(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'Theatre/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return  redirect('login')