#!/usr/bin/node
// Script that print an square
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
}
