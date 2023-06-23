<?php
    include("conexao.php");

    //comando sql.
    $comando = $pdo->prepare("SELECT pk_usuario, nome_usuario, email_usuario,is_adm_usuario, imagem_usuario FROM usuario WHERE pk_usuario=:pk_usuario;");
    
    //insere valores das variaveis no comando sql.
    $comando->bindValue(":pk_usuario", $_SESSION['pk_usuario']);

    //executa a consulta no banco de dados.
    $comando->execute();

    //Verifica se existe pelo menos um registro na tabela.
    if($comando->rowCount() >= 1)
    {
        //o fetch() transforma o retorno em um vetor (Use para um registro).
        $informacoes_usuario = $comando->fetch();
    }else{
        echo("Não há usuários cadastrados.");
    }

    unset($comando);
    unset($pdo);
?>