#!/usr/bin/node
const descriptor = process.argv.length;
if (descriptor === 2) {
  console.log('No argument');
} else if (descriptor === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
