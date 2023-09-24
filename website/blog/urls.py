from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.index, name="main"),
    path("blog/post<int:id>", views.post, name="post"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path('blog/category/<str:name>', views.category, name='category'),
    path('blog/search/', views.search, name="search"),
    path('blog/create/', views.create, name="create"),
    path('blog/post<int:post_id>/add_comment', views.add_comment, name='add_comment')
]