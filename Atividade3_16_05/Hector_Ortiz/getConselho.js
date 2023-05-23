fetch('https://api.adviceslip.com/advice')
  .then(response => response.json())
  .then(data => {
    console.log('Conselho:', data.slip.advice);
  })
  .catch(error => {
    console.log('Ocorreu um erro:', error);
  });
