function deleteStudent() {
    if (confirm('Are you sure you want to delete this item?')) {
        var Username = [];
        var csrf = $('input[name=csrfmiddlewaretoken]').val();
        $(':checkbox:checked').each(function(i) {
            Username[i] = $(this).val();
        })
        if (Username.length === 0) {
            alert('Please select an item to delete!');
        } else {
            $.ajax({
                url: "delete-student/",
                method: "POST",
                data: {
                    Username,
                    csrfmiddlewaretoken: csrf
                },
                success: function(response) {
                    for (var i = 0; i < Username.length; i++) {
                        $('tr#' + Username[i] + '').fadeOut('slow')
                    }
                }
            })
        }
    }
}

function searchStudent() {
    var grade = $('#select_grade').find(":selected").text();
    var address = $('#select_address').find(":selected").text();
    var major = $('#select_major').find(":selected").text();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: "/list/search-student/",
        method: "POST",
        data: {
            'grade': grade,
            'address': address,
            'major': major,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            var rowCount = $('table#student_data tr:last').index() + 1;
            if (rowCount > 1) {
                $('#' + 'student_data tr td').fadeOut('fast', function() {
                    $(this).parent().remove();
                });
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["DateOfBirth"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["Username"] + "'>\
                            <td><input type='checkbox' name='studentUsername[]' value='" + response.data[i]["Username"] + "' id='delete-student'></td>\
                            <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["Username"] + "\"> " + response.data[i]["Username"] + "</a></td>\
                            <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["Username"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                            <td>" + date + "</td>\
                            <td>" + response.data[i]["Gender"] + "</td>\
                            <td>" + response.data[i]["Major"] + "</td>\
                            <td>" + (response.data[i]["currentAddress"] || "") + "</td>\
                            <td>" + (response.data[i]["PhoneNumber"] || "") + "</td>\
                            </tr>");
                    rows.hide();
                    tb.after(rows);
                    rows.fadeIn("slow");
                }

            } else {
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["DateOfBirth"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["Username"] + "'>\
                                    <td><input type='checkbox' name='studentUsername[]' value='" + response.data[i]["Username"] + "' id='delete-student'></td>\
                                    <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["Username"] + "\"> " + response.data[i]["Username"] + "</a></td>\
                                    <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["Username"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                                    <td>" + date + "</td>\
                                    <td>" + response.data[i]["Gender"] + "</td>\
                                    <td>" + response.data[i]["Major"] + "</td>\
                                    <td>" + (response.data[i]["currentAddress"] || "") + "</td>\
                                    <td>" + (response.data[i]["PhoneNumber"] || "") + "</td>\
                                    </tr>");
                    rows.hide();
                    tb.after(rows);
                    rows.fadeIn("slow");
                }
            }

            // $('#' + 'student_data tr td').fadeIn('fast', function() {
            //     $('#' + 'student_data tr td').remove();
            // });

        },
        error: function() {
            console.log("No data");
        }
    })
}