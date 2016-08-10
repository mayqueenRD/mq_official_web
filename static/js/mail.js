$("form").on("submit", function(e){
  var contactInfo = {name: $("input[name='first_name']").val() + " " + $("input[name='last_name']").val(),
                  email: $("input[name='email']").val(),
                  number: $("input[name='telephone']").val(),
                  address: $("input[name='address']").val(),
                  city: $("input[name='city']").val(),
                  zipcode: $("input[name='zipcode']").val(),
                  project: $("select[name='project']").val(),
                  material: $("select[name='material']").val(),
                  terrain: $("select[name='terrain']").val(),
                  size: $("select[name='size']").val(),
                  tree: $("input[name='tree']:checked").val(),
                  fence: $("input[name='fence']:checked").val(),
                  call: $("input[name='contact']").val(),
                  comments: $("textarea[name='comments']").val()
              };

  e.preventDefault();
  console.log("ben and henry");
  $.ajax({
    type: "GET",
    url: "http://puget-fence-llc.herokuapp.com/submit",
    data: contactInfo
  });
  $('.submitInfo').show();
  document.getElementById("contactform").reset();
});

$('.submitInfo').on('click', function(event) {
  $('.submitInfo').hide();
});
