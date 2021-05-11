#!/usr/bin/node
// Programa que escribe un mensaje deacuerdo al numero de parametros pasados
const numberParametros = process.argv.length;
if (numberParametros === 2) {
  console.log('No argument');
} else if (numberParametros === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
