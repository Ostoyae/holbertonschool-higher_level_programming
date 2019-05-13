#!/usr/bin/node
// This file defines a Square with is a sub class of Rectangle

const Rectangle = require('./4-rectangle');

/**
 * Defines a class Square.
 * @type {module.Square}
 */
module.exports = class Square extends Rectangle {
  /**
   * constructor() method the initialize a Square object
   * @param size the size of square object to make
   */
  constructor (size) {
    if (size === undefined || size <= 0) {
      super(undefined);
      return;
    }
    super(size, size);
  }
};
