#!/usr/bin/node
const request = require('request');
let completed = {};

request(process.argv[2], { json: true }, (error, data, body) => {
  if (error) {
    console.log(error);
  } else {
    for (let task of body) {
      if (task['completed'] === true) {
        if (completed[task['userId']] === undefined) {
	  completed[task['userId']] = 0;
	}
	completed[task['userId']]++;
      }
    }
    console.log(completed);
  }
});
