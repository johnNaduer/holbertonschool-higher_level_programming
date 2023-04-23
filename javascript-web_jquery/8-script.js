$(document).ready(function() {
  $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    var movies = data.results;
    var list = $("<ul></ul>");
    $.each(movies, function(index, movie) {
      var title = $("<li></li>").text(movie.title);
      list.append(title);
    });
    $("#list_movies").replaceWith(list);
  });
});
