const apiUrl = "https://api.chucknorris.io/jokes/random";

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const joke = data.value;
    console.log(`Chuck Norris Joke: ${joke}`);
  })
  .catch(error => {
    console.error("Ocorreu um erro ao buscar a piada de Chuck Norris:", error);
  });
