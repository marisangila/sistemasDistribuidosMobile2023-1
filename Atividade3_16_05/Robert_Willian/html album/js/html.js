function alertar(){

    alert ('Atividade de Get')
}

var headers = new Headers();

var parametros = { method: 'GET',
               headers: headers,
               mode: 'cors',
               cache: 'default' };


function get_album(id){


    
    fetch('https://jsonplaceholder.typicode.com/albums/'+ id, parametros)
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("ID").innerHTML= data.id
        document.getElementById("titulo").innerHTML= data.title
        document.getElementById("usuario").innerHTML= data.userId
        
    } )
}