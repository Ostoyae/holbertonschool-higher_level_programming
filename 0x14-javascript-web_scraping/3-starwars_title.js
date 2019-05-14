#!/usr/bin/node
// makes a request to a endpoint and log the status code

const request = require('request');
const id = process.argv.slice(2)[0];
const url = 'http://swapi.co/api/films/' + id;
if (id) {
  let options = {
    url: url,
    gzip: true,
    encoding: 'utf8'
  };
  request.get(options)
    .on('data', (data) => {
      console.log(JSON.parse(data).title);
    });
}
