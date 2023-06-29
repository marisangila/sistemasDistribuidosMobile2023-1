<?php
        // Configurações do banco de dados
        $host = "localhost";
        $usuario = "root";
        $senha = "";
        $banco = "smtech";

        // Conexão com o banco de dados
        $conexao = mysqli_connect($host, $usuario, $senha, $banco);

        // Verifica se ocorreu um erro na conexão
        if (mysqli_connect_errno()) {
            echo "Falha ao conectar com o banco de dados: " . mysqli_connect_error();
            exit;
        }

        // Consulta para recuperar os dados
        $sql = "SELECT * FROM estoque";
        $resultado = mysqli_query($conexao, $sql);

        // Verifica se ocorreu um erro na consulta
        if (!$resultado) {
            echo "Erro na consulta: " . mysqli_error($conexao);
            exit;
        }

        // Exibe os dados
        while ($linha = mysqli_fetch_assoc($resultado)) {
            echo "<tr>";
            echo "<td>" . $linha['produto'] . "</td>";
            echo "<td>" . $linha['quantidade'] . "</td>";
            echo "<td>" . $linha['lote'] . "</td>";
            echo "<td>" . $linha['validade'] . "</td>";
            echo "</tr>";
        }

        // Fecha a conexão com o banco de dados
        mysqli_close($conexao);
        ?>