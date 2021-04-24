from django.contrib.auth import authenticate, login
from django.db.models.query import QuerySet
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddGymnastForm, LoginUserForm, RegisterUserForm, UpdateGymnastForm, AddAddressForm, AddUniversityForm, AddMeetForm, AddUniversityMeetForm
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


def add(request):
    context={}
    other={
        "title":"Add",
        "alert":"Access denied!"
    }
    context["other"]=other
    return render(request, 'mainapp/add.html', context)


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
    paginate_by=6
    
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


class GymnastAdd(CreateView):
    model=Gymnasts
    template_name="mainapp/addgymnast.html"
    success_url=reverse_lazy('add')
    form_class=AddGymnastForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Add a gymnast",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context


class AddressAdd(CreateView):
    model=Addresses
    template_name="mainapp/addaddress.html"
    success_url=reverse_lazy('add')
    form_class=AddAddressForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Add address",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context


class UniversityAdd(CreateView):
    model=University
    template_name="mainapp/adduniversity.html"
    success_url=reverse_lazy('add')
    form_class=AddUniversityForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Add University",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context


class MeetAdd(CreateView):
    model=Meets
    template_name="mainapp/addmeet.html"
    success_url=reverse_lazy('add')
    form_class=AddMeetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Add meet",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context

class UniversityMeetAdd(CreateView):
    model=University_Meet_Participation
    template_name="mainapp/adduniversitymeet.html"
    success_url=reverse_lazy('add')
    form_class=AddUniversityMeetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Add University meet",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context


class GymnastUpd(UpdateView):
    model=Gymnasts
    template_name="mainapp/updgymnast.html"
    form_class=UpdateGymnastForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            "title":"Update a gymnast",
            'alert':"Access denied!",
        }
        context["other"] = other
        return context


class GymnastDelete(DeleteView):
    model=Gymnasts
    template_name="mainapp/delete-submit.html"
    success_url= ('/view/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other = {
            'alert':"Access denied!",
        }
        context["other"] = other
        return context
