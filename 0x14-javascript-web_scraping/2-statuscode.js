#!/usr/bin/node
// makes a request to a endpoint and log the status code

const request = require('request');
const url = process.argv.slice(2)[0]
request(url, (err, res, body) => {
	err ? console.error(err) : console.log('code: %d', res.statusCode);
});
