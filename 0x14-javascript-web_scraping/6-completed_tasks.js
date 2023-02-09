#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    const aggregate = {};

    if (err) {
      console.log(err);
    }
    JSON.parse(body).forEach(element => {
      if (element.completed) {
        if (!aggregate[element.userId]) {
          aggregate[element.userId] = 0;
        }
        aggregate[element.userId]++;
      }
    });
    console.log(aggregate);
  });
}
