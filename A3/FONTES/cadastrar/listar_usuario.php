<?php
    include("conexao.php");

    $codigo = $_GET['codigo'];

    //comando sql.
    $comando = $pdo->prepare("SELECT nome_usuario, email_usuario, senha_usuario, imagem_usuario FROM usuario WHERE pk_usuario = :codigo");
    
    //insere valores das variaveis no comando sql.
    $comando->bindValue('codigo',$codigo);

    //executa a consulta no banco de dados.
    $comando->execute();

    //Verifica se existe pelo menos um registro na tabela.
    if($comando->rowCount() >= 1)
    {
        //o fetch() transforma o retorno em um vetor (Use para um registro).
        $usuario = $comando->fetch();
    }else{
        echo("Não há usuários cadastrados.");
    }


    //Fecha declaração e conexão.
    unset($comando);
    unset($pdo);