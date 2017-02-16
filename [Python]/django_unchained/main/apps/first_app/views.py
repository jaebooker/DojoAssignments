from django.shortcuts import render, HttpResponse
from datetime import datetime

def yourMethodFromUrls(request):
    context = {
    "somekey": str(datetime.now())
    }
    return render(request,'first_app/index.html', context)
