
console.log($("input[name='first_name']").val());

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
                    tree: $("input[name='tree']").val(),
                    fence: $("input[name='fence']").val(),
                    call: $("input[name='contact']").val(),
                    comments: $("textarea[name='comments']").val()

                };

    e.preventDefault();
    $.ajax({
      type: "GET",
      url: "http://0.0.0.0:3000/",
      data: contactInfo
    });
  });
