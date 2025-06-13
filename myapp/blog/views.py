from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at the blog index.")

def detail(request, post_id):
    return HttpResponse(f"You are viewing the post detail page. And ID is {post_id}")

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is the new URL")