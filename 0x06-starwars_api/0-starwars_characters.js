#!/usr/bin/node

const request = require("request");

const filmId = process.argv[2];
const endPoint = "https://swapi-api.hbtn.io/api/films/" + filmId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise((resolve) =>
    request(endPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error(
          "Error: ",
          err,
          "| StatusCode: ",
          res ? res.statusCode : "N/A"
        );
        resolve();
      } else {
        const data = JSON.parse(body);
        people = data.characters;
        resolve();
      }
    })
  );
};

const requestNames = async () => {
  for (const p of people) {
    await new Promise((resolve) =>
      request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error(
            "Error: ",
            err,
            "| StatusCode: ",
            res ? res.statusCode : "N/A"
          );
        } else {
          const data = JSON.parse(body);
          names.push(data.name);
        }
        resolve();
      })
    );
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of names) {
    console.log(n);
  }
};

getCharNames();
