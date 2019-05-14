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
        if (!users[id] && u.completed === true) { users[id] = 1; }
        if (u.completed === true) { users[id] += 1; }
      });
      // Object.entries(users)
      //   .map((ele) => { if (ele[1] === 0) { delete users[ele[0]]; } });
      console.log(users);
    });
}
