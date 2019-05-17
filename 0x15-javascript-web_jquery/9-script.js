let lang = navigator.language.split('-');
//or use the var below
// let lang = $('html').attr("lang");
$.get(`https://fourtonfish.com/hellosalut/?lang=${lang[0]}`, (data, status) => {
$("DIV#hello").text(data.hello);
});
