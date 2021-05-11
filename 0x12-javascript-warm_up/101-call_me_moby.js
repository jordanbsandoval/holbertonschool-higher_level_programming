#!/usr/bin/node
// Write a function that executes x times a function.
'use strict';
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
