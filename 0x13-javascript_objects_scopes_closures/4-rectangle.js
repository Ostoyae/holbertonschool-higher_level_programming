#!/usr/bin/node
// THis file defines a rectangle

/**
 * Define a class Rectangle
 * @type {module.Rectangle}
 */
module.exports = class Rectangle {
  /**
   * constructor() - method in which to create a Rectangle object
   * @param w
   * @param h
   */
  constructor (w, h) {
    if ((w === undefined || h === undefined) || (w <= 0 || h <= 0)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  /**
   * print() method will print a rectangle based off current height and width
   */
  print () {
    Array(this.height).fill().map(
      () => console.log('X'.repeat(this.width))
    );
  }

  /**
   * double() method will double the height and width
   */
  double () {
    this.height *= 2;
    this.width *= 2;
  }

  /**
   * rotate() method rotates the rectangle 90 degrease (swap width & height)
   */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};
