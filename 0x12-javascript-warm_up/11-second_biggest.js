#!/usr/bin/node
'use strict';
// Write a script that searches the second biggest integer in the list of arguments.
const entrada = process.argv;
const num_entrada = process.argv.length;

if (!(entrada)) {
  console.log(0);
} else if (num_entrada < 4) {
    console.log(0);
} else {
    entrada.sort(function (a, b) {return a - b;});
    const val_entrada = entrada.slice(num_entrada - 2);
    console.log(val_entrada[0]);
}

