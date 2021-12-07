function searchDonation() {
    var searchInputDonation = $('#searchInputDonation').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: "/donation/search-donation/",
        method: "POST",
        data: {
            'searchInputDonation': searchInputDonation,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            var rowCount = $('table#student_data tr:last').index() + 1;
            if (rowCount > 0) {
                $('#' + 'student_data tr td').fadeOut('fast', function() {
                    $(this).parent().remove();
                });
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["DonationDate"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                            <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                            <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                            <td>" + response.data[i]["AmountOfDonation"] + "</td>\
                            <td>" + response.data[i]["Messages"] + "</td>\
                            <td>" + date + "</td>\
                            </tr>");
                    rows.hide();
                    tb.after(rows);
                    rows.fadeIn("slow");
                }

            } else {
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["DonationDate"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                                <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                                <td> <a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                                <td>" + response.data[i]["AmountOfDonation"] + "</td>\
                                <td>" + response.data[i]["Messages"] + "</td>\
                                <td>" + date + "</td>\
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

function searchPressDonation(event) {
    if (event.which == 13) {
        searchDonation();
    }
}

function searchPressRegs(event) {
    if (event.which == 13) {
        searchRegs();
    }
}

function searchPressIntroduce(event) {
    if (event.which == 13) {
        searchIntroduce();
    }
}


function searchRegs() {
    var searchInputRegs = $('#searchInputRegs').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: "/donation/search-regs/",
        method: "POST",
        data: {
            'searchInputRegs': searchInputRegs,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            var rowCount = $('table#student_data tr:last').index() + 1;
            if (rowCount > 0) {
                $('#' + 'student_data tr td').fadeOut('fast', function() {
                    $(this).parent().remove();
                });
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["teach_date"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                            <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                            <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                            <td>" + response.data[i]["teach_title"] + "</td>\
                            <td>" + response.data[i]["teach_mess"] + "</td>\
                            <td>" + date + "</td>\
                            </tr>");
                    rows.hide();
                    tb.after(rows);
                    rows.fadeIn("slow");
                }

            } else {
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var date = response.data[i]["teach_date"].replace(/^"(.*)"$/, '$1');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                    <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                    <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                    <td>" + response.data[i]["teach_title"] + "</td>\
                    <td>" + response.data[i]["teach_mess"] + "</td>\
                    <td>" + date + "</td>\
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

function searchIntroduce() {
    var searchInputIntroduce = $('#searchInputIntroduce').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: "/donation/search-introduce/",
        method: "POST",
        data: {
            'searchInputIntroduce': searchInputIntroduce,
            csrfmiddlewaretoken: csrf
        },
        success: function(response) {
            var rowCount = $('table#student_data tr:last').index() + 1;
            if (rowCount > 0) {
                $('#' + 'student_data tr td').fadeOut('fast', function() {
                    $(this).parent().remove();
                });
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                            <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                            <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                            <td>" + (response.data[i]["intro_title"] || "") + "</td>\
                            <td>" + response.data[i]["intro_content"] + "</td>\
                            </tr>");
                    rows.hide();
                    tb.after(rows);
                    rows.fadeIn("slow");
                }

            } else {
                for (var i = 0; i < response.data.length; i++) {
                    var tb = $('#student_data tr:last-child');
                    var rows = $("<tr id='" + response.data[i]["StudentCode"] + "'>\
                                <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["StudentCode"] + "</a></td>\
                                <td><a href=\"" + "/userInfo/profile/" + response.data[i]["StudentCode"] + "\"> " + response.data[i]["FirstName"] + " " + response.data[i]["LastName"] + "</a></td>\
                                <td>" + (response.data[i]["intro_title"] || "") + "</td>\
                                <td>" + response.data[i]["intro_content"] + "</td>\
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