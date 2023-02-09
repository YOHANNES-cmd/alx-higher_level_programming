#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length > 3) {
  request
    .get(`${process.argv[2]}`)
    .pipe(fs.createWriteStream(process.argv[3]));
}
