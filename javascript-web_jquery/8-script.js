$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
  for (const result of data.results) {
    const liItem = $("<li></li>").text(result.title);
    $("#list_movies").append(liItem);
  }
})
