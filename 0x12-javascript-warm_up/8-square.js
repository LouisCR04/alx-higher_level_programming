#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (size) {
  let i = 0;

  while (i < size) {
    let j = 0;

    while (j < size) {
      process.stdout.write('X');
      j++;
    }

    if (j === size) {
      console.log('');
    }

    i++;
  }
} else {
  console.log('Missing size');
}
