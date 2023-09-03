from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("post/", views.post),
    path("about/", views.about),
    path("contact/", views.contact),
    path("services/", views.services),
]