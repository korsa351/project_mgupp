from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def gymnasts(request):
    return render(request, 'mainapp/gymnasts.html')
