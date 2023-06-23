<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conexão Banco de Dados</title>
</head>
<style>
        
      body {
        font-family: Arial, sans-serif;
        background-color: #49705d;
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
      h1 {
        text-align: center;
        color: #333;
      }
      
      label {
        display: block;
        margin-bottom: 8px;
        color: #333;
      }
      
      input[type="text"],
      input[type="password"] {
        display: block;
        width: 100%;
        padding: 8px;
        margin-bottom: 20px;
        border-radius: 4px;
        border: none;
        background-color: #f1f1f1;
      }
      input[type="submit"] {
        background-color: #4CAF50;
        color: #fff;
        border: none;
        padding: 10px;
        border-radius: 4px;
        cursor: pointer;
      }
      
      input[type="submit"]:hover {
        background-color: #3e8e41;
      }
</style>
<body>
    <!--O action determina para onde será enviado os dados do formulário.-->
    <form action="inserir.php" method="POST" enctype="multipart/form-data">
        <label>Nome:</label>
        <br>
        <input type="text" name="nome">
        <br>
        <label>Email:</label>
        <br>
        <input type="text" name="email">
        <br>
        <label>Senha:</label>
        <br>
        <input type="password" name="senha">
        <br>
        <input type="file" name="imagem" multiple accept="image/*"> 
        <br>
        <!--Necessário um input do tipo submit.-->
        <input type="submit" value="Cadastrar-se" name="submit">
    </form>
    <br>
    <a href="login.html">Entrar</a>
</body>
</html>