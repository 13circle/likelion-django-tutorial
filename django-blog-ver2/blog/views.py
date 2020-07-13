from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(req):
    blogs = Blog.objects
    return render(req, 'home.html', {'blogs': blogs})

def detail(req, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'detail.html', {'blog': blog_detail})