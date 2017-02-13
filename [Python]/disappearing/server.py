from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/ninja/')
def index2():
    color = 'tmnt.png'
    return render_template("index2.html", color=color)
@app.route('/ninja/<color>/')
def ninjaindex(color):
    if color == 'blue':
        color = 'leonardo.jpg'
    elif color == 'red':
        color = 'raphael.jpg'
    elif color == 'orange':
        color = 'michelangelo.jpg'
    elif color == 'purple':
        color = 'donatello.jpg'
    else:
        color = 'noninja.jpg'
    return render_template("index2.html", color=color)
app.run(debug=True)
