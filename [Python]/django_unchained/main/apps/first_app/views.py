from django.shortcuts import render, HttpResponse, redirect

def survey1(request):
    return render(request,'first_app/index.html')
def survery2(request):
    return render(request,'first_app/index3.html')
def survey3(request, color):
    context = {
        'color': color
    }
    return render(request,'first_app/index2.html', context)
