#!/usr/bin/node
// scrip does a factorial on a given int
let num = parseInt(process.argv.slice(2)[0]);
let fact = num;
if (!num) {
  fact = 1;
}

while (num > 1) {
  fact *= --num;
}

console.log(fact);
