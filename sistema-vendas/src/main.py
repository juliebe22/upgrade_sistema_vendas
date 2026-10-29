import tkinter as tk
from tkinter import messagebox
from vendas import abrir_tela_vendas
from relatorio import abrir_tela_relatorio


def abrir_vendas():
    abrir_tela_vendas(janela)


def abrir_relatorio():
    abrir_tela_relatorio(janela)


janela = tk.Tk()

janela.title("Sistema de Vendas")
janela.geometry("500x400")
janela.resizable(False, False)


titulo = tk.Label(
    janela,
    text="SISTEMA DE VENDAS",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=40)


botao_vendas = tk.Button(
    janela,
    text="Registrar Venda",
    font=("Arial", 14),
    width=25,
    command=abrir_vendas
)

botao_vendas.pack(pady=10)


botao_relatorio = tk.Button(
    janela,
    text="Relatório de Vendas",
    font=("Arial", 14),
    width=25,
    command=abrir_relatorio
)

botao_relatorio.pack(pady=10)


botao_sair = tk.Button(
    janela,
    text="Sair",
    font=("Arial", 14),
    width=25,
    command=janela.destroy
)

botao_sair.pack(pady=10)


janela.mainloop()