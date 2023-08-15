#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let rowString = '';

      for (let col = 0; col < this.width; col++) {
        rowString += 'X';
      }

      console.log(rowString);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width]; // Swap width and height
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
