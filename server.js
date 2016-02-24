var express = require('express');
var nodemailer = require("nodemailer");
var smtpTransport = require("nodemailer-smtp-transport");
var app = express();

var smtpTransport = nodemailer.createTransport(smtpTransport({
    host : "smtp.gmail.com",
    auth : {
        user : "henrybidesign@gmail.com",
        pass : "Orange999999999"
    }
}));
app.get('/send',function(req,res){
    var mailOptions={
        from : "henrybidesign@gmail.com",
        to : "henrybi@uw.edu",
        subject : "Node Mailer",
        text : "Your Text",
        html : "HTML GENERATED",
        attachments : [
            {   // file on disk as an attachment
                filename: 'text3.txt',
                path: 'Your File path' // stream this file
            }
        ]
    };
    console.log(mailOptions);
    smtpTransport.sendMail(mailOptions, function(error, response){
        if(error){
            console.log(error);
            res.end("error");
        }else{
            console.log(response.response.toString());
            console.log("Message sent: " + response.message);
            res.end("sent");
        }
    });
});


app.listen(3000,function(){
    console.log("Express Started on Port 3000");
});
