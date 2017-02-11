from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "SecretBox"
mysql = MySQLConnector(app,'emailsdb')
@app.route('/')
def index():
    query = "SELECT * FROM emails"                           # define your query
    emails = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_emails=emails) # pass data to our template

@app.route('/emails/<email_id>')
def show(email_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM emails WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': email_id}
    # Run query with inserted data.
    emails = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_email=emails[0])

@app.route('/emails', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    if len(request.form['emails']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['emails']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        query = "INSERT INTO emails (emails, created_at, updated_at) VALUES (:emails, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'emails': request.form['emails'],
                 #'created_at':  request.form['created_at'],
                 #'updated_at': request.form['updated_at']
               }
        mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
