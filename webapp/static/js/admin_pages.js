$(function(){
    var loading = false;
    $(".vTextField,.vLargeTextField").each(function(){
        var str_id = $(this).attr("id");
        //var str_val = $(this).val();
        var go = false;
        if( str_id.includes("id_translations") && str_id.includes("0") && str_id.includes("-title") ){
            go = true;
        }
        if( str_id.includes("id_translations") && str_id.includes("0") && str_id.includes("-subtitle") ){
            go = true;
        }
        if( str_id.includes("id_translations") && str_id.includes("0") && str_id.includes("-slug") ){
            go = true;
        }
        if( str_id.includes("id_translations") && str_id.includes("0") && str_id.includes("-content") ){
            go = true;
        }
        if(go){
            var url = new URL(window.location.href);
            var lang = "en";
            try { lang = url.searchParams.get("language", "en");
            } catch (e) { lang = "en"; }
            if (!lang) { lang = "en"; }

            if(lang != "en") {
                $(this).after("<span class='aws-button' id='aws-" + str_id + "'>" +
                    "<img style='height:28px;margin-left: 10px;margin-top: 5px' " +
                    " title='Update " + str_id.replace("id_translations-0-", "") + "' src='/static/img/icon-aws.png'/></a></span>");
                $("#aws-" + str_id).click(function () {
                    if (loading == false) {
                        loading = true;
                        $(this).find("img").attr("src", "/static/img/spinner.gif").css({
                            "position": "relative",
                            "top": "3px", "height": "16px",
                            "margin-left": "25px", "margin-right": "16px",
                            "margin-bottom": "11px", "margin-top": "6px"
                        });
                        var content;
                        try {
                            content = tinyMCE.get(str_id).getContent();
                        } catch (e) {
                            content = $("#" + str_id).val();
                        }

                        $.ajax({
                            url: "/admin/translate/",
                            method: "POST",
                            data: {
                                "text": content,
                                "language": lang
                            },
                            success: function (response) {
                                try {
                                    tinymce.get(str_id).setContent(response["translated"]);
                                } catch (e) {
                                    $("#" + str_id).val(response["translated"]);
                                }
                                loading = false;
                                $("#aws-" + str_id).find("img").attr("src", "/static/img/icon-aws.png").css({
                                    "position": "relative",
                                    "top": "0", "height": "28px",
                                    "margin-left": "10px", "margin-right": "0",
                                    "margin-bottom": "0", "margin-top": "5px"
                                });
                            }
                        });
                    }
                });
            }
        }
    });
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

