#!/usr/bin/node
'use strict';
// Write a script that computes and prints a factorial
const entrada = parseInt(process.argv[2]);

function factorial (x) {
  if (!(x)) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(entrada));
