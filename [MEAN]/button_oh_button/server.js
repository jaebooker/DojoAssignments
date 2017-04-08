var express = require("express");
var path = require("path");
// var bodyParser = require("body-parser");
var app = express();
// app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, "./static")));
app.set("views", path.join(__dirname, "./views"));
app.set("view engine", "ejs");
var server = app.listen(3000, function(){
  console.log("Good morning, Starshine, the Earth says 'Hello' at port 3000");
});
var io = require("socket.io").listen(server);
var counter = 0;
io.sockets.on("connection", function(socket){
  console.log('connection');
  socket.on("push_button", function(data){
    counter += 1;
    console.log("button")
    io.emit("push_counter", {response: counter});
  });
  socket.on("reset_counter", function(data){
    counter = 0;
    io.emit("reset_response", {response: counter});
  })
})

app.get("/", function(req, res){
  res.render("index");
})


// var route = require("./routes/index.js")(app, server);
