#!/usr/bin/node
// This script will import a list and modify it using map

let list = require('./100-data');
console.log(list.list);
let l = list.list.map((x, i) => x * i);
console.log(l);
