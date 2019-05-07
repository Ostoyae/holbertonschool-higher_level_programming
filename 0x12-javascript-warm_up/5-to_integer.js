#!/usr/bin/node
// This script check if a given argument is a number
const input = process.argv.slice(2);

let num = parseInt(input[0]);

if (!num) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
