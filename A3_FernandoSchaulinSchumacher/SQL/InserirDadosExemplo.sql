-- Vamos adicionar alguns livros
USE biblioteca;
GO
INSERT INTO livros (titulo, escritor, publicadora, localizacao)
VALUES
    ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Editora Seguinte', 'A-001'),
    ('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Editora Rocco', 'B-002'),
    ('As Crônicas de Nárnia', 'C.S. Lewis', 'Editora Martins Fontes', 'C-003'),
    ('A Menina que Roubava Livros', 'Markus Zusak', 'Editora Intrínseca', 'D-004'),
    ('A Culpa é das Estrelas', 'John Green', 'Editora Intrínseca', 'F-006'),
    ('Dom Quixote', 'Miguel de Cervantes', 'Editora Nova Fronteira', 'G-007'),
    ('Orgulho e Preconceito', 'Jane Austen', 'Editora Martin Claret', 'H-008'),
    ('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Editora Martins Fontes', 'I-009'),
    ('A Revolução dos Bichos', 'George Orwell', 'Editora Companhia das Letras', 'J-010'),
	('Moby Dick', 'Herman Melville', 'Editora Penguin Companhia', 'K-011'),
    ('O Morro dos Ventos Uivantes', 'Emily Bronte', 'Editora Martin Claret', 'L-012'),
	('Viagem ao Centro da Terra', 'Júlio Verne', 'Editora FTD', 'D-030');

INSERT INTO usuarios (username, password)
VALUES
    ('marisangila', 'mari'), -- A mestra das senhas secretas
    ('admin', 'admin'); -- A guardiã da senha forte

