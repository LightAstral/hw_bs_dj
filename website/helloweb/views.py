from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # lybaya logika

    return HttpResponse("""
        <h1> Hello from Django! </h1>
        <h2> Response </h2>
    """)


def contacts(request):
    return HttpResponse("""
        <h1> Contacts </h2>
        <p> Number: 12345678 </p>
    """)
