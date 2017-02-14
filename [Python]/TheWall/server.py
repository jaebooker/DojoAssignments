from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
import md5
import os, binascii
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SecretBox"
mysql = MySQLConnector(app,'login2')
@app.route('/')
def index():
    query = "SELECT * FROM posts"
    login = mysql.query_db(query)           # run query with query_db()
    queryfury = "SELECT * FROM comments"
    comment = mysql.query_db(queryfury)
    return render_template('index.html', all_login=login, comments=comment) # pass data to our template

@app.route('/login/<login_id>')
def show(login_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM users WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': login_id}
    # Run query with inserted data.
    login = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_login=login[0])

@app.route('/login', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    if len(request.form['email']) < 2:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 2:
        flash("Name cannot be blank!")
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("I see you have a strange name. I don't like it. Conform!")
    elif len(request.form['last_name']) < 2:
        flash("Name cannot be blank!")
    elif not NAME_REGEX.match(request.form['last_name']):
       flash("I see you have a strange name. I don't like it. Conform!")
    elif len(request.form['password']) < 8:
         flash("We like our passwords the way we like our men")
    elif request.form['passconfirm'] != request.form['password']:
        flash("It's not the same!!!")
    else:
        flash("Success!")
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        salt = binascii.b2a_hex(os.urandom(15))
        query = "INSERT INTO users (email, first_name, last_name, pw_hash, salt) VALUES (:email, :first_name, :last_name, :pw_hash, :salt)"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': email,
                 'first_name': first_name,
                 'last_name': last_name,
                 'salt': salt,
                 'pw_hash': pw_hash
                 #'cryp_password': md5.new('password' + 'salt').hexdigest()
               }
        mysql.query_db(query, data)
    return redirect('/')
@app.route('/logingin', methods=['POST'])
def logingin():
 email = request.form['uemail']
 password = request.form['upassword']
 user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
 query_data = { 'email': email }
 user = mysql.query_db(user_query, query_data) # user will be returned in a list
 if bcrypt.check_password_hash(user[0]['pw_hash'], password):
     flash("that's a pass")
     session['user'] = user[0]['id']
     session['userfull'] = user[0]
     session['username'] = user[0]['first_name']
 else:
     flash("what the fuck was that?")
 return redirect('/')

@app.route('/post1', methods=['post'])
def post1():
    content = request.form['post1']
    query = "INSERT INTO posts (content, user_id) VALUES (:content, :user_id)"
    data = { 'content': content, 'user_id': session['user'] }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comment1/<login_id>', methods=['post'])
def comment1(login_id):
    content = request.form['comment1']
    query = "INSERT INTO comments (content, post_id, user_id) VALUES (:content, :post_id, :user_id)"
    data = { 'content': content, 'post_id': login_id, 'user_id': session['user'] }
    mysql.query_db(query, data)
    user_query = "SELECT * FROM comments WHERE post_id = :post_id"
    return redirect('/')

app.run(debug=True)
