from django.shortcuts import render
from django.http import HttpResponse
from .models import Email, User
# Create your views here.

def index(response):
    return HttpResponse(" <h1>Hello, World!</h1>")



def about(response):
    return HttpResponse("<h1>This is the about page</h1")

def users(response, id):
    Is = User.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % Is.name)
