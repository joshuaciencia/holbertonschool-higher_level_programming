const url = 'https://swapi.co/api/people/5/?format=json';
$.getJSON(url, function (data) {
  $('DIV#character').text(data.name);
});
