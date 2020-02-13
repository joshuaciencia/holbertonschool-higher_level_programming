$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  } else {
    $('HEADER').addClass('red');
    $('HEADER').removeClass('green');
  }
});
