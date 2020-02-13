const url = 'https://swapi.co/api/films/?format=json';
$.getJSON(url, function (data) {
  $.each(data.results, function (key, val) {
    $('UL#list_movies').append('<li>' + val.title + '</li>');
  });
});
