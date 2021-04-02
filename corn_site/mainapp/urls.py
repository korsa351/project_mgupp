from django.contrib.auth import views
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', mainapp.main, name='bvg'),
]

