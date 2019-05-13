#!/usr/bin/node
// This file defines a method that will count the occurrences
// of a given argument

/**
 *
 * @param list - list of items "Haystack"
 * @param searchElement = element searching for "needle"
 * @returns {number} - number of occurrences of said "needle"
 */
module.exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || searchElement === undefined) {
    return 0;
  }

  return list.filter((x) => x === searchElement).length;
};
