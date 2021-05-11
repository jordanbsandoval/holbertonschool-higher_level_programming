#!/usr/bin/node
// Write a function that increments and calls a function.
'use strict';
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
