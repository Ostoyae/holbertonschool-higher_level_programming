$.get("https://swapi.co/api/films/?format=json", function (data, status) {
    data.results.forEach((mov) =>{
        $("UL#list_movies").append(`<li>${mov.title}</li>`)
    })
})

