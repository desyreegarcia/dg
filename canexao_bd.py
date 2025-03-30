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
                id INT AUTO_INCREMENT PRIMARY KEY,
                categoria VARCHAR(255),
                tamanho VARCHAR(10),
                valor_venda FLOAT)
        """
        query_cliente = """
            CREATE TABLE IF NOT EXISTS cliente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                telefone VARCHAR(20));
        """
        query_venda = """
            CREATE TABLE IF NOT EXISTS venda (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                produto_id INT,
                data_venda DATETIME,
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

    def selecionar_produto(self, id: int) -> list:
        query = 'SELECT * FROM produto'
        return self.connection.execute(query).fetchall()
    
banco = BandoDeDados("vendas_dg")
#banco.criar_tabelas()
#json_produto = {'categoria' : 'Americano Longo', 'tamanho':'G', 'valor_venda':'99.90'}
#banco.cadastrar_produto(json_produto)
resultado = banco.selecionar_produto(0)
print(resultado)
