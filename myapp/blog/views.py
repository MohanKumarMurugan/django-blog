from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at the blog index.")

def detail(request):
    return HttpResponse("You are viewing the blog detail.")