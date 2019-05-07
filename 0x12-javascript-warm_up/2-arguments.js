#!/usr/bin/node
// This script takes any number of argment and will print a different msg.

const input = process.argv.slice(2).length;

if (input === 0) {
  console.log('No argument');
} else if (input === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
