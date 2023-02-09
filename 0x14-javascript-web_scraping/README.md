vaScript - Web scraping

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

This project contains some tasks for learning how to perform web scraping with **JavaScript**.

## Tasks To Complete

+ [x] 0. Readme<br/>_**[0-readme.js](0-readme.js)**_ contains a script that reads and prints the content of a file.
  + Requirements:
    + The first argument is the file path.
    + The content of the file must be read in `utf-8`.
    + If an error occurred during the reading, print the error object.

+ [x] 1. Write me<br/>_**[1-writeme.js](1-writeme.js)**_ contains a script that writes a string to a file.
  + Requirements:
    + The first argument is the file path.
    + The second argument is the string to write.
    + The content of the file must be written in `utf-8`.
    + If an error occurred during while writing, print the error object.

+ [x] 2. Status code<br/>_**[2-statuscode.js](2-statuscode.js)**_ contains a script that displays the status code of a `GET` request.
  + Requirements:
    + The first argument is the URL to request (`GET`).
    + The status code must be printed like this: `code: <status code>`.
    + You must use the module `request`.

+ [x] 3. Star wars movie title<br/>_**[3-starwars_title.js](3-starwars_title.js)**_ contains a script that prints the title of a Star Wars movie where the episode number matches a given integer.
  + Requirements:
    + The first argument is the movie ID.
    + You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`.
    + You must use the module `request`.

+ [x] 4. Star wars Wedge Antilles<br/>_**[4-starwars_count.js](4-starwars_count.js)**_ contains a script that prints the number of movies where the character "Wedge Antilles" is present.
  + Requirements:
    + The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`.
    + Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API.
    + You must use the module `request`.

+ [x] 5. Loripsum<br/>_**[5-request_store.js](5-request_store.js)**_ contains a script that gets the contents of a webpage and stores it in a file.
  + Requirements:
    + The first argument is the URL to request.
    + The second argument the file path to store the body response.
    + The file must be UTF-8 encoded.
    + You must use the module `request`.

+ [x] 6. How many completed?<br/>_**[6-completed_tasks.js](6-completed_tasks.js)**_ contains a script that computes the number of tasks completed by user id.
  + Requirements:
    + The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`.
    + Only print users with completed task.
    + You must use the module `request`.

+ [x] 7. Who was playing in this movie?<br/>_**[100-starwars_characters.js](100-starwars_characters.js)**_ contains a script that prints all characters of a Star Wars movie.
  + Requirements:
    + The first argument is the Movie ID - example: `3` = "Return of the Jedi".
    + Display one character name by line.
    + You must use the [Star wars API](https://swapi-api.hbtn.io/).
    + You must use the module `request`.

+ [x] 8. Right order<br/>_**[101-starwars_characters.js](101-starwars_characters.js)**_ contains a script that prints all characters of a Star Wars movie.
  + Requirements:
    + The first argument is the Movie ID - example: `3` = "Return of the Jedi".
    + Display one character name by line **in the same order of the list "characters" in the /`films/` response**.
    + You must use the [Star wars API](https://swapi-api.hbtn.io/).
    + You must use the module `request`.
