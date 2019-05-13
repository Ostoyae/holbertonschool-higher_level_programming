#!/usr/bin/node
// This script will import a list and modify it using map

let dict = require('./101-data').dict;

let nd = {};
for (const [k, v] of Object.entries(dict)) {
  if (nd[v] === undefined) {
    nd[v] = [];
    nd[v].push(k);
  } else {
    nd[v].push(k);
  }
}
console.log(nd);
