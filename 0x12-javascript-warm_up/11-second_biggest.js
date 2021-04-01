#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let max = process.argv.slice(2).sort().map((val) => {
    return (val);
  });

  max.pop();
  max.reverse();
  console.log(max[0]);
}
