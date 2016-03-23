(function(){
var formInfo = {"party":"party"};

  $("form").on("submit", function(e){
    // e.preventDefault();
    console.log("sent");
    $.ajax({
      type: "POST",
      url: "http://puget-fence-llc.herokuapp.com",
      data: formInfo
    });
  });

})();
