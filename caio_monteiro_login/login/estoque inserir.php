<?php
{
include('connect.php');


$produto = $_POST["produto"];
$quantidade = $_POST["quantidade"];
$validade = $_POST["produto"];
$lote = $_POST["lote"];

// posting data to server

$sql1 = ("SELECT * FROM estoque");
$result = mysqli_query($conn, $sql1);

while ($row = mysqli_fetch_array($result)) {

    $noname = $row['produto'] ;
}

if ($noname == $produto )
{
    {
        echo '<script type="text/javascript">'; 
        echo 'alert("Produto existente");';
        echo 'window.location.href = "./estoque-inserir.html";';
        echo '</script>';
    }
}
else {

    $sql2 = "INSERT INTO estoque VALUES ('$produto','$quantidade', '$validade','$lote')";

if (mysqli_query($conn, $sql2)) {
    echo '<script type="text/javascript">'; 
    echo 'alert("Registrado!");';
    echo 'window.location.href = "./estoque-inserir.html";';
    echo '</script>';
}
else {
    echo "ERROR: Hush! Sorry $sql2. "
        . mysqli_error($conn);
}
}
       
// Close connection

 mysqli_close($conn);
}

?>
