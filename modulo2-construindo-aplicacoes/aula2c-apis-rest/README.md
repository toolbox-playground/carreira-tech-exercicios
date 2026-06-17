# Aula 2.C — APIs REST: Lab Prático

Dois labs: consumir uma API pública com `requests` e criar sua própria API com FastAPI.

---

## Pré-requisitos

- Python 3.10+
- Docker Desktop (só para o Lab 3)

---

## Configurar o ambiente

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## Lab 1 — Consumindo uma API pública com requests

Nenhum servidor necessário — consome a API pública `jsonplaceholder.typicode.com`.

```bash
python3 consumir_api.py
```

O script demonstra:
- `GET /posts` — busca lista e mostra total e primeiro título
- `GET /posts/1` — busca item por ID
- `POST /posts` — cria novo recurso e recebe 201
- `raise_for_status()` — tratamento de erro HTTP

---

## Lab 2 — Criando sua API FastAPI

### Rodar localmente com uvicorn

```bash
uvicorn main:app --reload
```

A API sobe em `http://localhost:8000`.  
Docs interativas (Swagger): `http://localhost:8000/docs`

### Endpoints disponíveis

| Método | URL | O que faz |
|--------|-----|-----------|
| GET | `/` | Mensagem de boas-vindas |
| GET | `/produtos` | Lista todos os produtos |
| GET | `/produtos/{id}` | Busca produto por ID |
| POST | `/produtos` | Cria novo produto |
| DELETE | `/produtos/{id}` | Remove produto |

### Testar com curl

```bash
# Listar produtos
curl http://localhost:8000/produtos

# Buscar por ID
curl http://localhost:8000/produtos/1

# Criar produto
curl -X POST http://localhost:8000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Monitor", "preco": 1200.00}'

# Remover produto
curl -X DELETE http://localhost:8000/produtos/1
```

Ou use o Swagger em `http://localhost:8000/docs` — sem precisar do curl.

---

## Lab 3 — Containerizar a API com Docker

### Construir a imagem

```bash
docker build -t minha-api:latest .
```

### Rodar o container

```bash
docker run -p 8000:8000 minha-api:latest
```

A API estará disponível em `http://localhost:8000` — rodando dentro do container.

---

## Estrutura dos arquivos

```
aula2c-apis-rest/
├── consumir_api.py    # Lab 1: consome API pública com requests
├── main.py            # Lab 2: API FastAPI com CRUD de produtos
├── Dockerfile         # Lab 3: containerização da API
├── requirements.txt
└── .gitignore
```

---

## Missão da aula — checklist

- [ ] Lab 1 rodou e mostrou posts no terminal
- [ ] API FastAPI subiu e `/docs` abre no browser
- [ ] Testou GET, POST e DELETE no Swagger ou curl
- [ ] Container Docker rodou e API respondeu
- [ ] **Desafio:** conectar o `GET /produtos` ao MySQL da Aula 2.B
