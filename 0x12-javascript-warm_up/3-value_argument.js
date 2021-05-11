#!/usr/bin/node                                                                                       
// Write a script that prints the first argument passed to it
const entrada = process.argv[2];
if (!entrada) {
  console.log('No argument');
} else if (entrada) {
  console.log(entrada);
}
