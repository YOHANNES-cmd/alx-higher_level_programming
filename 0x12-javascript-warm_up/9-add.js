#!/usr/bin/node
/**
 * add - computes the sum of 2 numbers.
 * @param {Number} a - The first number.
 * @param {Number} b - the second number.
 *
 * @returns The sum of the two numbers.
 */

function add (a, b) {
	return a + b;
}
console.log(
	add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
);
