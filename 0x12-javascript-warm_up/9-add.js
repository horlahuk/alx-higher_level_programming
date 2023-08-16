#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (!isNaN(a) && !isNaN(b)) {
  function add (a, b) {
    const result = a + b;
    console.log(result);
  }

  add(a, b);
} else {
  console.log('NaN');
}
