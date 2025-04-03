import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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
    nome = entry_nome.get()
    telefone = entry_telefone.get()

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
root = tk.Tk()
root.title("Loja de Pijamas")

# Formulário para cadastrar produtos
tk.Label(root, text="Categoria:").pack()
entry_categoria = tk.Entry(root)
entry_categoria.pack()

tk.Label(root, text="Tamanho:").pack()
entry_tamanho = tk.Entry(root)
entry_tamanho.pack()

tk.Label(root, text="Valor Venda:").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto).pack()

# Formulário para cadastrar clientes
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Telefone:").pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

tk.Button(root, text="Cadastrar Cliente", command=cadastrar_cliente).pack()

# Formulário para cadastrar vendas
tk.Label(root, text="ID do Cliente:").pack()
entry_cliente_id = tk.Entry(root)
entry_cliente_id.pack()

tk.Label(root, text="Total Venda:").pack()
entry_total_venda = tk.Entry(root)
entry_total_venda.pack()

#tk.Button(root, text="Cadastrar Venda", command=cadastrar_venda).pack()

# Botão para exibir relatório de vendas
#tk.Button(root, text="Relatório de Vendas", command=exibir_relatorios).pack()

# Fechar conexão com o banco ao fechar a aplicação
'''def fechar_conexao():
    cursor.close()
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", fechar_conexao)'''

root.mainloop()