const request = require("request");

function getMovieCharacters(movieId) {
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(baseUrl, (error, response, body) => {
    if (error) {
      console.error(`Error fetching movie data: ${error}`);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error fetching character data: ${error}`);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error("Usage: node star_wars_characters.js <movie_id>");
  process.exit(1);
}

getMovieCharacters(movieId);
