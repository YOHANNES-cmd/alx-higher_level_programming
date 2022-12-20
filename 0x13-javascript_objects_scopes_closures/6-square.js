#!/usr/bin/node
const SquareParent = require('./5-square');

/**
 * Represents a Rectangle with 4 equal sides.
 */
class Square extends SquareParent {
  /**
   * Prints this Square with the given character, otherwise 'X'.
   * @param {String} c The character to print this Square with.
   */
  charPrint (c) {
    const pen = c === undefined ? 'X' : c;
    const row = new Array(this.width).fill(pen, 0, this.width);
    const rows = new Array(this.height).fill(row.join(''), 0, this.height);
    console.log(rows.join('\n'));
  }
}

module.exports = Square;
