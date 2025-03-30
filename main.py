from produto import Produto
from cliente import Cliente
from venda import Venda

# Exemplo de uso
gato_pijama = Produto("Pijama de Gato", "M", 25.99)
panda_pijama = Produto("Pijama de Panda", "G", 29.99)

cliente1 = Cliente("Maria Silva", "912345678")

venda1 = Venda(cliente1)
venda1.adicionar_produto(gato_pijama)
venda1.adicionar_produto(panda_pijama)

print(venda1)