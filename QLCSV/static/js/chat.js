var csrf = $('input[name=csrfmiddlewaretoken]').val();

loadContacts();

function loadContacts() {
    setInterval(function() {
        load_contacts_ajax("");
    }, 1000);
}

function load_contacts_ajax(input) {
    var contacts = $('#contacts ul');
    $.ajax({
        url: "load-contacts/",
        method: "POST",
        data: {
            'input': input,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            //console.log(contacts.children(":first").attr('id'));
            if (contacts.children(":first").attr('id') != response.data[0]['id']) {
                if (contacts.find('#' + response.data[0]['id']).length != 0) {
                    contacts.prepend(contacts.children('#' + response.data[0]['id']));
                    changePreview(response.data[0]['id'], response.data[0]['lastMessage']);
                } else {
                    var user;
                    if (response.data[0]['user1'].username == username) {
                        user = response.data[0]['user2'];
                    } else {
                        user = response.data[0]['user1'];
                    }
                    var rows = $('<li class="contact"\
                        to="' + user.username + '"\
                        id = "' + response.data[0]['id'] + '" >\
                        <div class = "wrap" >\
                        <img src = "' + user.image + '" alt = "" >\
                        <div class = "meta"> \
                        <p class = "name1" >' + user.name + '</p>\
                        <p class = "preview" >' + response.data[0]['lastMessage'] + '</p>\
                        </div> \
                        </div>\
                        </li>');
                    contacts.prepend(rows);
                    // rows.fadeIn("slow");
                }

            } else {
                var preview = $('#contacts').find('#' + response.data[0]['id']).children().children().children(".preview");
                if (preview.text() != response.data[0]['lastMessage']) {
                    changePreview(response.data[0]['id'], response.data[0]['lastMessage']);
                }
            }

        }
    })
}

function changePreview(room_id, content) {
    var preview = $('#contacts').find('#' + room_id).children().children().children(".preview");
    var newText = preview.text().replace(preview.text(), content);
    preview.text(newText);

}

$('.contact').on('click', function() {
    //Acitve clicked account
    //Open chatbox
    $(this).siblings().removeClass('active');
    $(this).addClass('active');


    //Replace name in the header bar by clicked account
    var name = $(this).children().children().children(".name1").text();
    var curr_name = $('.contact-profile p');
    var newText = curr_name.text().replace(curr_name.text(), name);
    curr_name.text(newText);

    //Replace image in the header bar by clicked account
    $('.contact-profile img').attr('src', $(this).children().children("img").attr('src'));

    room_id = $(this).attr('id');
    //setInterval(function() {

    $.ajax({
            url: "get-messages/",
            method: "POST",
            data: {
                'receiver': $(this).attr('to'),
                'room_id': room_id,
                csrfmiddlewaretoken: csrf
            },
            success: function(response) {
                $(".messages ul li").remove();
                for (var i = 0; i < response.data.length; i++) {
                    if (response.data[i]['user'] === username) {

                        var rows = $('<li class="sent">\
                <img src="' + response.data[i]['image'] + '" alt="" /><p>' + response.data[i]['content'] + '</p></li>');
                    } else {
                        var rows = $('<li class="replies">\
                <img src="' + response.data[i]['image'] + '" alt="" /><p>' + response.data[i]['content'] + '</p></li>');
                    }
                    rows.appendTo($('.messages ul'));
                    rows.fadeIn("slow");
                }
                changePreview(room_id, response.data[response.data.length - 1]['content']);

            }
        })
        // }, 1000);

});


function newMessage() {
    var messagesContainer = $(".messages");
    message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><img src="' + imageurl + '" alt="" /><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $.ajax({
        url: "create-msg/",
        method: "POST",
        data: {
            'username': username,
            'room_id': room_id,
            'message': message,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {}
    })
    $('.message-input input').val(null);
    $('.contact.active .preview-mess').html('<span>You: </span>' + message);
    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
};


$('.chat_btn').on('click', function() {
    var username = $(this).parents().siblings('.acc-username').text();
    check_room(username);

});

$('.submit').click(function() {
    newMessage();
});

function sendMsg(event) {
    if (event.which == 13) {
        newMessage();
        return false;
    }
}

function searchContact() {
    search = $("#search input").val();
    if ($.trim(search) == '') {
        return false;
    }
    load_contacts_ajax(search);
}

function check_room(username) {
    $.ajax({
        url: '/chat/index/check-room/',
        method: "POST",
        data: {
            'toUser': username,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            window.location.href = '/chat/index/';
        }
    })
}