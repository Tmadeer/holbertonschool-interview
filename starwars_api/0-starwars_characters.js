#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function getJSON (uri) {
  return new Promise((resolve, reject) => {
    request(uri, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}

async function main () {
  const film = await getJSON(filmUrl);
  for (const characterUrl of film.characters) {
    const character = await getJSON(characterUrl);
    console.log(character.name);
  }
}

main().catch(console.error);
