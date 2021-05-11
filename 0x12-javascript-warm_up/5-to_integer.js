#!/usr/bin/node
// Write a script that prints My number: ... if the first argument can be converted to an integer
// If the argument can’t be converted to an integer, print “Not a number”
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
