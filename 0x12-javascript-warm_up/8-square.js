#!/usr/bin/node
// Script that print an square
const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('x'.repeat(num));
  }
}
