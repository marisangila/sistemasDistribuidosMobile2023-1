<?php
session_start();
// Verifique se o usuário está logado, se não, redirecione-o para uma página de login
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("location: login.html");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina Inicial</title>
</head>
<style>
    body {
        background-color: #76AF50;
    }
</style>
<body>
    <?php
        include("listar_usuario_conectado.php");
        echo "<p>Bem vindo ".$informacoes_usuario['nome_usuario']."!</p>";
    ?>
    <h3>Listar Usuários:</h3>
    <table border="1">
        <thead>
            <tr>
                <th>Foto</th>
                <th>Nome</th>
                <th>Código</th>
                <th>Email</th>
                <th>Nível de Acesso</th>
                <th>Editar</th>
                <th>Excluir</th>
            </tr>
        </thead>
        <tbody>
            <?php
            include("listar_usuarios.php");

            //verifica se a variável tem os valores da tabela.
            if (!empty($lista_usuarios)) {
                //seleciona linha por linha.
                foreach ($lista_usuarios as $linha) { ?>
                    <tr>
                        <td> <?php echo '<img height="40px" width="40px" src="' .$linha['imagem_usuario']. '">'; ?> </td>
                        <td> <?php echo $linha['pk_usuario']; ?></td>
                        <td> <?php echo $linha['nome_usuario']; ?></td>
                        <td> <?php echo $linha['email_usuario']; ?></td>
                        <td> <?php echo $linha['is_adm_usuario']; ?></td>
                        <td> <a href="editar.php?codigo=<?php echo $linha['pk_usuario'];?> ">
                                <input type="button" value="Editar">
                            </a>
                        </td>
                        <td> <a href="excluir_usuario.php?codigo=<?php echo $linha['pk_usuario'];?> ">
                                <input type="button" value="Excluir">
                            </a>
                        </td>
                    </tr>
            <?php }
            }
            ?>
        </tbody>
    </table>
    <br>
    <a href="TELINIC.html">Página Inicial</a>
</body>

</html>