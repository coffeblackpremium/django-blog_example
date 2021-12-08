from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, 'partials/index.html')

def linux_basico(request):
    return render(request, 'blog/posts/001-linuxbasico.html')

def post_brucelee(request):
    return render(request, 'blog/posts/002-sejacomoaagua.html')
