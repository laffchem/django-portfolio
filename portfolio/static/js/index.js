'use strict';
const jokeSpace = document.getElementById('dad-joke');
const button = document.getElementById('dad-img');

async function getJoke() {
  const response = await fetch('https://icanhazdadjoke.com', {
    method: 'GET',
    headers: { Accept: 'application/json' },
  });
  const data = await response.json();
  console.log(data.joke);
  jokeSpace.innerText = data.joke;
}

button.addEventListener('click', getJoke);
