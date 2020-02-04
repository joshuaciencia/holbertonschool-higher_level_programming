#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);

function factorial (val, i) {
  if (i <= 1) {
    return (val);
  }
  return (factorial(val * i, i - 1));
}

if (!num) {
  console.log(1);
} else {
  console.log(factorial(num, num - 1));
}
