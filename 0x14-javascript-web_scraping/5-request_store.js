#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
// importando el metodo request
const request = require('request');
const fs = require('fs');

// get url example
const url = process.argv[2];
const name = process.argv[3];

// utilizar el metodo request. Obtener todo el contenido de una pagina y enviarla a un archivo
request(url, function (error, response, body) {
  request(url).pipe(fs.createWriteStream(name));
});
