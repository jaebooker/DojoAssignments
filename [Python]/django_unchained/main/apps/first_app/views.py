from django.shortcuts import render, HttpResponse, redirect
import string
import random
from .models import Post, Comment

def survey1(request):
    context = {
    "posts": Post.objects.all()
    }
    return render(request,'first_app/index.html', context)
def survey2(request):
    #using ORM
    Post.objects.create(title=request.POST['title'], message=request.POST['message'])
    #inset into blogs (title, blog, created_at, updated_at) values (title, blog, NOW(), NOW())
    return redirect('/')
def survey3(request, id):
    post = Post.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], post=post)
    return redirect('/')
