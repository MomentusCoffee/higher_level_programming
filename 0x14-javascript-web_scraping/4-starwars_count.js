#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (error, data, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let result of body['results']) {
      for (let id of result['characters']) {
        if (id.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
