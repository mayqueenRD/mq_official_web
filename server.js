var express = require('express');
var app = express();
var nodemailer = require("nodemailer");
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies

app.get('/', function(req, res){

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
    subject: "fence pricing estimate",
    text: "estimate",
    html: "<h4>Hello Ben 🐴, You have a contact to make for an estimate</h4> <br>" +
    "Client Name: " + req.query.name + "<br>"  +
    "Email Address: " + req.query.email + "<br>" +
    "Telephone Number: " + req.query.number + "<br>" +
    "Address: " + req.query.address + "<br>" + req.query.city + " , " + req.query.zipcode + "<br>" +
    "Project Type: " + req.query.project + "<br>" +
    "Fencing Material: " + req.query.material + "<br>" +
    "Terrain Description: " + req.query.terrain + "<br>" +
    "Project Size: " + req.query.size + "<br>" +
    "Existing Tree Removal: " + req.query.tree + "<br>" +
    "Existing Fence Removal: " + req.query.fence + "<br>" +
    "Best Time to Call: " + req.query.call + "<br>" +
    "Other Comments: " + req.query.comments + "<br>"
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

app.listen(3000, function(){
console.log("Express Started on Port 3000");
});
