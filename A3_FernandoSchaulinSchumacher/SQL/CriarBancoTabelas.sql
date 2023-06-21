-- Criar o banco de dados "biblioteca".
CREATE DATABASE biblioteca;
GO
-- Agora, vamos entrar no mundo da biblioteca!
USE biblioteca;
GO
-- Vamos criar a tabela "usuarios".
CREATE TABLE usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
GO
-- Vamos criar a tabela "livros".
CREATE TABLE livros (
    id INT IDENTITY(1,1) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    escritor VARCHAR(100) NOT NULL,
    publicadora VARCHAR(100) NOT NULL,
    localizacao VARCHAR(50) NOT NULL
);