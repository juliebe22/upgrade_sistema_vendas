import os
from dotenv import load_dotenv
from upstash_redis import Redis

load_dotenv()

url = os.getenv("UPSTASH_REDIS_REST_URL")
token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if not url or not token:
    raise ValueError(
        "Configure UPSTASH_REDIS_REST_URL e "
        "UPSTASH_REDIS_REST_TOKEN no arquivo .env"
    )

redis = Redis(url=url, token=token)

CHAVE_PRODUTOS = "sistema-vendas:produtos"


def buscar_cache_produtos():
    dados = redis.get(CHAVE_PRODUTOS)

    if dados is None:
        print("CACHE MISS - Produtos não encontrados no Redis.")
        return None

    import json

    print("CACHE HIT - Produtos carregados do Redis.")
    return json.loads(dados)


def salvar_cache_produtos(produtos):
    import json

    redis.set(
        CHAVE_PRODUTOS,
        json.dumps(produtos, ensure_ascii=False),
        ex=60
    )


def invalidar_cache_produtos():
    redis.delete(CHAVE_PRODUTOS)
    print("CACHE INVALIDADO - Lista de produtos removida.")
