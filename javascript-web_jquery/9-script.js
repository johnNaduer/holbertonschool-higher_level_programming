$(document).ready(function() {
  $.getJSON("https://stefanbohacek.com/hellosalut/?lang=fr", function(data) {
    var translation = data.hello;
    var div = $("<div></div>").text(translation);
    $("#hello").replaceWith(div);
  });
});

