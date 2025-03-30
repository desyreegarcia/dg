class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    
    def __str__(self):
        return f"Cliente: {self.nome} | Telefone: {self.telefone}"