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

    def selecionar_produto(self, id: int) -> list:
        query = 'SELECT * FROM produto'
        return self.connection.execute(query).fetchall()
    
banco = BandoDeDados("vendas_dg.db")
#banco.criar_tabelas()
#json_produto = {'categoria' : 'Americano Longo', 'tamanho':'G', 'valor_venda':'99.90'}
#banco.cadastrar_produto(json_produto)
resultado = banco.selecionar_produto(1)
print(resultado)