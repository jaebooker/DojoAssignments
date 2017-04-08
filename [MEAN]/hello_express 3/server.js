var express = require("express");
var bodyParser = require('body-parser');
var path = require('path');
var app = express();

app.use(bodyParser.urlencoded());
app.use(express.static(path.join( __dirname + "./static")));
app.set("views", path.join(__dirname, "./views"));
app.set('view engine', 'ejs');

var server = app.listen(3000, function(){
  console.log("working...")
})
var route = require("./routes/index.js")(app, server);
