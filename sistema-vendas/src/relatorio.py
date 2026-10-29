
import tkinter as tk
from tkinter import ttk, messagebox
from database import supabase


def listar_vendas():
    resposta = (
        supabase.table("vw_relatorio_vendas")
        .select("*")
        .order("data", desc=True)
        .execute()
    )
    return resposta.data


def abrir_tela_relatorio(janela_principal):
    tela = tk.Toplevel(janela_principal)
    tela.title("Relatório de Vendas")
    tela.geometry("1000x450")

    tk.Label(
        tela,
        text="RELATÓRIO DE VENDAS",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    colunas = (
        "ID",
        "Data",
        "Produto",
        "Quantidade",
        "Preço",
        "Total",
        "Pagamento"
    )

    tabela = ttk.Treeview(
        tela,
        columns=colunas,
        show="headings"
    )

    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=130)

    tabela.pack(fill="both", expand=True, padx=20, pady=10)

    try:
        vendas = listar_vendas()

        for venda in vendas:
            tabela.insert(
                "",
                tk.END,
                values=(
                    venda["id_venda"],
                    venda["data"],
                    venda["produto"],
                    venda["quantidade"],
                    venda["preco_unitario"],
                    venda["valor_total"],
                    venda["forma_pagamento"]
                )
            )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível carregar o relatório:\n{erro}",
            parent=tela
        )
