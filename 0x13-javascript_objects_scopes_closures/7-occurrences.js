#!/usr/bin/node
/**
 * Computes the number of occurrences of an element in a list.
 * @param {Array} list The list of elements.
 * @param {Any} searchElement The element to look for.
 * @returns {Number} The number of occurrences of the given element.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
