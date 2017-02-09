import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretBox'
@app.route('/')
def index():
    try:
        session['counter'] = random.randrange(0,101)
    except KeyError:
		session['counter'] = random.randrange(0,101) # random number between 0-100
    return render_template("numbergames.html")
@app.route('/', methods=['POST'])
def create():
    number = int(request.form["form2"])
    if number == int(session['counter']):
        return render_template("numbergames.html", message="I don't accept the outcome of your guess. What a rigged deal, folks. No one knows numbers better than me, let me tell you. This is fake news!")
        print "gold!"
    elif number != int(session['counter']):
        #return render_template("numbergames.html", message="Wrong!")
        print "this is wrong"
        if number < int(session['counter']):
            return render_template("numbergames.html", message="WRONG! You're very low energy!")
        elif number > int(session['counter']):
            return render_template("numbergames.html", message="WRONG! Have you seen my number? It's so high, you have no idea. Everyone's been telling me so. And the media, they, they just don't know what to do. Bunch of losers, let me tell you. These random numbers, they're a rigged deal. Totally rigged.")
app.run(debug=True)
