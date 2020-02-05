#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);

function factorial (val) {
  if (!val || val <= 1) {
    return 1;
  }
  return val * factorial(val - 1);
}
console.log(factorial(num, num - 1));

