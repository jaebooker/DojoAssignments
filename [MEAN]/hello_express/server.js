var express = require("express");
var bodyParser = require('body-parser');
var path = require('path');
var app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join( __dirname + "/static")));
app.set("views", path.join(__dirname, "./views"));
app.set('view engine', 'ejs');

var route = require("./routes/index.js")(app)
// app.get('/', function(request, response){
//   response.send("Good morning, Starshine, the Earth says 'Hello'!")
// })
app.listen(3000, function(){
  console.log("working...")
})
// app.set('views', __dirname + '/views');
// // Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
// app.get("/users", function (request, response){
//     var users_array = [
//         {name: "Michael", email: "michael@codingdojo.com"},
//         {name: "Jay", email: "jay@codingdojo.com"},
//         {name: "Brendan", email: "brendan@codingdojo.com"},
//         {name: "Andrew", email: "andrew@codingdojo.com"}
//     ];
//     response.render('users', {users: users_array});
// })
// // root route
// app.get('/', function (req, res){
//   res.render('index', {title: "my Express project"});
// });
//
// // route to process new user form data:
// app.post('/users', function (req, res){
//   console.log("POST DATA \n\n", req.body
//   // code to add user to db goes here!
//   // redirect the user back to the root route.
//   // All we do is specify the URL we want to go to:
//   res.redirect('/');
// })
// app.get("/users/:id", function (req, res){
//     console.log("The user id requested is:", req.params.id);
//     // just to illustrate that req.params is usable here:
//     res.send("You requested the user with id: " + req.params.id);
//     // code to get user from db goes here, etc...
// });
