# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import Email
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def index(request):
    return render(request, 'first_app/index.html')
def index2(request):
    # using ORM
    count = 4
    if count < 1:
        return HttpResponse("That's it! THAT'S IT! I'm done with you! \
        I'm not going to waste my time as you clown around. No email for you!")
    elif len(request.POST['email']) < 1:
        return HttpResponse("What the hell was that? That was nothing...\
         YOU are nothing.")
        count -= 1
    elif not EMAIL_REGEX.match(request.POST['email']):
        return HttpResponse("I said an EMAIL! What the fuck is wrong with you? \
        Do you think this is a joke? You, sir, are a joke.")
        count -= 1
    else:
        Email.objects.create(email=request.POST['email'])
    context = {
    "uemails": Email.objects.all()
    # select * from Blog
    }
    # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return render(request, 'first_app/index2.html', context)
