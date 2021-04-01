#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, data, body) => {
  if (error) {
    console.log(error);
  } else if (data.statusCode === 200) {
    fs.writeFile(process.argv[3], body, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
