$(function() {
  $.get('https://swapi-api.hbtn.io/api/people/5/', function(data) {
    $('#character').text(data.name);
  });
});
