#!/usr/bin/node
// importando el modulo request
const request = require('request');

// url a get
const url = process.argv[2];

// request
request(url, function (error, response, body){
  if (!error && response.statusCode == 200) {
    const info = JSON.parse(body);
    for i in info.results
    console.log(info.results)
  }
});
