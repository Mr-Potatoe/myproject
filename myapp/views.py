# Create your views here.
from django.shortcuts import render
# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")
