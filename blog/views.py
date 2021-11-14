from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, 'partials/index.html')

def helloworld(request):
    return render(request, 'blog/posts/helloworld.html')

def post_brucelee(request):
    return render(request, 'blog/posts/02-post-bruce.html')
