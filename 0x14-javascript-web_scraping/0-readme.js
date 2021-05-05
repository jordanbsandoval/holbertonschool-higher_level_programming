#!/usr/bin/node
'use strict';
const fs = require('fs');
const dato = process.argv[2];

fs.readFile(dato, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
