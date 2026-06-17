# Lab 2 — Criando sua primeira API REST com FastAPI

Neste lab você vai criar uma API com 4 endpoints funcionando no seu computador. Os dados ficam em memória (uma lista Python) — sem banco de dados ainda. No Lab 3 você vai conectar essa mesma API ao MySQL.

---

## O que você vai aprender

- Como criar endpoints GET, POST e DELETE com FastAPI
- Como usar Pydantic para validar o corpo da requisição automaticamente
- Como testar a API pelo Swagger (interface gerada automaticamente)
- Como testar com `curl` pelo terminal

---

## Pré-requisitos

- Python 3.10+

---

## Passo 1 — Criar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows
```

## Passo 2 — Instalar as dependências

```bash
pip install -r requirements.txt
```

## Passo 3 — Rodar a API

```bash
uvicorn main:app --reload
```

O `--reload` reinicia o servidor automaticamente quando você salva o arquivo.

Você vai ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

## Passo 4 — Testar no Swagger

Abra no browser: **http://localhost:8000/docs**

O Swagger é a documentação interativa gerada automaticamente pelo FastAPI. Você pode testar todos os endpoints direto pelo browser, sem precisar do curl.

---

## Testando com curl (opcional)

### Listar todos os produtos
```bash
curl http://localhost:8000/produtos
```

### Buscar produto por ID
```bash
curl http://localhost:8000/produtos/1
```

### Criar novo produto
```bash
curl -X POST http://localhost:8000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Monitor", "preco": 1200.00}'
```

### Remover produto
```bash
curl -X DELETE http://localhost:8000/produtos/1
```

---

## Endpoints disponíveis

| Método | URL | O que faz |
|--------|-----|-----------|
| GET | `/` | Mensagem de boas-vindas + total de produtos |
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/{id}` | Busca produto por ID (404 se não existir) |
| POST | `/produtos` | Cria novo produto (body: `nome` e `preco`) |
| DELETE | `/produtos/{id}` | Remove produto por ID |

---

## Atenção — dados em memória

Os produtos somem quando você para o servidor (`Ctrl+C`). Isso é esperado neste lab — no **Lab 3** você vai conectar ao MySQL para os dados ficarem salvos.

---

## Estrutura de arquivos

```
lab2-criando-api-fastapi/
├── main.py            # API FastAPI completa
└── requirements.txt
```

---

## Checklist

- [ ] API subiu sem erro (`uvicorn main:app --reload`)
- [ ] `/docs` abriu no browser e mostrou os 5 endpoints
- [ ] Criou um produto novo via Swagger ou curl
- [ ] Buscou o produto por ID
- [ ] Tentou buscar um ID inexistente e recebeu 404
- [ ] Removeu um produto e confirmou que sumiu da lista
