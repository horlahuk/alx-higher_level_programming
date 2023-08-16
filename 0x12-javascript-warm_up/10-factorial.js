#!/usr/bin/node

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const inputNumber = Number(process.argv[2]);
const result = factorial(inputNumber);

console.log(result);
