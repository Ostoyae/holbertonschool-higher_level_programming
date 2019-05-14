#!/usr/bin/node
// This script will save the contents of a get request to a file.

const request = require('request');
const input = process.argv.slice(2);
let url = input[0];
let data = [];
let users = {};
if (input.length >= 1) {
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
      let content = JSON.parse(Buffer.concat(data).toString());
      content.forEach((u) => {
        let id = u.userId.toString();
        if (!users[id]) { users[id] = 0; }
        if (u.completed === true) { users[id] += 1; }
      });
      console.log(users);
    });
}
