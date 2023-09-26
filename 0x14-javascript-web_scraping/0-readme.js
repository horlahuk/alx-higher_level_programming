#!/usr/bin/node

const fs = require('fs');

filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
	if (error) {
		console.error(error);
		return;
	}
	else {
		console.log(data);
	}
})
