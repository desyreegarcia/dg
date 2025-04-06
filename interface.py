import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
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
'''def cadastrar_venda():
    cliente_id = entry_cliente_id.get()
    total_venda = entry_total_venda.get()

    if not cliente_id.isdigit() or not total_venda.replace(".", "").isdigit():
        messagebox.showerror("Erro", "ID do cliente e total da venda devem ser números.")
        return

    cliente_id = int(cliente_id)
    total_venda = float(total_venda)
    data_venda = datetime.now()

    cursor.execute("INSERT INTO vendas (cliente_id, data_venda, total_venda) VALUES (%s, %s, %s)", 
                   (cliente_id, data_venda, total_venda))
    conn.commit()
    messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")

# Função para exibir relatórios
def exibir_relatorios():
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    
    if not vendas:
        messagebox.showinfo("Relatório de Vendas", "Nenhuma venda registrada ainda.")
        return

    relatorio = "\n".join(
        f"ID: {venda[0]} | Cliente ID: {venda[1]} | Data: {venda[2]} | Total: {venda[3]}€"
        for venda in vendas
    )
    
    messagebox.showinfo("Relatório de Vendas", relatorio)'''

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
titulo_cadastro_cliente = Label(interface, text="Cadastro de Clientes")
titulo_cadastro_cliente.grid(row=6, column=0, columnspan=2, pady=10)
cliente = Label(interface, text="Nome:")
cliente.grid(row=7, column=0)
entry_cliente = Entry(interface)
entry_cliente.grid(row=7, column=1)

telefone = Label(interface, text="Telefone:")
telefone.grid(row=8, column=0)
entry_telefone = Entry(interface)
entry_telefone.grid(row=8, column=1)

btn_cliente = Button(
    interface, text="Cadastrar Cliente",
    command=lambda:cadastrar_cliente(entry_cliente.get(), entry_telefone.get()))
btn_cliente.grid(row=9, column=1, pady=10)

'''# Formulário para cadastrar vendas
Label(interface, text="ID do Cliente:").pack()
entry_cliente_id = Entry(interface)
entry_cliente_id.pack()

Label(interface, text="Total Venda:").pack()
entry_total_venda = Entry(interface)
entry_total_venda.pack()

#tk.Button(root, text="Cadastrar Venda", command=cadastrar_venda).pack()

# Botão para exibir relatório de vendas
#tk.Button(root, text="Relatório de Vendas", command=exibir_relatorios).pack()

# Fechar conexão com o banco ao fechar a aplicação
def fechar_conexao():
    cursor.close()
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", fechar_conexao)'''

interface.mainloop()