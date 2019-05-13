#!/usr/bin/node
// defines a function that will convert a number to a selected base value

/**
 *  converter() - method that constructs a function that will return the base
 *  value.
 * @param base
 * @returns {function(*): string}
 */
module.exports.converter = function (base) {
  return function (value) {
    return value.toString(base);
  };
};
