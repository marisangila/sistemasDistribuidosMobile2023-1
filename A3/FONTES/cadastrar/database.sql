-- Criar banco de banco de dados chamado: `php`
--
-- --------------------------------------------------------
--
-- Estrutura da tabela `usuario`
--
CREATE TABLE `usuario` (
  `pk_usuario` int(11) NOT NULL,
  `email_usuario` varchar(100) NOT NULL,
  `senha_usuario` varchar(100) NOT NULL,
  `is_adm_usuario` bit(1) NOT NULL DEFAULT b'0',
  `imagem_usuario` longtext DEFAULT NULL,
  `nome_usuario` varchar(100) NOT NULL
);
--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`pk_usuario`);
--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`