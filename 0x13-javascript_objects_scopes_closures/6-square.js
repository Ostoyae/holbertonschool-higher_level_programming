#!/usr/bin/node
// This file defines a Square with is a sub class of Rectangle

const SquareV1 = require('./5-square');

/**
 * Defines a class Square.
 * @type {module.Square}
 */
module.exports = class Square extends SquareV1 {
  /**
   * constructor() method the initialize a Square object
   * @param size the size of square object to make
   */
  constructor (size) {
    if (size === undefined || size <= 0) {
      super(undefined);
      return;
    }
    super(size);
    this.size = size;
  }

  /**
   * charPrint() will print a square based with the give character
   * else 'X' if on is not defined.
   * @param c - character to print with.
   */
  charPrint (c) {
    if (c === undefined || c === '') {
      c = 'X';
    }
    if (this.size > 0) {
      Array(this.size)
        .fill()
        .map(() => console.log(c.repeat(this.size)));
    }
  }
};
