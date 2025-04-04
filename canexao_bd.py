import sqlite3

# Conexão com o banco
class BandoDeDados:
    def __init__(self, nome):
        self.nome = nome
        self.connection = sqlite3.connect(nome)
    
    # Criando tabela de produtos
    def criar_tabelas(self):
        query_produto = """
            CREATE TABLE IF NOT EXISTS produto (
                id INTERGER AUTO_INCREMENT PRIMARY KEY NOT NULL,
                categoria TEXT(255) NOT NULL,
                tamanho TEXT(10) NOT NULL,
                valor_venda REAL NOT NULL)
        """
        query_cliente = """
            CREATE TABLE IF NOT EXISTS cliente (
                id INTERGER AUTO_INCREMENT PRIMARY KEY NOT NULL,
                nome TEXT(255) NOT NULL,
                telefone TEXT(11) NOT NULL);
        """
        query_venda = """
            CREATE TABLE IF NOT EXISTS venda (
                id INTERGER AUTO_INCREMENT PRIMARY KEY NOT NULL,
                cliente_id INTERGER NOT NULL,
                produto_id INTERGER NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
                FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE CASCADE)
        """
        self.connection.execute(query_cliente)
        self.connection.execute(query_produto)
        self.connection.execute(query_venda)
    
    def cadastrar_produto(self, produto : dict):
        query = "INSERT INTO produto (categoria, tamanho, valor_venda) VALUES (:categoria, :tamanho, :valor_venda)"
        self.connection.execute(query, produto)
        self.connection.commit()

    def selecionar_produto(self, id: int = 0) -> list:
        if id > 0:
            query = f'SELECT * FROM produto WHERE id={id}'
            return self.connection.execute(query).fetchall()
        else:
            query = 'SELECT * FROM produto'
            return self.connection.execute(query).fetchall()
        
    def cadastrar_cliente(self, cliente : dict):
        query = "INSERT INTO cliente (nome, telefone) VALUES (:nome, :telefone)"
        self.connection.execute(query, cliente)
        self.connection.commit()

    def selecionar_cliente(self, id: int = 0) -> list:
        if id > 0:
            query = f'SELECT * FROM cliente WHERE id={id}'
            return self.connection.execute(query).fetchall()
        else:
            query = 'SELECT * FROM cliente'
            return self.connection.execute(query).fetchall()
        
    def cadastrar_venda(self, cliente : dict):
        query = "INSERT INTO venda (cliente, produto, data) VALUES (:cliente, :produto, :data)"
        self.connection.execute(query, cliente)
        self.connection.commit()

    def selecionar_venda(self, id: int = 0) -> list:
        if id > 0:
            query = f'SELECT * FROM venda WHERE id={id}'
            return self.connection.execute(query).fetchall()
        else:
            query = 'SELECT * FROM venda'
            return self.connection.execute(query).fetchall()
    
banco = BandoDeDados("vendas_dg.db")
#banco.criar_tabelas()
resultado = banco.selecionar_produto(1)
print(resultado)