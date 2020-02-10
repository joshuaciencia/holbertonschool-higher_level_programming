#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height= h;
    }
  }

  print() {
    for (let h = 0; h < this.height; h++) {
      let row = '';
      for (let w = 0; w < this.width; w++) {
        row += 'X';
      }
      console.log(row);
    }
  }

	rotate() {
		let old_width = this.width;
		this.width = this.height;
		this.height = old_width;
	}

	double() {
		this.width *= 2;
		this. height *= 2;
	}
}

module.exports = Rectangle;
