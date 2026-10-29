
from database import supabase
from cache import (
    buscar_cache_produtos,
    salvar_cache_produtos
)


def listar_produtos():
    # 1. Tenta buscar os produtos no Redis
    produtos_cache = buscar_cache_produtos()

    if produtos_cache is not None:
        return produtos_cache

    # 2. Se não houver cache, consulta o Supabase
    resposta = (
        supabase.table("produtos")
        .select("id_produto,nome,preco,estoque")
        .order("id_produto")
        .execute()
    )

    produtos = resposta.data

    # 3. Guarda o resultado no Redis por 60 segundos
    salvar_cache_produtos(produtos)

    print("Produtos consultados no Supabase e salvos no Redis.")

    return produtos
