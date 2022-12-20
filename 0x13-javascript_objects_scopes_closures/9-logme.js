#!/usr/bin/node
let num = 0;
/**
 * Logs a message to the console.
 * @param {String} item The message to be logged.
 */
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
