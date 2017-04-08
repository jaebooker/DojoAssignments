var express = require("express");
var path = require("path");
var bodyParser = require("body-parser");
var app = express();
app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, "./static")));
app.set("views", path.join(__dirname, "./views"));
app.set("view engine", "ejs");
var server = app.listen(8000, function(){
  console.log("Good morning, Starshine, the Earth says 'Hello' at port 8000");
});
var route = require('./routes/index.js')(app,server);
// var io = require("socket.io").listen(server);
// io.sockets.on("connection", function(socket){
//   console.log('connection');
// })
// app.get("/", function(req, res){
//   res.render("index");
// })
