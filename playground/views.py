from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a view function takes a request and returns a response
# a view is a request handler

def calculate():
    x = 1
    y = 2
    return x
    

def say_hello(request):
    x = calculate()
    return render(request, "hello.html", {"name": "Cameron"})