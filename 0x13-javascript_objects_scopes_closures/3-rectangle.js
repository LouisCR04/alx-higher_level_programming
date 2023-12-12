#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;

      while (j < this.width) {
        process.stdout.write('X');
        j++;
      }

      if (j === this.width) {
        console.log('');
        i++;
      }
    }
  }
};
