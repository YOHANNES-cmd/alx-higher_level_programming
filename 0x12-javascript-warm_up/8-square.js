#!/usr/bin/node

/**
 * square - prints a square with 'X'.
 * @param {Nunmber} size - the of the square.
 */
function square (size) {
	if (Number.isNaN(size)) {
		console.log('Missing size');
	} else if (size >= 0){
		const row = new Array(size);
		for (let i = 0; i < size; i++){
			row.push('X');
		}
		let rows = new Array(size);
		rows = rows.fill(row.join(''), 0, size);
		console.log(rows.join('\n'));
	}
}

square(Number.parseInt(process.argv[2]));
