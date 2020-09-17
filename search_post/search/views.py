from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.

def search(request):
    blogs = Blog.objects.all()
    return render(request, 'search.html', {'blogs' : blogs})