#!/usr/bin/node

const request = require('request');

// Base URL for the SWAPI API
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/';

// Function to fetch movie details by movie ID
function fetchMovieCharacters (movieId) {
  const url = `${BASE_URL}${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to retrieve movie data. Status code:', response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          console.error('Failed to retrieve character data. Status code:', charResponse.statusCode);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if a movie ID was provided
if (!movieId) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

// Fetch and display the movie characters
fetchMovieCharacters(movieId);
