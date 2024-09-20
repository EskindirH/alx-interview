#!/usr/bin/node

const axios = require('axios');

// Base URL for the SWAPI API
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/';

// Function to fetch movie details by movie ID
async function fetchMovieCharacters (movieId) {
  try {
    // Fetch the movie data based on movie ID
    const movieResponse = await axios.get(`${BASE_URL}${movieId}/`);
    const movieData = movieResponse.data;

    // Retrieve the list of character URLs from the movie data
    const characterUrls = movieData.characters;

    // For each character URL, fetch and print the character name
    for (const characterUrl of characterUrls) {
      const characterResponse = await axios.get(characterUrl);
      const characterData = characterResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching movie characters:', error.message);
  }
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Check if a movie ID was provided
if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

// Fetch and display the movie characters
fetchMovieCharacters(movieId);
