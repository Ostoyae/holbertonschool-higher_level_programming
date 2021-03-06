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
};
