#!/usr/bin/node
const SuperSquare = require('./5-square.js');

module.exports = class Square extends SuperSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
