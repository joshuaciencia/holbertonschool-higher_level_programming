#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);
if (!num) {
  console.log(1);
} else {
  let result = num;
  for (let i = num - 1; i > 1; i--) {
    result *= i;
  }
  console.log(result);
}
