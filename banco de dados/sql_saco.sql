CREATE DATABASE IF NOT EXISTS tb_saco
DEFAULT CHARSET = latin1
DEFAULT COLLATE = latin1_general_ci;

USE tb_saco;

CREATE TABLE IF NOT EXISTS tb01_cliente (
    tb01_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tb01_nome VARCHAR(300),
    tb01_endereco VARCHAR(300),
    tb01_telefone VARCHAR(14)
);
ALTER TABLE tb01_cliente MODIFY COLUMN tb01_telefone VARCHAR(17);



CREATE TABLE IF NOT EXISTS tb02_saco (
    tb02_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tb02_descricao VARCHAR(300)

);


ALTER TABLE tb02_saco 
ADD COLUMN tb02_preco DECIMAL (4,2),
ADD COLUMN tb02_quantidade INT;

ALTER TABLE tb02_saco MODIFY COLUMN tb02_preco DECIMAL(6,2);

CREATE TABLE IF NOT EXISTS tb03_compras (
    tb03_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tb03_idCliente INT UNSIGNED NOT NULL,
    tb03_idSaco INT UNSIGNED NOT NULL,
    tb03_data DATE not null,
    FOREIGN KEY (tb03_idCliente) REFERENCES tb01_cliente(tb01_id),
    FOREIGN KEY (tb03_idSaco) REFERENCES tb02_saco(tb02_id)
);