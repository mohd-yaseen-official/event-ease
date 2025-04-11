$(document).on("submit", "form.ajax", function (e) {
    e.preventDefault();
    var $this = $(this);

    document.onkeydown = function (evt) {
        return false;
    };

    var url = $this.attr("action");
    var method = $this.attr("method");

    jQuery.ajax({
        type: method,
        url: url,
        dataType: "json",
        data: new FormData(this),
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            Swal.hideLoading();

            var message = data["message"];
            var status = data["status"];
            var title = data["title"];
            var redirect = data["redirect"];
            var redirect_url = data["redirect_url"];

            if (status == "success") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                function doAfter() {
                    if (redirect == true) {
                        window.location.href = redirect_url;
                    }
                    if (isReload) {
                        window.location.reload();
                    }
                }
                
                Swal.fire({
                    icon: status,
                    title: title,
                    html: message,
                }).then((result) => {
                    console.log(result.isConfirmed);
                    if (result.isConfirmed) {
                        doAfter();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }

                Swal.fire(title, message, "error");
            }
        },
        error: function (data) {
            Swal.hideLoading();

            var title = "An error occurred";
            var message = "An error occurred. Please try again later.";
            Swal.fire(title, message, "error");
        },
    });
});


$(document).on("click", ".action-button", function (e) {
    e.preventDefault();
    $this = $(this);
    var text = $this.attr("data-text");
    var type = "warning";
    var confirmButtonText = "I'm sure";
    var confirmButtonColor = "#DD6B55";
    var url = $this.attr("href");
    var title = $this.attr("data-title");
    if (!title) {
        title = "Are you sure?";
    }

    Swal.fire({
        title: title,
        text: text,
        icon: type,
        showCancelButton: true,
        confirmButtonText: confirmButtonText,
        confirmButtonColor: confirmButtonColor,
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.showLoading();

            jQuery.ajax({
                type: "GET",
                url: url,
                dataType: "json",
                success: function (data) {
                    var message = data["message"];
                    var status = data["status"];
                    var redirect = data["redirect"];
                    var redirect_url = data["redirect_url"];

                    var title = data["title"];

                    Swal.hideLoading();

                    if (status == "success") {
                        if (title) {
                            title = title;
                        } else {
                            title = "Success";
                        }
                        
                        Swal.fire({
                            icon: "success",
                            title: title,
                            text: message,
                            type: "success",
                        }).then((result) => {
                        
                            if (redirect == true) {
                                window.location.href = redirect_url;
                            }
                            if (isReload) {
                                window.location.reload();
                            }
                            
                        });
                        
                    } else {
                        if (title) {
                            title = title;
                        } else {
                            title = "An Error Occurred";
                        }

                        Swal.fire(title, message, "error");
                    }
                },
                error: function (data) {
                    Swal.hideLoading();

                    var title = "An error occurred";
                    var message =
                        "An error occurred. Please try again later.";
                    Swal.fire(title, message, "error");
                },
            });

        }
    });
});


$(document).on('click', '#clear_filter', function () {

    const url = new URL(window.location);

    const page = url.searchParams.get('page');

    url.search = '';

    if (page) {
        url.searchParams.set('page', page);
    }

    window.location.href = url
    
})
