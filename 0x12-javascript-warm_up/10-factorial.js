#!/usr/bin/node
// scrip does a factorial on a given int
let num = parseInt(process.argv.slice(2)[0]);
let fact = function (num) {
  if (!num || num === 0) {
    return 1;
  }
  return num * fact(num - 1);
};

let result = fact(num);

console.log(result);
