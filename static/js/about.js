$(document).ready(function () {
    $('#testimony-form').submit(function () {
        event.preventDefault()
        var data = $(this).serializeArray().reduce(function(obj, item) {
            obj[item.name] = item.value
            return obj
        }, {})
        $.ajax({
            url: "add-about/",
            method: "POST",
            data: {
                csrfmiddlewaretoken: data.csrfmiddlewaretoken,
                content: data["content"],
            },
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", data.csrfmiddlewaretoken)
                }
            },
            success: function(response) {
                $('').append("")
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
