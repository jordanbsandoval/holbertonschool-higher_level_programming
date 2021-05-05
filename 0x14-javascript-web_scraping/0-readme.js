#!/usr/bin/node
// importando el modulo fs
const fs = require('fs');

// obteniendo el path del archivo
const dato = process.argv[2];

// Metodo para leer el archivo
fs.readFile(dato, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
