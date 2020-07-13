from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(req):
    blogs = Blog.objects
    return render(req, 'home.html', {'blogs': blogs})

def new_blog(req):
    #
    return render(req, 'new.html')

def create(req):
    blog = Blog()
    blog.title = req.GET['title']
    blog.body = req.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def detail(req, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'detail.html', {'blog': blog_detail})