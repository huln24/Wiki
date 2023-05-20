from turtle import title
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("results", views.result, name="result"),
    path("newpage", views.newpage, name="newpage"),
    path("random", views.randompage, name="randompage"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
]
