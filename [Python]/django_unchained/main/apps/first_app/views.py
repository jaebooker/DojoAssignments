from django.shortcuts import render, HttpResponse, redirect
import string
import random

def survey1(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1000
    if 'message' not in request.session:
        request.session['message'] = "Welcome to the goldrush!"
    return render(request,'first_app/index.html')
def survery2(request):
    cavelives = 1
    farmlives = 1
    stashfind = 1
    if request.session['counter'] < 1:
        request.session['message'] = "Game over, man! Game over!"
        request.session['counter'] = 1000
        return redirect('/')
    elif request.POST['building'] == 'farm':
        request.session['counter'] -= 10
        request.session['counter'] += random.randrange(0,19)
        farmlives = random.randrange(-250,1000)
        if farmlives < 0:
            request.session['counter'] = 0
            request.session['message'] = "OH, GOD, WHY?! Why did you go next\
            door to look\
            for gold??? You should have\
            stayed away from them. Oh, gold. I feel sick.\
            This is all my fault.\
            This was meant to be fun! Now you're nothing but bones!\
            WHYYYYYYYY???!!!"
            return redirect('/')
        elif farmlives > 0:
            request.session['message'] = "It's a farm. It's boring.\
            But seriously, why do\
                the neighbors keep playing that banjo? It's starting\
                 to get to me"
            return redirect('/')
    elif request.POST['building'] == 'casino':
        request.session['counter'] -= 500
        request.session['counter'] += random.randrange(-2000,2500)
        if request.session['counter'] > 2000:
            request.session['message'] = "BIIIIIG LEEEAAAAGUUUEEEEEE!!!!!!"
            return redirect('/')
        elif request.session['counter'] > 2500:
            request.session['message'] = "You could become President one day"
            return redirect('/')
        elif request.session['counter'] < 2000:
            request.session['message'] = "Loser. Total loser.\
             Big disappointment, let me tell you. No energy. Weak."
            return redirect('/')
        elif request.session['counter'] < 1500:
            request.session['message'] = "No energy, total lightweight! \
            Just like Flask!"
            return redirect('/')
        elif request.session['counter'] < 1000:
            request.session['message'] = "Terrible! I know so much more about \
            casinos, let me tell you. And the media, they've rigged the whole\
             thing. Believe me, folks, what a rigged deal."
        elif request.session['counter'] < 500:
            request.session['message'] = "You make Jeb Bush look like a winner."
            return redirect('/')
        elif request.session['counter'] < 100:
            request.session['message'] = "WEAK! BAD! SAD! I'm gonna deport you!"
            return redirect('/')
    elif request.POST['building'] == 'our house in the middle of the street':
        request.session['counter'] -= 50
        request.session['counter'] += random.randrange(0,50)
        stashfind = random.randrange(-100,250)
        if stashfind > 200:
            request.session['counter'] += 10000
            request.session['message'] = "Hey! That's my stash!"
            return redirect('/')
        elif stashfind < 200:
            request.session['message'] = "It's a building. You search for drug\
             money, but don't find much. Er, treasure, you're looking for\
              treasure, not where I put my stash. But seriously,\
               if you find several rolls of hundred dollar bills and a pound of\
                cocain, contact me. It, uh, for the police, you know"
            return redirect('/')
    elif request.POST['building'] == 'cave':
        request.session['counter'] -= 0
        request.session['counter'] += random.randrange(0,200)
        cavelives = random.randrange(-5,30)
        if cavelives < 0:
            request.session['counter'] = 0
            request.session['message'] = "You died. Next time, find a caving\
             buddy"
            return redirect('/')
        elif cavelives >= 0:
            request.session['message'] = "You search the cave.\
             You hear some strange noises, but also find some gold"
            return redirect('/')
