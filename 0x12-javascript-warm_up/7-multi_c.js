#!/usr/bin/node
const number = process.argv[2];
if (number === undefined) {
  console.log('Missing number of ocurrences');
} else if (number > 0) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
