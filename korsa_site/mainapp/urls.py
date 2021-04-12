from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gymnasts/', views.GymnastsTable.as_view(), name='gymnasts'),
    path('view/', views.GymnastsView.as_view(), name='view_gymnasts'),
    path('test/', views.test, name="test"),
    path('gymnast=<int:post_pk>/', views.GymnastDetailView.as_view(), name="gymnast_detail"),
    path('register/', views.RegisterUser.as_view(), name="register")
]
