#!/usr/bin/node
const arg = process.argv;
if (arg.length < 4) {
  console.log('0');
} else {
  const nums = [];
  for (let i = 2; i < arg.length; i++) {
    nums.push(parseInt(arg[i]));
  }
  const largest = Math.max(...nums);
  nums.splice(nums.indexOf(largest), 1);
  console.log(Math.max(...nums));
}
