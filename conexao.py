import sqlite3 as bd

def conectarBanco():
    try:
        # Conectar ao banco de dados
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()
        
        # Criar as tabelas
        criarTabela = """
        CREATE TABLE IF NOT EXISTS tb01_cliente (
            tb01_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tb01_nome TEXT,
            tb01_endereco TEXT,
            tb01_telefone TEXT
        );

        CREATE TABLE IF NOT EXISTS tb02_saco (
            tb02_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tb02_descricao TEXT,
            tb02_preco REAL,
            tb02_quantidade INTEGER
        );

        CREATE TABLE IF NOT EXISTS tb03_compras (
            tb03_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tb03_idCliente INTEGER NOT NULL,
            tb03_idSaco INTEGER NOT NULL,
            tb03_data DATE NOT NULL,
            FOREIGN KEY (tb03_idCliente) REFERENCES tb01_cliente(tb01_id),
            FOREIGN KEY (tb03_idSaco) REFERENCES tb02_saco(tb02_id)
        );
        """
        
        # Executando a criação das tabelas
        cursor.executescript(criarTabela)
        conn.commit()
        print("SUCESSO")
        
    except Exception as e:
        print("Deu erro: " + str(e))
    finally:
        # Fechar a conexão
        conn.close()

# Chamar a função para criar as tabelas
conectarBanco()
