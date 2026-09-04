# API Pedidos

## Integrantes

1. Nome completo: Camila Eiko Honda Martins
   Turma: CC8P13
   RA: G78HFD-0

2. Nome completo: Leticia Costa de Moura
   Turma: CC8Q13
   RA: F35033-9

3. Nome completo: Vitor De Souza Botelho
   Turma: CC8P13
   RA: G819AJ-9

4. Nome completo: Caio Pacheco Andrade
   Turma: CC8P13
   RA: N08969-5

5. Nome completo: Fabricio Garcia
   Turma: CC7P13
   RA: R01501-7

6. Nome completo: Brian Borges Santos Silva
   Turma: CC7P13
   RA: F35159-9

## Visão geral

Este projeto é uma API REST para gerenciamento de pedidos, desenvolvida com FastAPI, SQLAlchemy e PostgreSQL. A aplicação permite criar, listar, consultar, atualizar e excluir pedidos, além de expor um endpoint de saúde para verificar se a aplicação e o banco de dados estão funcionando corretamente.

A solução foi pensada para ser executada de forma reproduzível com Docker Compose, sem depender de configurações locais do ambiente de desenvolvimento.

## Especificações do projeto

- API disponível em: http://localhost:8000
- Serviço da aplicação: `pedidos`
- Serviço do banco de dados: `postgres`
- Framework principal: FastAPI
- ORM: SQLAlchemy
- Banco de dados: PostgreSQL 16
- Migrations: Alembic
- Linguagem: Python 3.14

## Stack tecnológica

- Python 3.14
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Pydantic
- Docker / Docker Compose
- psycopg

## Estrutura do repositório

```text
.
├── alembic/
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       ├── c47afbb80b66_create_orders.py
│       └── 141894c96f4c_rename_price_to_unit_price.py
├── src/
│   └── app/
│       ├── models/
│       │   └── order.py
│       ├── routes/
│       │   └── orders.py
│       ├── schemas/
│       │   └── order.py
│       ├── service/
│       │   └── orders.py
│       ├── settings/
│       │   ├── database/
│       │   │   └── database.py
│       │   └── env/
│       │       └── env.py
├── .env.example
├── Dockerfile
├── README.md
├── docker-compose.yml
├── main.py
├── pyproject.toml
├── requirements.txt
├── alembic.ini
```

## Componentes principais

### `main.py`
Arquivo de inicialização da aplicação FastAPI. Ele monta a aplicação e inclui o router de pedidos.

### `src/app/routes/orders.py`
Define os endpoints HTTP da API:
- listar pedidos
- buscar pedido por id
- criar pedido
- atualizar pedido
- excluir pedido

### `src/app/service/orders.py`
Contém a lógica de acesso ao banco e operações CRUD sobre os pedidos.

### `src/app/models/order.py`
Modelo SQLAlchemy da tabela `orders`.

### `src/app/schemas/order.py`
Schemas Pydantic para validação de entrada e saída da API.

### `src/app/settings/env/env.py`
Leitura das variáveis de ambiente do projeto.

### `src/app/settings/database/database.py`
Configuração do engine e da sessão do SQLAlchemy.

## Requisitos para execução

- Docker
- Docker Compose

## Como executar

1. Clone o repositório.
2. Acesse a pasta do projeto.
3. Execute:

```bash
docker compose up -d --build
```

4. A aplicação ficará disponível em:

```text
http://localhost:8000
```

5. A documentação interativa da API estará disponível em:

```text
http://localhost:8000/docs
```

6. O banco PostgreSQL será iniciado automaticamente pelo serviço `postgres`.

A interface Swagger em `/docs` permite testar os endpoints diretamente no navegador com a mesma API que será usada em produção.

## Variáveis de ambiente

O projeto já inclui um exemplo em `.env.example` com as variáveis de configuração padrão:

```env
POSTGRES_DB=api_pedidos
POSTGRES_USER=root
POSTGRES_PASSWORD=root
DATABASE_URL=postgresql+psycopg://root:root@postgres:5432/api_pedidos
```

No ambiente do Docker, os valores padrão já estão configurados no `docker-compose.yml`.

## Endpoints principais

### Health check

- `GET /health`

### Pedidos

- `GET /orders`
- `GET /orders/{order_id}`
- `POST /orders`
- `PUT /orders/{order_id}`
- `DELETE /orders/{order_id}`

## Observações finais

- A aplicação está pronta para subir com Docker Compose.
- O banco é criado e inicializado automaticamente.
- As migrations são executadas no container da aplicação via Alembic.
- A tag `APIPedidos-1-final` representa a versão que deverá ser considerada como entrega final.
