<?php
    include("conexao.php");

    $codigo = $_GET['codigo'];
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = MD5($_POST["senha"]);
    

    $base64 = '';
    if(!isset($_FILES)){
        $imagem = $_FILES['imagem']; 
        $extensao = $imagem['type'];
        $conteudo = file_get_contents($imagem['tmp_name']);
        $base64 = "data:".$extensao.";base64,".base64_encode($conteudo);
    }

    //comando sql.
    $comando = $pdo->prepare("UPDATE usuario SET nome_usuario = :nome, email_usuario = :email, senha_usuario = :senha, imagem_usuario= :imagem WHERE pk_usuario = :codigo;");

    //insere valores das variaveis no comando sql.
    $comando->bindValue(':codigo',$codigo);
    $comando->bindValue(':nome',$nome);
    $comando->bindValue(':email',$email);
    $comando->bindValue(':senha',$senha);
    $comando->bindValue(':imagem',$base64);

    //executa a consulta no banco de dados.
    $comando->execute();

    //Fecha declaração e conexão.
    unset($comando);
    unset($pdo);

    header("location:informacoes_usuario.php");
?>