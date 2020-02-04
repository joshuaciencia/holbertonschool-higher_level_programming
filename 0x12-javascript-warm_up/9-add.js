#!/usr/bin/node
const arg = process.argv;
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(arg[2], arg[3]));
