$(document).ready(function() {
    $("#student-id").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
             // Allow: Ctrl/cmd+A
            (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+C
            (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: Ctrl/cmd+X
            (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    })

    $("#registerForm    ").parsley({
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<span class="form-text text-danger"></span>',
        errorTemplate: '<span></span>',
        trigger: 'change'
    })


    // $("#registerForm").onsubmit(function (e) {
    //     e.preventDefault();
    //     var name = $('#name_field').val();
    //     var email = $('#email_field').val();
    //     var username = $('#username_field').val();
    //     var student_id = $('#student_id_field').val();
    //     var password = $('#password_field').val();
    //     var ver_password = $('#ver_password_field').val();
    
    //     $(".error").remove();
    
    //     if (name.length < 1) {
    //         $('#name_field').after('<span class="error">This field is required</span>');
    //     }
        
    //     if (email.length < 1) {
    //         $('#email').after('<span class="error">This field is required</span>');
    //     } else {
    //         var regEx = /^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
    //         var validEmail = regEx.test(email);
    //         if (!validEmail) {
    //             $('#email_field').after('<span class="error">Enter a valid email</span>');
    //         }
    //     }

    //     if (username.length < 1) {
    //         $('#username_field').after('<span class="error">This field is required</span>');
    //     }

    //     if (student_id.toString().length() != 10) {
    //         $('#student_id_field').after('<span class="error">Student ID is invalid</span>');
    //     }

    //     if (password.length < 8) {
    //         $('#password_field').after('<span class="error">Password must be at least 8 characters long</span>');
    //     }

    //     if (password.length != ver_password) {
    //         $('#password_field').after('<span class="error">Passwords do not match</span>');
    //     }
    // });
});


// function validateRegister() {
//     var name = document.forms['registerForm']['name_field'].value()
//     console.log(name);
//     return false;
// }