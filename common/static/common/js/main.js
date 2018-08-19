// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function HTTPSafeMethodTest(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
// ... the AJAX request is successful
let updatePage = function (resp) {
    $('#result').html(JSON.stringify(resp));
    //console.log(JSON.parse(resp));
};

// ... the AJAX request fails
let printError = function (req, status, err) {
    console.log('something went wrong', status, err);
};
$.ajaxSetup({
    beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
})


function doAjax() {
    let myfname = $('#id_firstName').val();
    // Create an object to describe the AJAX request
    let ajaxOptions = {
        url: '/ajaxView',
        type: 'POST',
        dataType: 'json',
        data: {
            firstName: myfname
        },
        success: updatePage,
        error: printError,
    };
    $.ajax(ajaxOptions);
}
//js for nav in responsive mode


function submitIdAJAX(sender, endpoint) {
    let did = $(sender).data('id');
    $.ajax({
        url: endpoint,
        data: {
            id: did
        },
        dataType: 'JSON',
        method: 'POST',
        success: function (result) {
            console.log('success:' + result.msg);
        ;debugger

            let noticeBox = $('#notice');
            noticeBox.removeClass('alert-danger');
            noticeBox.addClass('alert-info');
            noticeBox.removeClass('d-none');
            noticeBox.html(result.msg);
        },
        error: function () {
            console.log('ERROR:submitReservation failed');
            let noticeBox = $('#notice');
            noticeBox.removeClass('alert-info');
            noticeBox.addClass('alert-danger');
            noticeBox.removeClass('d-none');
            noticeBox.html('<strong>خطا</strong>');
        }
    })
}


function myFunction() {
    let txt;
    let question = window.confirm("are u sure?");
    if (question == true) {
        // txt = "درخواست شما ثبت شد";
        submitIdAJAX(sender,endpoint);
    }
    // document.getElementById("demo").innerHTML = txt;
}
// https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt manba