from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.home, name="home"),
    path("viewEvents", views.viewEvents, name="viewEvents"),
    path("carnival", views.carnival, name="carnival"),
]