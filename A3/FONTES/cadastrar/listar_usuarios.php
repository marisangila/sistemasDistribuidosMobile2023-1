<?php
    include("conexao.php");

    //comando sql.
    $comando = $pdo->prepare("SELECT pk_usuario, nome_usuario, email_usuario, is_adm_usuario, imagem_usuario FROM usuario;");
    //executa a consulta no banco de dados.
    $comando->execute();

    //Verifica se existe pelo menos um registro na tabela.
    if($comando->rowCount() >= 1)
    {
        //o fetch() transforma o retorno em uma matriz (Use quando você para um registro ou mais, ou seja, uma ou múltiplas linhas da tabela).
        $lista_usuarios = $comando->fetchAll();
    }else{
        echo("Não há usuários cadastrados.");
    }
    unset($comando);
    unset($pdo);
?>