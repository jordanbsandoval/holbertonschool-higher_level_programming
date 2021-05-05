#!/usr/bin/node
// script that display the status code of a GET request.
// importando el modulo request
const request = require('request');

// Url a get
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log('Code:', response.statusCode);
  }
});
