var csrf = $('input[name=csrfmiddlewaretoken]').val();

msgNotification();

function msgNotification() {
    notif = $('#messagesNotification');
    setInterval(function() {
        $.ajax({
            url: "/chat/index/load-msg-notif/",
            method: "POST",
            data: {
                csrfmiddlewaretoken: csrf
            },
            success: function(response) {
                var rows = $('<li class="noti-item" id="room_' + response.data[response.data.length - 1]['id'] + '" sender="' + response.data[response.data.length - 1]['sender_username'] + '">\
                                    <a href="">\
                                    <div class="row">\
                                        <div class="form-group col-1"></div>\
                                        <img src=' + response.data[response.data.length - 1]['image'] + ' height="50px" width="50px" alt="">\
                                        <div class="meta">\
                                        <p>' + response.data[response.data.length - 1]['sender'] + '</p>\
                                        <p class="previewNotif">' + response.data[response.data.length - 1]['content'] + '</p>\
                                        </div>\
                                    </div>\
                                    </a>\
                                </li>');
                if ((notif.children().length == 0)) {
                    notif.prepend(rows);
                } else {
                    console.log("1");
                    if (notif.children().find("#room_" + response.data[response.data.length - 1]['id']) != 0) {
                        console.log(notif.find("#room_" + response.data[response.data.length - 1]['id']));
                        notif.find("#room_" + response.data[response.data.length - 1]['id']).remove();
                    }
                    notif.prepend(rows);
                    // rows.fadeIn("slow");
                    // console.log("2");
                    // } else {
                    //     notif.children(":first").attr('id', response.data[0]['id'].toString());
                    //     var preview = notif.find('#' + response.data[0]['id']).children().children().children().children('.previewNotif');
                    //     var newText = preview.text().replace(preview.text(), response.data[0]['content']);
                    //     preview.text(newText);
                    //     console.log("3");

                    // }
                }

                $('#amountOfMessages').text(response.data[0]['amountOfUnseen'].toString());

            }
        })

    }, 1000);
}