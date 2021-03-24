#!/usr/bin/node
const n1 = parseInt(process.argv[2]);

function recFactorizar (n) {
  if (!(n)) {
    return (1);
  } else {
    return (n * recFactorizar(n - 1));
  }
}
console.log(recFactorizar(n1));
