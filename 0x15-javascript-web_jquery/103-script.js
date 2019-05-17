window.onload = function () {
    let field = $("INPUT#language_code");
    let btn = $("INPUT#btn_translate");
    btn.click(() => {
        get_hello(field);
    });
    field.keypress(function (event) {
        let keycode = event.which;
        if (keycode === 13) {
            get_hello(field);
        }
    });
};

function get_hello(field) {
    if (field.val()) {
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${field.val()}`, (data, status) => {
            if (status === "success") {
                $('DIV#hello').text(data.hello);
            }
        });
    }
};


