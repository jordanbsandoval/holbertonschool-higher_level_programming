#!/usr/bin/node
'use strict';
// Write a script that searches the second biggest integer in the list of arguments.
const entrada = process.argv;
const numEntrada = process.argv.length;

if (!(entrada)) {
  console.log(0);
} else if (numEntrada < 4) {
  console.log(0);
} else {
  entrada.sort(function (a, b) {
    return a - b;
  });
  const valEntrada = entrada.slice(numEntrada - 2);
  console.log(valEntrada[0]);
}
