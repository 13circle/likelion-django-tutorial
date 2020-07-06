from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(req):
    blogs = Blog.objects
    return render(req, 'home.html', {'blogs': blogs})