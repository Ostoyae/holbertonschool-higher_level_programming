window.onload = function () {
    let lang = 'en';
    let field = $("INPUT#language_code");
    let btn = $("INPUT#btn_translate");
    btn.click(function () {
        if (field.val()) {
            $.get(`https://www.fourtonfish.com/hellosalut/?lang=${field.val()}`, (data, status) => {
                if (status === "success") {
                    $('DIV#hello').text(data.hello);
                }
            });
        }
    });
};