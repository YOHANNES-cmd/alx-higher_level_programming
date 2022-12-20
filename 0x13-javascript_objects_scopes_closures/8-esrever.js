#!/usr/bin/node
/**
 * Reverses an array.
 * @param {Array} list The array to reverse.
 * @returns The reversed array.
 */
exports.esrever = function (list) {
  const n = list.length;
  const reversedList = new Array(n);

  list.forEach((item, i) => {
    reversedList[n - i - 1] = item;
  });
  return reversedList;
};
