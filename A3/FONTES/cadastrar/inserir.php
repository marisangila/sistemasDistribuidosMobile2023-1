<?php
    include("conexao.php");

        
    //atribuindo valores dos campos a variaveis.
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $imagem = $_FILES['imagem']; 
    $extensao = $imagem['type'];
    $conteudo = file_get_contents($imagem['tmp_name']);
    $base64 = "data:".$extensao.";base64,".base64_encode($conteudo);

    //converte a senha para hash MD5, para que não seja armazenada em texto limpo no banco de dados.
    $senha = MD5($_POST["senha"]);

    //comando SQL.
    $comando = $pdo -> prepare("INSERT INTO usuario(nome_usuario,email_usuario,senha_usuario,imagem_usuario) VALUES(:nome,:email,:senha,:conteudo)");  
    
    //insere valores das variaveis no comando sql.
    $comando->bindValue(":nome",$nome);    
    $comando->bindValue(":email",$email);                                  
    $comando->bindValue(":senha",$senha);                                  
    $comando->bindValue(":conteudo", $base64);

    //executa o comando SQL, ou seja, insere os dados no banco de dados.
    $comando->execute();

    //redireciona para a pagina informada.
    header("Location:cadastrar.php");

    //Fecha declaração e conexão.
    unset($comando);
    unset($pdo);
?>