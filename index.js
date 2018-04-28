var express = require('express');
var exphbs  = require('express-handlebars');
var bparse = require('body-parser');

var app = express();

//Listening port
app.listen(3000);
console.log('Listening at port 3000');

//Handlebars init
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

// Body-parser init
app.use(bparse.urlencoded({ extended: false }));
app.use(bparse.json());

app.use(express.static(__dirname + '/public'));

// Routes
// HomePage
app.get('/', function (req, res) {
    res.render('home');
});