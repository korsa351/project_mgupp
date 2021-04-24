from mainapp.forms import AddUniversityMeetForm
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
    path('registration/', views.RegisterUser.as_view(), name="registration"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('add/', views.add, name="add"),
    path('add/gymnast/', views.GymnastAdd.as_view(), name="add-gymnast"),
    path('gymnast=<int:pk>/update/', views.GymnastUpd.as_view(), name='gymnastupd'),
    path('gymnast=<int:pk>/delete-submit/', views.GymnastDelete.as_view(), name="gymnast_delete_submit"),
    path('add/address/', views.AddressAdd.as_view(), name="add-address"),
    path('add/university/', views.UniversityAdd.as_view(), name="add-university"),
    path('add/meet/', views.MeetAdd.as_view(), name="add-meet"),
    path('add/university-meet/', views.UniversityMeetAdd.as_view(), name="add-university-meet"),
]
