$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').replaceWith(data.name);
});
