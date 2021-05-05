#!/usr/bin/node
// importando el modulo fs
const fs = require('fs');

// obteniendo el path del archivo
const file_path = process.argv[2];
const write = process.argv[3];

// utilizando el metodo writeFile para escribir en el archivo
fs.writeFile(file_path, write, function (err) {
  if (err) {
    return console.error(err);
  }
});
