let name;
$.get("https://swapi.co/api/people/5/?format=json", function (data, status) {
    $("DIV#character").text(data.name);
})
