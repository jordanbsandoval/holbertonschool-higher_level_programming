#!/usr/bin/node
// Write a script that prints x times "C is fun"
const entrada = process.argv[2];
if (!entrada) {
  console.log('Missing number of occurrences');
} else if (entrada > 0) {
  for (let i = 0; i < entrada; i++) {
    console.log('C is fun');
  }
}
