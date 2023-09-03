import random

from django.shortcuts import render


# Create your views here.
def dummy():
    return str(random.randint(1, 10))


def index(request):
    return render(request, "blog/index.html")


def post(request):
    return render(request, "blog/post.html")


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def services(request):
    return render(request, "blog/services.html")
