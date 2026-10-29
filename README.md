# Sistema de Vendas — Python, Supabase e Redis

## Sobre o projeto

Sistema de vendas desenvolvido em Python com interface gráfica Tkinter, integrado ao Supabase para armazenamento dos dados e ao Redis para cache de produtos.

O projeto foi desenvolvido a partir de um sistema de vendas existente, com o objetivo de implementar integração com banco de dados em nuvem e armazenamento temporário em cache.

## Funcionalidades

- Consulta de produtos e estoque.
- Registro de vendas.
- Validação da quantidade e da forma de pagamento.
- Atualização automática do estoque após uma venda.
- Registro de movimentações financeiras.
- Relatório de vendas.
- Cache de produtos utilizando Redis.
- Interface gráfica desenvolvida com Tkinter.

## Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Tkinter:** desenvolvimento da interface gráfica.
- **Supabase:** armazenamento e consulta dos dados na nuvem.
- **PostgreSQL:** banco de dados utilizado pelo Supabase.
- **Redis:** armazenamento temporário dos dados consultados.
- **Upstash:** serviço de Redis em nuvem.
- **python-dotenv:** gerenciamento de variáveis de ambiente.

## Integração com Supabase

O Supabase é utilizado como banco de dados principal do sistema, armazenando produtos, vendas e movimentações.

A integração permite consultar produtos, registrar vendas e recuperar os dados necessários para a geração de relatórios.

A função `registrar_venda` realiza as seguintes operações:

1. Valida a quantidade solicitada.
2. Verifica a existência do produto.
3. Confere se há estoque suficiente.
4. Calcula o valor total da venda.
5. Atualiza o estoque.
6. Registra a venda e a movimentação correspondente.

## Integração com Redis

O Redis é utilizado como cache para a listagem de produtos, evitando consultas repetidas ao Supabase quando os dados já estão armazenados temporariamente.

O cache possui um tempo de expiração de 60 segundos e é invalidado após o registro de uma venda.

O funcionamento pode ser observado pelas mensagens:

- `CACHE MISS`: os dados não foram encontrados no cache e precisam ser consultados no Supabase.
- `CACHE HIT`: os dados foram encontrados no cache e podem ser reutilizados.
- `CACHE INVALIDADO`: o cache de produtos foi removido após uma alteração.

Essa estratégia reduz consultas desnecessárias ao banco de dados e demonstra o uso prático de cache em uma aplicação.

## Estrutura do projeto

```text
sistema-vendas/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── cache.py
│   ├── produtos.py
│   ├── vendas.py
│   ├── relatorio.py
│   └── testar_cache.py
├── database/
│   ├── tables/
│   ├── inserts/
│   ├── functions/
│   ├── procedures/
│   └── views/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
## Como executar o projeto

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar as variáveis de ambiente

Crie um arquivo `.env` na pasta principal do projeto e configure suas credenciais do Supabase e do Redis:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
UPSTASH_REDIS_REST_URL=sua_url_do_redis
UPSTASH_REDIS_REST_TOKEN=seu_token_do_redis
```

**Importante:** não publique o arquivo `.env` no GitHub.

### 3. Executar o sistema

Na pasta principal do projeto, execute:

```bash
python src/main.py
```

### 4. Testar o Redis

Para verificar o funcionamento do cache, execute:

```bash
python src/testar_cache.py
```

### 5. Vídeo de demonstração

**Link do vídeo:** [Assistir à demonstração](COLE_AQUI_O_LINK_DO_DRIVE)
