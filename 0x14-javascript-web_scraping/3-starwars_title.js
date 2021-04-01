#!/usr/bin/node
const request = require('request');

request(('http://swapi.co/api/films/' + process.argv[2]), { json: true }, (error, data, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body['title']);
  }
});
