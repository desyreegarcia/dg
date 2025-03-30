from datetime import datetime
from produto import Produto
from cliente import Cliente

class Venda:
    def __init__(self, produto: Produto, cliente: Cliente):
        self.cliente = cliente
        self.produto = produto
        self.data_venda = datetime.now()
    
    def calcular_total_venda(self):
        return sum(produto.valor_venda for produto in self.produto)
    
    def __str__(self):
        produtos_str = "\n".join(str(prod) for prod in self.produto)
        return (f"Venda realizada em {self.data_venda}\n"
                f"Cliente: {self.cliente.nome}\n"
                f"Produtos:\n{produtos_str}\n"
                f"Total da Venda: {self.calcular_total_venda():.2f}")