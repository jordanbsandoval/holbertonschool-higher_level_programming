#!/usr/bin/node
// Importando el modulo request
const request = require('request');

// obteniedo la entrada
const id = process.argv[2];

// url a trabajar
const url = 'https://swapi-api.hbtn.io/api/films/';

// url + id
const url_id = url + id;

request(url_id, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info);
  }
});
