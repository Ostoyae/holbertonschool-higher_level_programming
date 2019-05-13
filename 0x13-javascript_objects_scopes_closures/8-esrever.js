#!/usr/bin/node
// This file define a function that will reverse a list
// without using the built in method.

/**
 * esrever() - method that reverse the order of a list.
 * @param list - a list
 * @returns revered list
 */
module.exports.esrever = function (list) {
  if (list === undefined || list.length <= 1) {
    return list;
  }
  let i = 0;
  return list.map(() => list[(list.length - 1) - i++]);
};
