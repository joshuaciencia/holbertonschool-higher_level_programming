#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((val, index) => {
  return val * index;
});
console.log(list);
console.log(newList);
