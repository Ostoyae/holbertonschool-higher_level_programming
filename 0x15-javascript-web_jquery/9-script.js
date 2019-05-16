let lang = navigator.language.split('-');
$.get(`https://fourtonfish.com/hellosalut/?lang=${lang[0]}`, (data, status) => {
$("DIV#hello").text(data.hello);
})
