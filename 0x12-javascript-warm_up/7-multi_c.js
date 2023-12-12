#!/usr/bin/node
const quant = parseInt(process.argv[2]);
let i = 0;

if (quant) {
  while (i < quant) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
