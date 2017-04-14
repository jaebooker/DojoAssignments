// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
var mongoose = require('mongoose');
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    res.render('index');
})
// Routes
// Root Request
// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/messageboard');
var Schema = mongoose.Schema;
var UserSchema = new mongoose.Schema({
 name: String,
 quote: String,
 _comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
})
mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
var User = mongoose.model('User') // We are retrieving this Schema from our Models, named 'User'
// This is the route that we already have in our server.js
// When the user presses the submit button on index.ejs it should send a post request to '/users'.  In
//  this route we should add the user to the database and then redirect to the root route (index view).
//mongoose.Promise = spherical.Promise;
// The root route -- we want to get all of the users from the database and then render the index view passing it all of the users
var commentSchema = new mongoose.Schema({
 // since this is a reference to a different document, the _ is the naming convention!
 commentName: String,
 comment: { type: String, required: true },
 _quote: {type: Schema.Types.ObjectId, ref: 'User'}
}, {timestamps: true });
app.post('/post', function(req, res) {
  console.log("POST", req.body);
  console.log("anything")
  // create a new User with the name and age corresponding to those from req.body
  var user = new User({name: req.body.name, quote: req.body.quote});
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  user.save(function(err, user) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
    } else { // else console.log that we did well and then redirect to the root route
      console.log('suddenly added a quote!');
      res.redirect('quotes');
    }
  })
})
app.get('/quotes', function(req, res) {
  User.find({}, function(err, user) {
    res.render('quotes', {user: user});
  })
})
app.post('/comment', function(req, res) {
  User.findOne({_id: req.params.id}, function(err, user){
    // data from form on the front end
    var comment = new Comment(req.body);
    //  set the reference like this:
    comment._quote = quote._id;
    // now save both to the DB
    comment.save(function(err){
            quote.comments.push(comment);
            quote.save(function(err){
                 if(err) {
                      console.log('Error');
                 } else {
                   console.log("success")
                      res.redirect('/');
                 }
             });
     });
});
})
mongoose.model("Comment", commentSchema);
var Comment = mongoose.model("Comment");
app.listen(8000, function() {
    console.log("listening on port 8000");
})
