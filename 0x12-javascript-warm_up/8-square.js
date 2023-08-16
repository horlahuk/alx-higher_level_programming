#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  for (let i = 0; i < number; i++) {
    let square = '';
    for (let j = 0; j < number; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
