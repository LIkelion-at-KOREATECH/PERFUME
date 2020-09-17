from django.shortcuts import render
from .models import Post

# Create your views here.

def search(request):
    posts = Post.objects.all()
    return render(request, 'search.html', {'posts':posts})

def detail(request):
    return render(request, 'detail.html')