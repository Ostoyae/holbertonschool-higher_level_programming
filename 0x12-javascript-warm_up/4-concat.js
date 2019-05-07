#!/usr/bin/node
// This script takes any number of argment and will print a different msg.
const input = process.argv.slice(2);
let msg = `${input[0]} is ${input[1]}`;
console.log(msg);
