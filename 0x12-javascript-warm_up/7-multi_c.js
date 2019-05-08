#!/usr/bin/node
// Loop basesd on given arguments
const num = parseInt(process.argv.slice(2));
let i = 0;
if (num) {
  while (i++ < num) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
