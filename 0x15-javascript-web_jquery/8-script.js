$.getJSON('https://swapi.co/api/films?format=json', function (data) {
  let items = [];
  $.each(data.results, function (key, value) {
    items.push('<li id=' + key + '>' + value['title'] + '</li>');
  });

  $('<ul/>', {
    'class': 'list_movies',
    html: items.join('')
  }).appendTo('body');
});
