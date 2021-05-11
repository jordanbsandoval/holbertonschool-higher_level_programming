#!/usr/bin/node
//Write a script that prints two arguments passed to it, in the following format: " is "
const word = ' is ';
const entrada = process.argv[2];
const entrada2 = process.argv[3];

if (entrada && entrada2) {
  console.log(entrada + word + entrada2);
} else if (entrada) {
  console.log(entrada + word + undefined);
} else {
  console.log(undefined + word + undefined);
}
