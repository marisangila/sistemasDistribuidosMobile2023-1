<?php

include('connect.php');

$uname = $_POST["username"];
$pass = $_POST["password"];


$result = mysqli_query($conn, "SELECT password FROM smtech WHERE username='$uname'");

if ($row = mysqli_fetch_array($result)) {
    $password = $row['password'];

if ( $password == $pass ) {

        echo '<script type="text/javascript">'; 
        echo 'alert("Logado com SUCESSO!");';
        echo 'window.location.href = "estoque.html";';
        echo '</script>';
        
        }
        else 
            { 
                echo '<script type="text/javascript">'; 
                echo 'alert("Senha incorreta!");';
                echo 'window.location.href = "login.html";';
                echo '</script>';  
            }
    
}
else {
    echo '<script type="text/javascript">'; 
    echo 'alert("Nome incorreto!");';
    echo 'window.location.href = "login.html";';
    echo '</script>';
}



mysqli_close($conn);
    


?>




}
    else 