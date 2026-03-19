# CÓDIGO EXEMPLO TKINTER:
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import (messagebox)

# ===============================
# Estrutura de dados (em memória)
# ===============================
# Lista de produtos (cada produto é um dicionário)
produtos = []

# ID incremental
proximo_id = 1

# ===============================
# Funções CRUD
# ===============================

def criar_produto():
    global proximo_id

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": qtd
    }

    produtos.append(produto)
    proximo_id += 1

    atualizar_lista()
    limpar_campos()


def ler_produto():
    try:
        indice = listbox.curselection()[0]
        produto = produtos[indice]

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, produto["nome"])

        entry_preco.delete(0, tk.END)
        entry_preco.insert(0, produto["preco"])

        entry_qtd.delete(0, tk.END)
        entry_qtd.insert(0, produto["quantidade"])
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")

from tkinter import messagebox

# ===============================
# Estrutura de dados (em memória)
# ===============================
# Lista de produtos (cada produto é um dicionário)
produtos = []

# ID incremental
proximo_id = 1

# ===============================
# Funções CRUD
# ===============================

def criar_produto():
    global proximo_id

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": qtd
    }

    produtos.append(produto)
    proximo_id += 1

    atualizar_lista()
    limpar_campos()


def ler_produto():
    try:
        indice = listbox.curselection()[0]
        produto = produtos[indice]

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, produto["nome"])

        entry_preco.delete(0, tk.END)
        entry_preco.insert(0, produto["preco"])

        entry_qtd.delete(0, tk.END)
        entry_qtd.insert(0, produto["quantidade"])

    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")


def atualizar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produtos[indice]["nome"] = nome
    produtos[indice]["preco"] = preco
    produtos[indice]["quantidade"] = qtd

    atualizar_lista()
    limpar_campos()


def deletar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    del produtos[indice]

    atualizar_lista()
    limpar_campos()

# ===============================
# Funções auxiliares
# ===============================

def atualizar_lista():
    listbox.delete(0, tk.END)
    for p in produtos:
        texto = f"ID: {p['id']} | {p['nome']} | R$ {p['preco']} | Qtd: {p['quantidade']}"
        listbox.insert(tk.END, texto)


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)

# ===============================
# Interface TkinterListbox
# ===============================

root = tk.Tk()
root.title("CRUD de Produtos")
root.geometry("600x400")

# Labels
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="Quantidade:").pack()
entry_qtd = tk.Entry(root)
entry_qtd.pack()

# Botões
tk.Button(root, text="Criar", command=criar_produto).pack(pady=5)
tk.Button(root, text="Ler", command=ler_produto).pack(pady=5)
tk.Button(root, text="Atualizar", command=atualizar_produto).pack(pady=5)
tk.Button(root, text="Deletar", command=deletar_produto).pack(pady=5)

# Lista de produtos
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()

def atualizar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produtos[indice]["nome"] = nome
    produtos[indice]["preco"] = preco
    produtos[indice]["quantidade"] = qtd

    atualizar_lista()
    limpar_campos()


def deletar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    del produtos[indice]

    atualizar_lista()
    limpar_campos()

# ===============================
# Funções auxiliares
# ===================import tkinter as tk
from tkinter import messagebox

# ===============================
# Estrutura de dados (em memória)
# ===============================
# Lista de produtos (cada produto é um dicionário)
produtos = []

# ID incremental
proximo_id = 1

# ===============================
# Funções CRUD
# ===============================

def criar_produto():
    global proximo_id

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": qtd
    }

    produtos.append(produto)
    proximo_id += 1

    atualizar_lista()
    limpar_campos()


def ler_produto():
    try:
        indice = listbox.curselection()[0]
        produto = produtos[indice]

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, produto["nome"])

        entry_preco.delete(0, tk.END)
        entry_preco.insert(0, produto["preco"])

        entry_qtd.delete(0, tk.END)
        entry_qtd.insert(0, produto["quantidade"])

    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")


def atualizar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    nome = entry_nome.get()
    preco = entry_preco.get()
    qtd = entry_qtd.get()

    if nome == "" or preco == "" or qtd == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        preco = float(preco)
        qtd = int(qtd)
    except:
        messagebox.showerror("Erro", "Preço deve ser número e quantidade inteiro!")
        return

    produtos[indice]["nome"] = nome
    produtos[indice]["preco"] = preco
    produtos[indice]["quantidade"] = qtd

    atualizar_lista()
    limpar_campos()


def deletar_produto():
    try:
        indice = listbox.curselection()[0]
    except:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return

    del produtos[indice]

    atualizar_lista()
    limpar_campos()

# ===============================
# Funções auxiliares
# ===============================

def atualizar_lista():
    listbox.delete(0, tk.END)
    for p in produtos:
        texto = f"ID: {p['id']} | {p['nome']} | R$ {p['preco']} | Qtd: {p['quantidade']}"
        listbox.insert(tk.END, texto)


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)

# ===============================
# Interface Tkinter
# ===============================

root = tk.Tk()
root.title("CRUD de Produtos")
root.geometry("500x400")

# Labels
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="Quantidade:").pack()
entry_qtd = tk.Entry(root)
entry_qtd.pack()

# Botões
tk.Button(root, text="Criar", command=criar_produto).pack(pady=5)
tk.Button(root, text="Ler", command=ler_produto).pack(pady=5)
tk.Button(root, text="Atualizar", command=atualizar_produto).pack(pady=5)
tk.Button(root, text="Deletar", command=deletar_produto).pack(pady=5)

# Lista de produtos
listbox = tk.Listbox(root, values=["BA", "SE"])
listbox.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()
#================

def atualizar_lista():
    listbox.delete(0, tk.END)
    for p in produtos:
        texto = f"ID: {p['id']} | {p['nome']} | R$ {p['preco']} | Qtd: {p['quantidade']}"
        listbox.insert(tk.END, texto)


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)

# ===============================
# Interface Tkinter
# ===============================

root = tk.Tk()
root.title("CRUD de Produtos")
root.geometry("500x400")

# Labels
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Preço:").pack()
entry_preco = tk.Entry(root)
entry_preco.pack()

tk.Label(root, text="Quantidade:").pack()
entry_qtd = tk.Entry(root)
entry_qtd.pack()

# Botões
tk.Button(root, text="Criar", command=criar_produto).pack(pady=5)
tk.Button(root, text="Ler", command=ler_produto).pack(pady=5)
tk.Button(root, text="Atualizar", command=atualizar_produto).pack(pady=5)
tk.Button(root, text="Deletar", command=deletar_produto).pack(pady=5)

# Lista de produtos
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()

