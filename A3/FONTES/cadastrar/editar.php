<?php
include("listar_usuario.php");

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
    <title>Conexão Banco de Dados</title>
</head>
<style>
    body{
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
    <!--O action determina para onde será enviado os dados do formulário.-->
    <form action="editar_usuario.php?codigo=<?php echo $_GET['codigo'];?>" method="POST" enctype="multipart/form-data">
        <label>Nome:</label>
        <br>
        <input type="text" name="nome" value="<?php echo $usuario['nome_usuario']?>">
        <br>
        <label>Email:</label>
        <br>
        <input type="text" name="email" value="<?php echo $usuario['email_usuario']?>">
        <br>
        <label>Senha:</label>
        <br>
        <input type="password" name="senha">
        <br>
        <input type="file" name="imagem" multiple accept="image/*"> 
        <br>
        <!--Necessário um input do tipo submit.-->
        <input type="submit" value="Atualizar" name="submit">
    </form>
    <br>
    <a href="informacoes_usuario.php">Voltar</a>
</body>
</html>