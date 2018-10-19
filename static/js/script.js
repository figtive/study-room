function validateRegister() {
    var password = document.forms["registerForm"]["password"].value;
    var ver_password = document.forms["registerForm"]["ver_password"].value;
    var student_id = document.forms["registerForm"]["student_id"].value;
    if (password != ver_password) {
        alert("Passwords do not mathch.");
        return false;
    }

    if (student_id.toString().length() != 10) {
        return false;
    }
}

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
    });

    $("#registerForm").onsubmit(function (e) {

    });
});