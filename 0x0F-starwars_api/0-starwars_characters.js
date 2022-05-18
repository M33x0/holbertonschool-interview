#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request.get(url, async (err, res, body) => {
  if (err) console.log(err);
  else {
    for (const character of JSON.parse(body).characters) {
      const name = await new Promise((resolve, reject) => {
        request.get(character, (err, res, body) => {
          if (err) reject(err);
          else resolve(JSON.parse(body).name);
        });
      });
      console.log(name);
    }
  }
});
