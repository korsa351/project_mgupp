from django.db.models.query import QuerySet
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView


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
            "guest":"Oh, No!\n Log in to view this page",
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
            "guest":"Oh, No!\n Log in to view this page",
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
            "guest":"Oh, No!\n Log in to view this page",
        }
        context["other"] = other
        return context
    

class RegisterUser(CreateView):
    form_class=UserCreationForm
    template_name="mainapp/register.html"
    success_url=reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Registration",
        }
        context["other"] = other
        return context
