from django.urls import path
from MyDjangoApp import views

urlpatterns = [
    path("", views.home, name="home"),
]