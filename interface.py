import tkinter as tk
from tkinter import StringVar, Tk, Label, Entry, Button, messagebox, ttk
from datetime import datetime
from canexao_bd import BandoDeDados
from produto import Produto
from cliente import Cliente

conexao = BandoDeDados("vendas_dgpijamas.db")

# Função para cadastrar produtos
def cadastrar_produto(categoria, tamanho, valor_venda):
    print(f'categoria {categoria}, tamanho {tamanho} e preço de venda {valor_venda}')
    conexao.cadastrar_produto({'categoria':categoria, 'tamanho':tamanho, 'valor_venda':valor_venda})
    #lista_produtos = conexao_bd.
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

# Função para cadastrar clientes
def cadastrar_cliente(cliente, telefone):
    print(f'nome {cliente}, telefone {telefone}')
    conexao.cadastrar_cliente({'nome':cliente, 'telefone':telefone})
    #lista_produtos = conexao_bd.
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

# Função para cadastrar vendas
def cadastrar_venda():
    cliente_id = cliente_dict.get(cliente_var.get())
    produto_id = produto_dict.get(produto_var.get())

    if not cliente_id or not produto_id:
        messagebox.showerror("Erro", "Selecione cliente e produto.")
        return

    venda = {'cliente_id': cliente_id, 'produto_id': produto_id,'data_venda': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")
    listar_vendas()

def listar_vendas():
    for row in treeview.get_children():
        treeview.delete(row)

    vendas = conexao.selecionar_venda()
    for venda in vendas:
        venda_id, cliente_id, produto_id, data_venda = venda

        cliente = conexao.selecionar_cliente(cliente_id)
        produto = conexao.selecionar_produto(produto_id)

        if cliente and produto:
            cliente_nome = cliente[0][1]
            categoria = produto[0][1]
            valor_venda = produto[0][3]

            treeview.insert('', 'end', values=(cliente_nome, categoria, valor_venda, data_venda))

# Criando a interface gráfica
interface = Tk()
interface.title("DG Pijamas")

# Formulário para cadastrar produtos
titulo_cadastro_produtos = Label(interface, text="Cadastro de Produtos")
titulo_cadastro_produtos.grid(row=1, column=0, columnspan=2, pady=10)
categoria = Label(interface, text="Categoria:")
categoria.grid(row=2, column=0)
entry_categoria = Entry(interface)
entry_categoria.grid(row=2, column=1)

tamanho = Label(interface, text="Tamanho:")
tamanho.grid(row=3, column=0)
entry_tamanho = Entry(interface)
entry_tamanho.grid(row=3, column=1)

valor_venda = Label(interface, text="Valor Venda:")
valor_venda.grid(row=4, column=0)
entry_valor_venda = Entry(interface)
entry_valor_venda.grid(row=4, column=1)

btn_produto = Button(
    interface, text="Cadastrar Produto",
    command=lambda:cadastrar_produto(entry_categoria.get(), entry_tamanho.get(), entry_valor_venda.get()))
btn_produto.grid(row=5, column=1, pady=10)

# Formulário para cadastrar clientes
titulo_cadastro_cliente = Label(interface, text="Cadastro de Clientes").grid(row=6, column=0, columnspan=2, pady=10)
cliente = Label(interface, text="Nome:").grid(row=7, column=0)
entry_cliente = Entry(interface).grid(row=7, column=1)

telefone = Label(interface, text="Telefone:").grid(row=8, column=0)
entry_telefone = Entry(interface).grid(row=8, column=1)

btn_cliente = Button(
    interface, text="Cadastrar Cliente",
    command=lambda:cadastrar_cliente(entry_cliente.get(), entry_telefone.get()))
btn_cliente.grid(row=9, column=1, pady=10)

# Formulário para cadastrar vendas
titulo_cadastro_venda = Label(interface, text="Cadastrar Nova Venda").grid(row=10, column=0, columnspan=2, pady=10)

cliente_var = StringVar()
produto_var = StringVar()

# Listas do banco
clientes = conexao.selecionar_cliente() #Isso retorna uma lista com os dados dos clientes, algo assim: [(1, 'Ana', '11999999999'), (2, 'Carlos', '11888888888')]
produtos = conexao.selecionar_produto() #Isso retorna uma lista com os dados dos produtos

# Dicionários exibição id
cliente_dict = {f"{c[0]} - {c[1]}": c[0] for c in clientes} #Para cada cliente c na lista clientes, crie uma chave do tipo "id - nome" e associe ao id
produto_dict = {f"{p[0]} - {p[1]} - {p[2]}": p[0] for p in produtos} #Para cada produto p na lista produto, crie uma chave do tipo "id - produto - valor" e associe ao id

venda_produto = Label(interface, text="Selecione o Produto:").grid(row=11, column=0)
entry_venda_produto = ttk.Combobox(interface, textvariable=produto_var, values=list(produto_dict.keys())).grid(row=11, column=1)

venda_cliente = Label(interface, text="Selecione o Cliente:").grid(row=12, column=0)
entry_venda_cliente = ttk.Combobox(interface, textvariable=cliente_var, values=list(cliente_dict.keys())).grid(row=12, column=1)

venda_data = Label(interface, text="Selecione a data:").grid(row=13, column=0)
entry_venda_data = Entry(interface).grid(row=13, column=1)

btn_venda = Button(
    interface, text="Cadastrar Venda",
    command=cadastrar_venda)
btn_venda.grid(row=14, column=1, pady=10)

treeview = ttk.Treeview(interface, columns=("cliente", "categoria", "valor_venda", "data_venda"), show="headings")
treeview.heading("cliente", text="cliente")
treeview.heading("categoria", text="categoria")
treeview.heading("valor_venda", text="valor_venda")
treeview.heading("data_venda", text="data_venda")
treeview.grid(row=15, column=0, columnspan=4, pady=10, sticky="nsew")

listar_vendas()
interface.mainloop()