#!/usr/bin/node
'use strict';
// importando un modulo atraves del metodo required
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    // super: Es usada para llamar funciones del objeto padre
    super(size, size);
  }
};
