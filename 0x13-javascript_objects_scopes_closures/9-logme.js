#!/usr/bin/node

let count = 0;
/**
 * logMe() method will keep track of how many times this
 * function is called to print item
 * @param item - value to print
 */
module.exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count += 1;
};
