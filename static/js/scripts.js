$("form[name=signup_form]").submit(function(e){
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href="/dashboard/";
        },
        error: function(resp){
            console.log(resp)
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});


$("form[name=login_form]").submit(function(e){
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href="/dashboard/";
        },
        error: function(resp){
            console.log(resp)
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
})

$("form[name=forgot_password]").submit(function(e){
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/forgot-password",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp)
            $error.text(resp.success).removeClass("error-message").addClass("success-message").removeClass("error--hidden"); 
        },
        error: function(resp){
            console.log(resp)
            $error.text(resp.responseJSON.error).removeClass("success-message").addClass("error-message").removeClass("error--hidden");
        }
    });

    e.preventDefault();
})
