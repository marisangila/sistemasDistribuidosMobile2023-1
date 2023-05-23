function alertar(){

    alert ('Atividade de Get')
}

var headers = new Headers();

var parametros = { method: 'GET',
               headers: headers,
               mode: 'cors',
               cache: 'default' };


function get_album(id){


    
    fetch('https://jsonplaceholder.typicode.com/users/'+ id, parametros)
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("ID").innerHTML= data.id
        document.getElementById("nome").innerHTML= data.name
        document.getElementById("usuario").innerHTML= data.username
        document.getElementById("email").innerHTML= data.email
        
    } )
}