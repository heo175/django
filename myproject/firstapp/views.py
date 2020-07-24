from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs
import datetime

# Create your views here.
def main(request):
    blog = Blogs.objects
    return render(request, 'main.html', {'blogs':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blogs()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.lan = request.GET['lan']
    blog.save()
    return redirect('/')

def detail2(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'detail2.html', {'blog':blog})

def update(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'update.html', {'blog':blog})

def ud(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.lan = request.GET['lan']
    blog.date = datetime.datetime.now()
    blog.save()
    return redirect('/detail2/'+str(blog_id))

def delete(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    blog.delete()
    return redirect('/')