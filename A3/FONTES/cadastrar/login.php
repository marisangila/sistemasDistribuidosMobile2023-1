<?php
    include("conexao.php");

    //atribuindo valores dos campos a variaveis.
    $email = $_POST["email"];
    $set_senha = $_POST["senha"];

    //comando sql.
    $comando = $pdo->prepare("SELECT pk_usuario, senha_usuario, is_adm_usuario FROM usuario WHERE email_usuario = :email");

    //insere valores das variaveis no comando sql.
    $comando->bindValue(":email", $email);

    //executa a consulta no banco de dados.
    $comando->execute();

    //Se a consulta retornar uma única linha significa que o email inserido existe.
    if ($comando->rowCount() == 1) {
        //o fetch() transforma o retorno em um array (use apenas se o retorno for apenas um registro, ou seja, uma única linha da tabela).
        $resultado = $comando->fetch();

        //Comparar senha informada com a senha armazenado no banco de dados.
        if ($resultado['senha_usuario'] == MD5($set_senha)) {
            //inicia uma sessão.
            session_start();

            //insere informações na sessão.
            $_SESSION['pk_usuario'] = $resultado['pk_usuario'];
            $_SESSION['senha_usuario'] = $resultado['senha_usuario'];
            $_SESSION['is_adm_usuario'] = $resultado['is_adm_usuario'];
            $_SESSION['loggedin'] = true;

            //redireciona para a pagina informada.
            header("Location:TELINIC.html");
        } else {
            echo ("Email ou Senha Inválida!");
        }
    } else {
        echo ("Email ou Senha Inválida!");
    }
    //Fecha declaração e conexão.
    unset($comando);
    unset($pdo);
?>