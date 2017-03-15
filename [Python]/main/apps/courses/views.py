# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import Course
def index(request):
    context = {
    'cour': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def index2(request):
    # using ORM
    Course.objects.create(title=request.POST['title'], description=request.POST['description'])
    # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return redirect('/')
