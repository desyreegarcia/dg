class Produto:
    def __init__(self, categoria, tamanho, valor_venda):
        self.categoria = categoria
        self.tamanho = tamanho
        self.valor_venda = valor_venda

    def __str__(self):
        return f"Produto: {self.categoria} | Tamanho: {self.tamanho} | Preço: {self.valor_venda:.2f}"
