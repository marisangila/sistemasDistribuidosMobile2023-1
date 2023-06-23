<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="../css/geral.css">
    <link rel="stylesheet" href="../css/geralForm.css">
    <link rel="icon" href="../img/icone.png">
    <title>Fale Conosco - Natural Flavour</title>
</head>
<style>
     body {
          font-family: Arial, sans-serif;
          background-color: #76AF50;
        }

        form {
          background-color: #fff;
          margin: 0 auto;
          padding: 20px;
          width: 400px;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          
        }
</style>

<body>
 
<script>
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
</script>
    <header id="cabecalho">
        <section id="navegacao">
            <div id="inicio" class="linksDiv">
                <a href="TELINIC.html">Início</a>
            </div>
            <div id="faleConosco" class="linksDiv">
                <a class="links" href="#">Fale Conosco</a>
            </div>

            <div id="Alterar Usuário" class="linksDiv">
                <a class="links" href="informacoes_usuario.php">Editar Usuário</a>      
            </section>

    </header>
    <section id="conteudoPrincipal">
    <form action="#" method="POST">
        <fieldset id="formulario">
            <p id="tituloPrincipal">Preencha as Informações</p><br>
                <div class="campos"> 
                    <input type="text" id="nome" name="nome" placeholder="Nome" class="camposForm">
                </div><br>
                <div class="campos">
                    <input type="email" id="email" name="email" placeholder="E-mail" class="camposForm"><br>
                </div><br>
                <div class="campos">
                    <input type="number" id="telefone" name="telefone" placeholder="Telefone" class="camposForm"><br>
                </div><br>
                <div class="campos">
                    <select id="motivoContato">
                        <option value="0">Motivo de Contato</option>
                        <option value="1">Dúvida</option>
                        <option value="2">Sugestão</option>
                        <option value="3">Reclamação</option>
                    </select><br>
                </div><br>
                <div class="campos">
                    <textarea name="mensagem" id="mensagem" placeholder="Mensagem" class="camposForm"></textarea><br>
                </div><br>
                <div class="campos" id="botoes">
                    <button class="botoes" id="vermelho" type="reset">CANCELAR</button>
                    <button class="botoes" id="verde" type="submit" onclick="return validaFormulario()">ENVIAR</button>
        </fieldset>
    </form> 
</section>   
</body>
</html>