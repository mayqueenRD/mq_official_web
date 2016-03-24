var express = require('express');
var app = express();
var http = require('http');
var nodemailer = require("nodemailer");


app.use(express.static(__dirname + '/'));

app.get('/', function(req, res){
  res.sendfile(__dirname + '/index.html');
});

app.get('/submit', function(req, res){

  var smtpConfig = {
      host: 'smtp.gmail.com',
      port: 465,
      secure: true, // use SSL
      auth: {
          user: "honghaobitest@gmail.com",
          pass: "test1234567890"
      }
  };

  var transporter = nodemailer.createTransport(smtpConfig);
  console.log(req.query.tree);
  var mailOptions = {
    from: req.query.name + " 👥 " + req.query.email,
    to: "henrybi@uw.edu",
    subject: "New Request for Pricing Estimate",
    text: "New Contact Estimate",
    html: "<h4>Hi Ben, You have a new contact requesting for an estimate</h4><br>" +
    "Client Name: <b>" + req.query.name + "</b><br>"  +
    "Email Address: <b>" + req.query.email + "</b><br>" +
    "Telephone Number: <b>" + req.query.number + "</b><br>" +
    "Address: <b>" + req.query.address + "</b><br><b>" + req.query.city + " </b>, <b>" + req.query.zipcode + "</b><br>" +
    "Project Type: <b>" + req.query.project + "</b><br>" +
    "Fencing Material: <b>" + req.query.material + "</b><br>" +
    "Terrain Description: <b>" + req.query.terrain + "</b><br>" +
    "Project Size: <b>" + req.query.size + "</b><br>" +
    "Existing Tree Removal: <b>" + req.query.tree + "</b><br>" +
    "Existing Fence Removal: <b>" + req.query.fence + "</b><br>" +
    "Best Time to Call: <b>" + req.query.call + "</b><br>" +
    "Other Comments: <b>" + req.query.comments + "</b><br>"
  };

  transporter.sendMail(mailOptions, function(error, info){
      if(error){
          return console.log(error);
      }
      console.log('Message sent: ' + info.response);
  });

  console.log(mailOptions);

  res.send('sent');
});

var port = process.env.PORT || 3000;

app.listen(port, function(){
  console.log('listening on *:' + port);
});
