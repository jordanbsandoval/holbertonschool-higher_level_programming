#!/usr/bin/node
'use strict';
let fs = require("fs");
let dato = process.argv[2];

fs.readFile(dato, 'utf8', function (err, data){
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
