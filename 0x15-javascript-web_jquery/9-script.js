let lang = navigator.language.split('-');
// let lang = $('html').attr("lang");
alert(lang);
$.get(`https://fourtonfish.com/hellosalut/?lang=${lang[0]}`, (data, status) => {
$("DIV#hello").text(data.hello);
});
