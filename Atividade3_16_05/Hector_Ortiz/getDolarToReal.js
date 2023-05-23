fetch("https://economia.awesomeapi.com.br/last/USD-BRL")
  .then(response => response.json())
  .then(data => {

    const usdToBrl = data.USDBRL.high;

    console.log(`A taxa de câmbio atual é: ${usdToBrl}`);
  })
  .catch(error => {
    console.error("Ocorreu um erro ao obter a taxa de câmbio:", error);
  });