#!/usr/bin/node
const value = process.argv;
if (value.length <= 3) {
  console.log('0');
} else {
  value.sort(function (a, b) {
    return a - b;
  });
  const valArr = value.slice(value.length - 2);
  console.log(valArr[0]);
}
