#!/usr/bin/node
// 3-starwars_title.js

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
