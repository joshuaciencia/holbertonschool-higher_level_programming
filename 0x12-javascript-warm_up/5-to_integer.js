#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
