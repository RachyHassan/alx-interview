#!/usr/bin/node

const request = require('request');

// Function to get character names by URLs
const getCharacterNames = (characterUrls, callback) => {
  let characters = [];
  let requestsCompleted = 0;

  characterUrls.forEach(url => {
    request({ url: url, json: true }, (error, response, body) => {
      if (error) {
        callback(error, null);
        return;
      }
      characters.push(body.name);
      requestsCompleted++;
      if (requestsCompleted === characterUrls.length) {
        callback(null, characters);
      }
    });
  });
};

// Main function to get characters from a movie
const getCharactersFromMovie = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request({ url: url, json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Error: Received status code', response.statusCode);
      return;
    }

    const characterUrls = body.characters;
    getCharacterNames(characterUrls, (err, characterNames) => {
      if (err) {
        console.error('Error fetching character names:', err);
        return;
      }
      characterNames.forEach(name => console.log(name));
    });
  });
};

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

getCharactersFromMovie(movieId);