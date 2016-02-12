<?php
session_start();
   //Check form verification
?>
<?php

if(isset($_POST['email'])) {



    // EDIT THE 2 LINES BELOW AS REQUIRED

    $email_to = "henrybi@uw.edu";
		//pugetfence@gmail.com
    $email_subject = "Free Estimate Form";





    function died($error) {

    // your error code can go here

        echo "We are very sorry, but there were error(s) found with the form you submitted. ";

        echo "These errors appear below.<br /><br />";

        echo $error."<br /><br />";

        echo "Please go back and fix these errors.<br /><br />";

        die();

    }



    // validation expected data exists

    if(!isset($_POST['first_name']) ||

        !isset($_POST['last_name']) ||

        !isset($_POST['email']) ||

        !isset($_POST['telephone'])) {

        died('We are sorry, but there appears to be a problem with the form you submitted.');

    }



    $first_name = $_POST['first_name']; // required

    $last_name = $_POST['last_name']; // required

    $email_from = $_POST['email']; // required

    $telephone = $_POST['telephone']; // required

    $address = $_POST['address'];

		$city = $_POST['city'];

		$zipcode = $_POST['zipcode'];

		$project = $_POST['project'];

		$material = $_POST['material'];

		$terrain = $_POST['terrain'];

		$size = $_POST['size'];

		$tree = $_POST['tree'];

		$fence = $_POST['fence'];

		$contact = $_POST['contact'];

    $comments = $_POST['comments'];



    $error_message = "";

    $email_exp = '/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/';

  if(!preg_match($email_exp,$email_from)) {

    $error_message .= 'The Email Address you entered does not appear to be valid.<br />';

  }

    $string_exp = "/^[A-Za-z .'-]+$/";

  if(!preg_match($string_exp,$first_name)) {

    $error_message .= 'The First Name you entered does not appear to be valid.<br />';

  }

  if(!preg_match($string_exp,$last_name)) {

    $error_message .= 'The Last Name you entered does not appear to be valid.<br />';

  }


  if(strlen($error_message) > 0) {

    died($error_message);

  }

    $email_message = "Form details below.\n\n";



    function clean_string($string) {

      $bad = array("content-type","bcc:","to:","cc:","href");

      return str_replace($bad,"",$string);

    }



    $email_message .= "First Name: ".clean_string($first_name)."\n";

    $email_message .= "Last Name: ".clean_string($last_name)."\n";

    $email_message .= "Email: ".clean_string($email_from)."\n";

    $email_message .= "Telephone: ".clean_string($telephone)."\n";

    $email_message .= "Street Address: ".clean_string($address)."\n";

    $email_message .= "City: ".clean_string($city)."\n";

		$email_message .= "Zip Code: ".clean_string($zipcode)."\n";

		$email_message .= "Project Type: ".clean_string($project)."\n";

		$email_message .= "Material Type: ".clean_string($material)."\n";

		$email_message .= "Terrain Description: ".clean_string($terrain)."\n";

		$email_message .= "Project Size: ".clean_string($size)."\n";

		$email_message .= "Tree Removal: ".clean_string($tree)."\n";

		$email_message .= "Fence Removal: ".clean_string($fence)."\n";

		$email_message .= "Best Time to Contact: ".clean_string($contact)."\n";

		$email_message .= "Comments: ".clean_string($comments)."\n";



// create email headers

$headers = 'From: '.$email_from."\r\n".

'Reply-To: '.$email_from."\r\n" .

'X-Mailer: PHP/' . phpversion();

@mail($email_to, $email_subject, $email_message, $headers);

?>



<!-- include your own success html here -->



Thank you for contacting us. We will be in touch with you very soon.



<?php

}

?>
