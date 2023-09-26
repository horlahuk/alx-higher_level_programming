#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    fs.writeFile(file, body, { flag: 'w'}, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
