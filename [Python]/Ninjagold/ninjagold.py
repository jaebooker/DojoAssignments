import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretBox'
@app.route('/')
def index():
    try:
        session['counter'] = 1000
    except KeyError:
		session['counter'] = 1000
    return render_template("ninjagold.html")
@app.route('/process_money', methods=['post'])
def NinjaCasino():
    cavelives = 1
    farmlives = 1
    stashfind = 1
    if session['counter'] == 0:
        return render_template("ninjagold.html", message="Game over, man. Game over.")
    elif request.form['building'] == 'farm':
        session['counter'] -= 10
        session['counter'] += random.randrange(0,19)
        farmlives = random.randrange(-250,1000)
        if farmlives < 0:
            session['counter'] = 0
            return render_template("ninjagold.html", message="OH, GOD, WHY?! Why did you go next door to look for gold??? You should have stayed away from them. Oh, gold. I feel sick. This is all my fault. This was meant to be fun! Now you're nothing but bones! WHYYYYYYYY???!!!")
        elif farmlives > 0:
            return render_template("ninjagold.html", message="It's a farm. It's boring. But seriously, why do the neighbors keep playing that banjo? It's starting to get to me")
    elif request.form['building'] == 'casino':
        session['counter'] -= 500
        session['counter'] += random.randrange(-2000,2500)
        if session['counter'] > 2000:
            return render_template("ninjagold.html", message="BIIIIIG LEEEAAAAGUUUEEEEEE!!!!!!")
        elif session['counter'] > 2500:
            return render_template("ninjagold.html", message="You could become President one day")
        elif session['counter'] < 2000:
            return render_template("ninjagold.html", message="Loser. Total loser. Big disappointment, let me tell you. No energy. Weak.")
    elif request.form['building'] == 'our house in the middle of the street':
        session['counter'] -= 50
        session['counter'] += random.randrange(0,50)
        stashfind = random.randrange(-100,250)
        if stashfind > 200:
            session['counter'] += 10000
            return render_template("ninjagold.html", message="Hey! That's my stash!")
        elif stashfind < 200:
            return render_template("ninjagold.html", message="It's a building. You search for drug money, but don't find much. Er, treasure, you're looking for treasure, not where I put my stash. But seriously, if you find several rolls of hundred dollar bills and a pound of cocain, contact me. It, uh, for the police, you know")
    elif request.form['building'] == 'cave':
        session['counter'] -= 0
        session['counter'] += random.randrange(0,200)
        cavelives = random.randrange(-5,30)
        if cavelives < 0:
            session['counter'] = 0
            return render_template("ninjagold.html", message="You died. Next time, find a cave buddy")
        elif cavelives >= 0:
            return render_template("ninjagold.html", message="You search the cave. You hear some strange noises, but also find some gold")

app.run(debug=True)
