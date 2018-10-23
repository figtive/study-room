$(document).ready(function () {
    $("#student_id_field").keydown(function (e) {
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
            (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
            (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
            (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
            (e.keyCode >= 35 && e.keyCode <= 39)) {
            return;
        }
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    })

    $("#registerForm").parsley({
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<span class="invalid-feedback form-notice"></span>',
        errorTemplate: '<span></span>',
        trigger: 'change'
    })

    $("#loginForm").parsley({
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<span class="invalid-feedback form-notice"></span>',
        errorTemplate: '<span></span>',
        trigger: 'change'
    })

    $("#rsvpForm").parsley({
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<span class="invalid-feedback form-notice"></span>',
        errorTemplate: '<span></span>',
        trigger: 'change'
    })
});

window.Parsley.addValidator('studentid', {
    validateString: function (value) {
        var i;
        var even = 0;
        var odd = 0;
        if (value.length == 10) {
            for (i = 0; i < 9; i++) {
                var num = parseInt(value.charAt(i));
                if (i % 2 == 0) {
                    even = even + (3 * num);
                } else {
                    odd = odd + num;
                }
            }
            return (even + odd) % 7 == parseInt(value.charAt(9));
        }
        return false;
    },
    messages: {
        en: 'Please enter a valid Student ID!'
    }
});
