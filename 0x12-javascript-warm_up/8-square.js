#!/usr/bin/node
const arg = process.argv;
const x = parseInt(arg[2]);
if (!x) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
