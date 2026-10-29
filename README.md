# Sistema de Vendas — Integração com Supabase e Redis

## 1. Sobre o projeto

O Sistema de Vendas é uma aplicação desenvolvida em Python com interface gráfica para auxiliar no gerenciamento de produtos, estoque e vendas.

O projeto busca resolver a necessidade de registrar vendas, acompanhar o estoque e consultar informações de forma organizada. Além disso, utiliza serviços em nuvem para persistência dos dados e cache, demonstrando a integração entre uma aplicação desktop, um banco de dados e uma tecnologia de armazenamento temporário.

## 2. Objetivo

O objetivo do projeto é integrar uma aplicação Python a um banco de dados Supabase e utilizar o Redis para otimizar o acesso aos produtos, reduzindo consultas repetidas ao banco de dados.

## 3. Principais funcionalidades

- Listagem de produtos cadastrados.
- Consulta de preços e estoque.
- Registro de vendas.
- Validação da quantidade disponível.
- Atualização do estoque após uma venda.
- Registro das informações das vendas.
- Consulta de relatórios.
- Cache de produtos utilizando Redis.
- Interface gráfica desenvolvida com Tkinter.

## 4. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **Tkinter:** criação da interface gráfica.
- **Supabase:** serviço utilizado para armazenamento e consulta dos dados.
- **PostgreSQL:** banco de dados relacional utilizado pelo Supabase.
- **Redis:** armazenamento temporário dos dados acessados frequentemente.
- **Upstash:** serviço utilizado para disponibilizar o Redis em nuvem.
- **python-dotenv:** carregamento das variáveis de ambiente.

## 5. Integração com o Supabase

O Supabase funciona como banco de dados principal da aplicação, armazenando os produtos, as vendas e as movimentações relacionadas ao sistema.

A conexão é realizada por meio da biblioteca `supabase-py`, utilizando as credenciais configuradas em variáveis de ambiente.

A integração permite:

- Consultar produtos e seus estoques.
- Registrar vendas no banco de dados.
- Atualizar o estoque após as vendas.
- Armazenar as informações necessárias para os relatórios.
- Consultar a view `vw_relatorio_vendas`.

O registro das vendas utiliza a função RPC `registrar_venda`, responsável por executar as operações de registro da venda no banco de dados.

## 6. Integração com o Redis

O Redis foi utilizado como mecanismo de cache para a listagem de produtos, por meio do serviço Upstash.

O cache está implementado no arquivo `src/cache.py` e é utilizado pelo módulo responsável pela consulta dos produtos.

### Como funciona

1. O sistema verifica se a lista de produtos está armazenada no Redis.
2. Se os dados não estiverem disponíveis, ocorre um **Cache Miss**. Nesse caso, o sistema consulta o Supabase e armazena o resultado temporariamente no Redis.
3. Se os dados já estiverem armazenados, ocorre um **Cache Hit**, permitindo recuperar a lista sem realizar uma nova consulta ao Supabase.
4. O cache possui um tempo de expiração de 60 segundos.
5. Após o registro de uma venda, o cache de produtos é invalidado para evitar a reutilização de informações antigas sobre o estoque.

### Por que o Redis foi escolhido?

O Redis permite armazenar temporariamente dados que são consultados com frequência, reduzindo consultas repetidas ao banco de dados principal.

Sua utilização demonstra uma estratégia de cache que pode melhorar a eficiência da aplicação, especialmente em operações de leitura frequentes.

### Teste do cache

Para testar o funcionamento do Redis, execute:

```bash
python src/testar_cache.py
```

As mensagens exibidas no terminal indicam o comportamento do cache:

- `CACHE MISS`: os produtos não foram encontrados no cache.
- `CACHE HIT`: os produtos foram recuperados do cache.
- `CACHE INVALIDADO`: o cache foi removido após uma alteração.

## 7. Estrutura do projeto

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
├── .gitignore
├── requirements.txt
└── README.md
```

## 8. Instalação, configuração e execução

### Pré-requisitos

- Python instalado.
- Projeto configurado no Supabase.
- Instância Redis configurada no Upstash.

### 8.1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd sistema-vendas
```

Substitua `LINK_DO_REPOSITORIO` pelo endereço do repositório.

### 8.2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 8.3. Configurar as variáveis de ambiente

Crie um arquivo `.env` na pasta principal do projeto:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
UPSTASH_REDIS_REST_URL=sua_url_do_redis
UPSTASH_REDIS_REST_TOKEN=seu_token_do_redis
```

Substitua os valores de exemplo pelas credenciais dos serviços utilizados.

**Importante:** o arquivo `.env` contém credenciais privadas e não deve ser enviado ao GitHub. Ele deve estar listado no arquivo `.gitignore`.

### 8.4. Executar a aplicação

Na pasta principal do projeto, execute:

```bash
python src/main.py
```

A interface gráfica será aberta, permitindo utilizar as funcionalidades do sistema.

### 8.5. Testar o Redis

Em outro momento, ou após fechar a aplicação se necessário, execute:

```bash
python src/testar_cache.py
```

Observe as mensagens exibidas no terminal para verificar o comportamento do cache.

## 9. Capturas de tela

### Interface principal

<img width="498" height="425" alt="image" src="https://github.com/user-attachments/assets/7a86747a-0ba4-4702-84b2-3af5cb4fbd33" />

### Registro de vendas

![Tela de registro de vendas](screenshots/tela-vendas.png)

### Relatório de vendas

![Relatório de vendas](screenshots/relatorio-vendas.png)

### Integração com o Redis

![Teste de Cache Hit e Cache Miss](screenshots/teste-cache.png)

> Para exibir as imagens no GitHub, crie a pasta `screenshots` na raiz do projeto e coloque nela as capturas de tela com os nomes indicados acima.

## 10. Vídeo de demonstração

**Link do vídeo:** [Assistir à demonstração](https://drive.google.com/file/d/11l2LHpIFmA1irFTbg6cElfHvFi2_7ynH/view?usp=sharing)

## 11. Considerações finais

O projeto demonstra a integração de uma aplicação Python com interface gráfica, um banco de dados relacional em nuvem e um sistema de cache. A utilização do Supabase permite persistir e consultar os dados, enquanto o Redis possibilita reutilizar temporariamente informações acessadas com frequência, reduzindo consultas repetidas ao banco principal.

---

**Projeto desenvolvido para fins acadêmicos.**
