var express = require('express');
var nodemailer = require("nodemailer");
var app = express();

var smtpTransport = nodemailer.createTransport("SMTP",{
    service: "Gmail",
    auth: {
        user: "henrybidesign@gmail.com",
        pass: "Orange999999999"
    }
});

app.get('/send',function(req,res){
  var mailOptions = {
    to : "henrybi@uw.edu",
    subject : "test",
    text : "test"
  };
  console.log(mailOptions);

  smtpTransport.sendMail(mailOptions, function(error, response){
    if(error){
    console.log(error);
    res.end("error");
    }else{
    console.log("Message sent: " + response.message);
    res.end("sent");
    }
  });
});

app.listen(3000, function(){
console.log("Express Started on Port 3000");
});
