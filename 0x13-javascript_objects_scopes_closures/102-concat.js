#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const fileA = argv[2];
const fileB = argv[3];
const fileC = argv[4];
let content = '';
content += fs.readFileSync(fileA);
content += fs.readFileSync(fileB);
fs.writeFile(fileC, content, function (err) { if (err) throw err; });
