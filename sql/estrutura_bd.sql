- Criação do banco de dados para gerenciar uma biblioteca escolar - SGB
CREATE DATABASE IF NOT EXISTS SGB;
USE SGB;

-- Tabela Categoria
CREATE TABLE Categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT
);

-- Tabela Livro
CREATE TABLE Livro (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    sinopse TEXT,
    capa TEXT,
    quantidade INT DEFAULT 1,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

-- Tabela Aluno
CREATE TABLE Aluno(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    serie VARCHAR(20) NOT NULL,
    status ENUM('ativo', 'bloqueado') DEFAULT 'ativo'
);

-- Tabela professor
CREATE TABLE professor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    disciplina VARCHAR(50),
    status ENUM('ativo', 'inativo',) DEFAULT 'ativo'
);

--Tabela Bibliotecario
CREATE TABLE Bibliotecario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

-- Tabela Diretor
CREATE TABLE Diretor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

-- Tabela Supervisor
CREATE TABLE Supervisor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

-- Tabela Emprestimo
CREATE TABLE Emprestimo(
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT,
    livro_id INT,
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE,
    data_devolucao_real DATE,
    multa DECIMAL(6,2) DEFAULT 0.00,
    FOREIGN KEY (aluno_id) REFERENCES Aluno(id),
    FOREIGN KEY (livro_id) REFERENCES Livro(id)
);

-- Tabela Reserva

    
    

    
