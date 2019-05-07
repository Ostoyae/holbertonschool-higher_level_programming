#!/usr/bin/node
// This script takes any number of argment and will print a different msg.
const input = process.argv.slice(2);
let c = 0;

input.forEach((val, index) => {
  console.log(`${val}`);
  c++;
});

if (c === 0) {
  console.log('No Argument');
}
