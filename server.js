var express = require('express');
var nodemailer = require("nodemailer");

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



var mailOptions = {
  from: '"Henry Bi 👥" <henrybidesign@gmail.com>',
  to : "henrybi@uw.edu",
  subject : "test",
  text : "test",
  html: '<b>Hello world 🐴</b>'
};

transporter.sendMail(mailOptions, function(error, info){
    if(error){
        return console.log(error);
    }
    console.log('Message sent: ' + info.response);
});

// app.listen(3000, function(){
// console.log("Express Started on Port 3000");
// });
