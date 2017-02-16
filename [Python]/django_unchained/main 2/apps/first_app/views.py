from django.shortcuts import render, HttpResponse, redirect
import random
import string

def yourMethodFromUrls(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    if 'count' not in request.session:
        request.session['count'] = 1
    return render(request,'first_app/index.html')
def create(request):
    stringletters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newstring = ""
    if request.method == 'POST':
        for x in range(0, 20):
            newstring += random.choice(stringletters)
        request.session['num'] = newstring
        request.session['count'] += 1
        return redirect('/')
    else:
        return redirect('/')
