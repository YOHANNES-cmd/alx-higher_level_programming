#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${BASE_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;

    charactersURL.forEach(element => {
      request(element, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
}
