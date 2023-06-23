<?php
    include("conexao.php");

    //atribuindo valores dos campos a variaveis.
    $email = $_POST["email"];
    $set_senha = $_POST["senha"];

    //comando sql.
    $comando = $pdo -> prepare("SELECT senha_usuario, FROM usuario; WHERE email_usuario = :email");  
    
    //insere valores das variaveis no comando sql.
    $comando->bindValue(":email",$email);                                                         
    
    //executa a consulta no banco de dados.
    $comando->execute();

    //o fetch() transforma o retorno em um array (use apenas se o retorno for apenas um registro, ou seja, uma única linha da tabela).
    $get_senha = $comando->fetchColumn();    
    
    //Comparar senha informada com a senha armazenado no banco de dados.
    if($get_senha == MD5($set_senha)){
        header("Location:pagina_inicial.html");
    }else{
        echo("Email ou Senha Inválida");
    }

    //Fecha declaração e conexão.
    unset($comando);
    unset($pdo);
?>