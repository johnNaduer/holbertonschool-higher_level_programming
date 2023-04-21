// Wait for the document to be fully loaded before running the script
$(document).ready(function() {

  // Select the DIV#toggle_header element and attach a click event handler to it
  $('div#toggle_header').click(function() {

    // Select the <header> element and get its current class
    var header = $('header');
    var currentClass = header.attr('class');

    // Update the class of the <header> element depending on the current class
    if (currentClass === 'red') {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }

  });

});
/*

$(function() {
  $('#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});

*/
