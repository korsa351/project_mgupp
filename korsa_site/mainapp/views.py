from django.contrib.auth import authenticate, login
from django.db.models.query import QuerySet
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.models import User


def index(request):
    context={}
    other = {
        "title":"University Gymnastics",
    }
    context["other"]=other
    return render(request, 'mainapp/index.html', context)

def test(request):
    context={}
    other = {
        "title":"Test",
        "alert":"Access denied!"
    }
    context["other"]=other
    return render(request, 'mainapp/test.html', context)


class GymnastsTable(ListView):
    model=Gymnasts
    context_object_name='gymnasts_list'
    template_name='mainapp/gymnasts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"List of Gymnasts",
            "alert":"Oh, No!\n Sign in to view this page",
        }
        context["other"] = other
        return context


class GymnastsView(ListView):
    model=Gymnasts
    context_object_name='gymnasts_list'
    template_name='mainapp/view.html'
    paginate_by=5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Viewing Gymnasts",
            "alert":"Oh, No!\n Sign in to view this page",
        }
        context["other"] = other
        return context


class GymnastDetailView(DetailView):
    model=Gymnasts
    context_object_name='gymnast'
    template_name='mainapp/gymnast-detail.html'
    pk_url_kwarg="post_pk"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Gymnast",
            "alert":"Oh, No!\n Log in to view this page",
        }
        context["other"] = other
        return context
    

class RegisterUser(CreateView):
    model=User
    form_class=RegisterUserForm
    template_name="mainapp/register.html"
    success_url=reverse_lazy('index')
    success_msg="Successful registration!"
    form=RegisterUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Registration",
            'alert':"You are already sign in",
        }
        context["other"] = other
        return context

    def form_valid(self, form):
        form_valid=super().form_valid(form)
        username=form.cleaned_data["username"]
        password=form.cleaned_data["password1"]
        auth_user=authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class LoginUser(LoginView):
    template_name="mainapp/login.html"
    form_class=LoginUserForm
    success_url=reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Authorization",
            'alert':"You are already sign in",
        }
        context["other"] = other
        return context

    def get_success_url(self) -> str:
        return self.success_url


class Logout(LogoutView):
    next_page=reverse_lazy('index')
