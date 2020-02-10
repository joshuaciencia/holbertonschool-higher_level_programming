#!/usr/bin/node
const list = require('./100-data').list;
const new_list = list.map(x => x * list.indexOf(x));
console.log(list);
console.log(new_list);
