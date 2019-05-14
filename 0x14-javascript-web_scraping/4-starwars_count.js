#!/usr/bin/node
// makes a request to a endpoint and log the status code

const request = require('request');
const person = 'https://swapi.co/api/people/18/';
const url = process.argv.slice(2)[0];
let data = [];

if (url) {
  request.get(url)
    .on('data', (chunk) => {
      data.push(chunk);
    })
    .on('end', () => {
      let films = JSON.parse(Buffer.concat(data).toString());
      let count = 0;
      films.results.forEach((mov) => {
        if (mov.characters.includes(person)) { count++; }
      });
      console.log(count);
    });
}
