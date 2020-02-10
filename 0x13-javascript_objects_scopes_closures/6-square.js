#!/usr/bin/node
const Square1 = require('./5-square')
class Square extends Square1 {
  constructor(size) {
    super(size);
  }

	charPrint(c) {
		let ch = c;
		if (c == undefined) {
			ch = 'X';
		}
		for (let r = 0; r < this.width; r++) {
			let s = '';
			for (let c = 0; c < this.width; c++) {
				s += ch;
			}
			console.log(s);
		}
	}
}

module.exports = Square;
