from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def index (request) :

    return HttpResponse("request")

def about(request) :
    return HttpResponse("about")

def contact(request) :
    return HttpResponse("contact")
