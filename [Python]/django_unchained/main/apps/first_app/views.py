from django.shortcuts import render, HttpResponse, redirect

def survey1(request):
    return render(request,'first_app/index.html')
def survey2(request):
    if request.method == "POST":
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        request.session['comments'] = request.POST['comments']
    return redirect('/result')
def survey3(request):
    return render(request,'first_app/index2.html')
