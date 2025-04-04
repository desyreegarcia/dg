import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
from datetime import datetime
from produto import Produto
from cliente import Cliente

# Conectar ao banco
#conn, cursor = conexao_bd()

# Função para cadastrar produtos
def cadastrar_produto():
    categoria = entry_categoria.get()
    tamanho = entry_tamanho.get()
    valor = float(entry_valor.get())

    #cursor.execute("INSERT INTO produtos (categoria, tamanho, valor_venda) VALUES (%s, %s, %s)", 
                   #(categoria, tamanho, valor))
    #conn.commit()
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

# Função para cadastrar clientes
def cadastrar_cliente():
    nome = entry_cliente.get()
    telefone = entry_fone.get()

    #cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (nome, telefone))
    #conn.commit()
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
categoria = Label(interface, text="Categoria:")
categoria.grid(row=0, column=0)
entry_categoria = Entry(interface)
entry_categoria.grid(row=0, column=1)

tamanho = Label(interface, text="Tamanho:")
tamanho.grid(row=1, column=0)
entry_tamanho = Entry(interface)
entry_tamanho.grid(row=1, column=1)

valor = Label(interface, text="Valor Venda:")
valor.grid(row=2, column=0)
entry_valor = Entry(interface)
entry_valor.grid(row=2, column=1)

btn_produto = Button(interface, text="Cadastrar Produto", command=cadastrar_produto)
btn_produto.grid(row=3, column=1)

# Formulário para cadastrar clientes
cliente = Label(interface, text="Nome:")
cliente.grid(row=6, column=0)
entry_cliente = Entry(interface)
entry_cliente.grid(row=6, column=1)

fone = Label(interface, text="Telefone:")
fone.grid(row=7, column=0)
entry_fone = Entry(interface)
entry_fone.grid(row=7, column=1)

btn_cliente = Button(interface, text="Cadastrar Cliente", command=cadastrar_cliente)
btn_cliente.grid(row=8, column=1)

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