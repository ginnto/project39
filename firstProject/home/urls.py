from django.urls import path

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('studentList',views.list,name='list'),
    path('studentDetails/<int:id>',views.profile,name='details'),


]