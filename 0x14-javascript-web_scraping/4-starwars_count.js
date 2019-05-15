#!/usr/bin/node
// makes a request to a endpoint and log the status code

const request = require('request');
const person = 'https://swapi.co/api/people/18/';
const url = process.argv.slice(2)[0];
let data = [];
let status = 200;
if (url) {
  request.get(url)
    .on('error', (err) => {
      console.err(err);
    })
    .on('response', (resp) => { status = resp.statusCode; })
    .on('data', (chunk) => {
      data.push(chunk);
    })
    .on('end', () => {
      if (status !== 200) {
        console.log(0);
        return;
      }
      let films = JSON.parse(Buffer.concat(data).toString());
      let count = 0;
      films.results.forEach((mov) => {
        if (mov.characters.includes(person)) { count++; }
      });
      console.log(count);
    });
} else { console.log(0); }
