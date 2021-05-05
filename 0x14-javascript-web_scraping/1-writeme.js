#!/usr/bin/node
// importando el modulo fs
const fs = require('fs');

// obteniendo el path del archivo
const filePath = process.argv[2];
const write = process.argv[3];

// utilizando el metodo writeFile para escribir en el archivo
fs.writeFile(filePath, write, function (err) {
  if (err) {
    return console.error(err);
  }
});
