
from database import supabase

try:
    resposta = (
        supabase.table("produtos")
        .select("id_produto,nome,preco,estoque")
        .execute()
    )

    print("Conexão com Supabase funcionando!")
    print("Produtos encontrados:", len(resposta.data))

    for produto in resposta.data:
        print(produto)

except Exception as erro:
    print("Erro ao consultar o Supabase:")
    print(erro)
