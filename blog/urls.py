
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblog, name='bloghome'),
    path('<int:blog_id>', views.details, name='details'),
]
