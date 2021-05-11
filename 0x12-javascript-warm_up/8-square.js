#!/usr/bin/node
// write an script that print a square
const entrada = process.argv[2];
if (!entrada) {
  console.log('Missing size');
} else if (isNaN(entrada)) {
  console.log('Missing size');
} else if (entrada > 0) {
  for (let i = 0; i < entrada; i++) {
    console.log('x'.repeat(entrada));
  }
}
