function preencherEndereco(json) {
    //Preenchendo os campos de texto com o JSON retornad pelo webservice.
    document.querySelector('input[id=rua]').value = json.logradouro;
    document.querySelector('input[id=bairro]').value = json.bairro;
    document.querySelector('input[id=cidade]').value = json.localidade;
    document.querySelector('input[id=estado]').value = json.uf;
}
function charmarWebService(){
    //Chamando o webwervice e recebendo a resposta.
    fetch(url)
        .then(response => response.json())
        .then(json => {
            if (json.logradouro) {
                //Chamando a função que preenche os campos de texto com os valores retornados.
                preencherEndereco(json)
            }else{
                alert("Parece que este CEP não existe!")
            }
        });
}