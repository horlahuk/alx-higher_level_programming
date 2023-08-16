#!/usr/bin/node

const inputArray = process.argv.slice(2);
const sortedArray = inputArray.sort((a, b) => {
  return a - b;
});

const secondToLast = sortedArray[sortedArray.length - 2];
if (isNaN(secondToLast)) {
  console.log(0);
} else {
  console.log(secondToLast);
}
