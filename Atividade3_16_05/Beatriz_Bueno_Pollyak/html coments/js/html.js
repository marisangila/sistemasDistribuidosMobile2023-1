function alertar(){

    alert ('Atividade de Get')
}

var headers = new Headers();

var parametros = { method: 'GET',
               headers: headers,
               mode: 'cors',
               cache: 'default' };


function get_album(id){


    
    fetch('https://jsonplaceholder.typicode.com/comments/'+ id, parametros)
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("ID").innerHTML= data.id
        document.getElementById("nome").innerHTML= data.name
        document.getElementById("corpo").innerHTML= data.body
        document.getElementById("email").innerHTML= data.email
        document.getElementById("post_id").innerHTML= data.postId
        
    } )
}