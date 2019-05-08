#!/usr/bin/node
// Loop basesd on given arguments
const num = parseInt(process.argv.slice(2));
const shape = 'X';
let y = 0;

if (num) {
  while (y++ < num) {
    console.log(shape.repeat(num));
  }
} else {
  console.log('Missing size');
}
