#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

request(url, (error, response, body) => {
  if (!error) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
