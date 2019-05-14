#!/usr/bin/node
// This script will save the contents of a get request to a file.

const request = require('request');
const fs = require('fs');
const input = process.argv.slice(2);
let url = input[0];
let dest = input[1];
let data = [];

if (input.length === 2) {
  request.get(url)
    .on('responce', (err, resp) => {
      if (err) {
        console.error(err);
      }
    })
    .on('data', (chunk) => {
      data.push(chunk);
    })
    .on('end', () => {
      let content = Buffer.concat(data).toString();
      fs.writeFile(dest, content, (err) => {
        if (err) {
          if (err.code === 'ENOENT') {
            console.error(err);
            return;
          }
          throw err;
        }
      });
    });
}
