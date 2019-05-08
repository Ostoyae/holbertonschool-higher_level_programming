#!/usr/bin/node
// find the second biggest
const list = process.argv.slice(2).map(x => parseInt(x));
let max = list[0];
let prev = list[0];

if (list.length < 2) {
  console.log(0);
  process.exit();
}

list.forEach(x => {
  if (x > max) {
    prev = max;
    max = x;
  }
});

console.log(prev);
