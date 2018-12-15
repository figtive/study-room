$(document).ready(function () {
    $("#aboutForm").parsley({
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<span class="invalid-feedback form-notice"></span>',
        errorTemplate: '<span></span>',
        trigger: 'change'
    })

    $('#aboutForm').submit(function () {
        event.preventDefault();
        var data = $(this).serializeArray().reduce(function(obj, item) {
            obj[item.name] = item.value
            return obj
        }, {})
        $.ajax({
            url: "add-about/",
            method: "POST",
            data: {
                about_post: data["about_post"],
            },
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", data.csrfmiddlewaretoken)
                }
            },
            success: function(response) {
                var today = new Date();
                var month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
                var html = '\
                <div class="row">\
                    <div class="col-lg-12">\
                        <div class="card clickable-card event-card shadow" data-toggle="modal">\
                            <div class="card-flex">\
                                <div class="content-colorbox color-about">\
                                    <div class="event-date">\
                                        <p>' + today.getDate() + '</p>\
                                    </div>\
                                    <div class="event-month">\
                                        <p>' + month[today.getMonth()] + '</p>\
                                    </div>\
                                </div>\
                                <div class="card-body">\
                                    <h5 class="card-title news-title">\
                                        ' + data["name"] + '\
                                    </h5>\
                                    <div class="card-text news-content">\
                                        ' + data["about_post"] + '\
                                    </div>\
                                </div>\
                            </div>\
                        </div>\
                    </div>\
                </div>'

                $('.testimony-list').prepend(html)
                $('#about_field').val("")
            }, 
            error: function(response) {
                alert("Sorry, your testimony cannot be submitted. Try again later.")
            }
        })
    })

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
    }
})
