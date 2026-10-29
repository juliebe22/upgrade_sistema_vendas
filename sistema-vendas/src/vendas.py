
import tkinter as tk
from tkinter import messagebox, ttk

from database import supabase
from produtos import listar_produtos
from cache import invalidar_cache_produtos


def buscar_produtos():
    return listar_produtos()


def registrar_venda(id_produto, quantidade, forma_pagamento):
    resposta = supabase.rpc(
        "registrar_venda",
        {
            "p_id_produto": id_produto,
            "p_quantidade": quantidade,
            "p_forma_pagamento": forma_pagamento
        }
    ).execute()

    return resposta.data


def abrir_tela_vendas(janela_principal):
    tela = tk.Toplevel(janela_principal)
    tela.title("Registrar Venda")
    tela.geometry("500x450")
    tela.resizable(False, False)

    tk.Label(
        tela,
        text="REGISTRAR VENDA",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    try:
        produtos = buscar_produtos()
    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível carregar os produtos:\n{erro}",
            parent=tela
        )
        tela.destroy()
        return

    produtos_dict = {}

    for produto in produtos:
        texto = (
            f"{produto['nome']} - "
            f"R$ {float(produto['preco']):.2f} "
            f"(Estoque: {produto['estoque']})"
        )
        produtos_dict[texto] = produto["id_produto"]

    tk.Label(tela, text="Produto:").pack()

    combo_produtos = ttk.Combobox(
        tela,
        values=list(produtos_dict.keys()),
        state="readonly",
        width=42
    )
    combo_produtos.pack(pady=8)

    if produtos:
        combo_produtos.current(0)

    tk.Label(tela, text="Quantidade:").pack()

    entrada_quantidade = tk.Entry(tela)
    entrada_quantidade.pack(pady=8)

    tk.Label(tela, text="Forma de pagamento:").pack()

    combo_pagamento = ttk.Combobox(
        tela,
        values=[
            "PIX",
            "Dinheiro",
            "Cartão de Crédito",
            "Cartão de Débito"
        ],
        state="readonly",
        width=30
    )
    combo_pagamento.pack(pady=8)
    combo_pagamento.current(0)

    def confirmar():
        produto_selecionado = combo_produtos.get()

        if not produto_selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione um produto.",
                parent=tela
            )
            return

        try:
            quantidade = int(entrada_quantidade.get())

            if quantidade <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Quantidade inválida",
                "Digite um número inteiro maior que zero.",
                parent=tela
            )
            return

        try:
            resultado = registrar_venda(
                produtos_dict[produto_selecionado],
                quantidade,
                combo_pagamento.get()
            )

            # Invalida o cache após a venda ser registrada.
            invalidar_cache_produtos()

            if isinstance(resultado, dict):
                mensagem = (
                    f"Venda registrada!\n\n"
                    f"Produto: {resultado.get('produto', '')}\n"
                    f"Quantidade: {resultado.get('quantidade', quantidade)}\n"
                    f"Total: R$ {float(resultado.get('valor_total', 0)):.2f}"
                )
            else:
                mensagem = "Venda registrada com sucesso!"

            messagebox.showinfo(
                "Sucesso",
                mensagem,
                parent=tela
            )
            tela.destroy()

        except Exception as erro:
            messagebox.showerror(
                "Erro ao registrar venda",
                str(erro),
                parent=tela
            )

    tk.Button(
        tela,
        text="Registrar Venda",
        font=("Arial", 12, "bold"),
        width=22,
        command=confirmar
    ).pack(pady=25)
