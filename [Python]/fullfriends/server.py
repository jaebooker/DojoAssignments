from flask import Flask, request, url_for, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "SecretBox"
mysql = MySQLConnector(app,'fullfriends')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', friends = friends)

@app.route('/friends', methods=['post'])
def create():
        if len(request.form['email']) < 1:
            flash("Email cannot be blank!")
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
        else:
            flash("Success!")
            query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
            # We'll then create a dictionary of data from the POST data received.
            data = {
                     'first_name': request.form['first_name'],
                     'last_name':  request.form['last_name'],
                     'email': request.form['email']
                   }
            mysql.query_db(query, data)
        return redirect('/')
@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        query = "UPDATE friends (first_name, last_name, email, updated_at) VALUES (:first_name, :last_name, :email, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'email': request.form['email']
               }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/retrieve/<id>', methods=['get'])
def update(id):
    query = "SELECT * from friends WHERE id = id"
    data = {
        'id': id
    }
    print 'stars**********************'
    mysql.query_db(query, data)
    return render_template('index2.html'), redirect('/friends/edit/<id>')
#@app.route('friends/<id>/murder')
#def murder(id):
    #pass

app.run(debug=True)
