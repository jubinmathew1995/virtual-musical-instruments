var express = require('express');
var exphbs  = require('express-handlebars');
var bparse = require('body-parser');

var app = express();

//Listening port
var port = 3000;
var server = require('http').Server(app).listen(port,function(err,success) {
    console.log("Server is running at port "+port);
});

//Handlebars init
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// Body-parser init
app.use(bparse.urlencoded({ extended: false }));
app.use(bparse.json());

app.use(express.static(__dirname + '/public'));

/**
* Socket.io - web socket implementation
*/
var io = require('socket.io')(server);

io.sockets.on('connection', function (socket) {
    console.log('client connected');
});

// Make io accessible to our router
app.use(function(req,res,next){
    req.io = io;
    next();
});

// Routes
// HomePage
app.get('/', function (req, res) {
    res.render('home');
});

app.get('/data/:dataVal', function(req, res) {
	req.io.emit("data", req.params.dataVal);
	res.send("Got data");
});