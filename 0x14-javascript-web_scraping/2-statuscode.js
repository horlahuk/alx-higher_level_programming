#!/usr/bin/node

const request = require('request');
const param = process.argv[2];

request(param, (error, response) => {
  if (!error) {
    console.log('code: ', response.statusCode);
  }
});
