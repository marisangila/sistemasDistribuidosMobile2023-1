function validaFormulario(){

    var nome=document.getElementById("nome");
    var telefone=document.getElementById("telefone");
    var email=document.getElementById("email");
    var motivoContato=document.getElementById("motivoContato");
    var mensagem=document.getElementById("mensagem");

    if(nome.value=="" || nome.value.length <3){
        alert("Preencha o nome corretamente");
        nome.focus();
        return false;
    }


    if(email.value=="" || email.value.indexOf("@")==-1
    || email.value.indexOf(".")==-1){
    alert("Preencha o e-mail corretamente");
    email.focus();
    return false;
    }

    if(telefone.value=="" || telefone.value.length <9){
        alert("Preencha o telefone corretamente");
        telefone.focus();
        return false;
    }

   
    if(motivoContato.value=="0"){
        alert("Selecione um motivo");
        motivoContato.focus();
        return false;
    }

    if(mensagem.value=="" || mensagem.value.length<1){
        alert("Deixe um comentário");
        mensagem.focus();
        return false;
    }
    alert("E-mail enviado com sucesso!");
    return true;
}

function verificaMotivo(motivo){
    
    if(motivo=="4"){
        document.getElementById("divNrPedido").style.display="block";
    }else{
        document.getElementById("divNrPedido").style.display="none";
    }

}