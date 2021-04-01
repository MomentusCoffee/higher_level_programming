#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return a + b;
  }
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
