# Lab 3 — API REST conectada ao MySQL

Neste lab você vai conectar a API do Lab 2 a um banco de dados MySQL real rodando via Docker. Os dados agora ficam salvos permanentemente — mesmo depois de reiniciar o servidor.

Este lab une os conceitos de três aulas:
- **Aula 2.C** — API REST com FastAPI
- **Aula 2.D** — Credenciais protegidas com `.env`
- **Aula 2.B** — Banco de dados MySQL

---

## O que você vai aprender

- Como conectar FastAPI a um banco de dados MySQL
- Como criar a tabela automaticamente na inicialização da API
- Como executar INSERT, SELECT e DELETE via Python
- Como usar `.env` para proteger as credenciais do banco

---

## Pré-requisitos

- Python 3.10+
- Docker Desktop rodando

---

## Passo 1 — Subir o banco MySQL com Docker

```bash
docker compose up -d
```

Aguarde o banco iniciar (uns 15 segundos). Verifique se está saudável:

```bash
docker compose ps
```

O status deve ser `healthy`.

## Passo 2 — Criar o arquivo .env

```bash
cp .env.example .env
```

O `.env` tem as credenciais do banco. Ele está no `.gitignore` e nunca vai para o GitHub.

## Passo 3 — Criar o ambiente virtual e instalar dependências

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

## Passo 4 — Rodar a API

```bash
uvicorn main:app --reload
```

Na primeira vez, a API cria automaticamente a tabela `produtos` no banco.

Você vai ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

## Passo 5 — Testar no Swagger

Abra no browser: **http://localhost:8000/docs**

---

## Testando com curl

### Criar um produto (fica salvo no MySQL)
```bash
curl -X POST http://localhost:8000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Monitor", "preco": 1200.00}'
```

### Listar todos os produtos
```bash
curl http://localhost:8000/produtos
```

### Buscar produto por ID
```bash
curl http://localhost:8000/produtos/1
```

### Remover produto
```bash
curl -X DELETE http://localhost:8000/produtos/1
```

---

## Diferença do Lab 2 para o Lab 3

| Lab 2 | Lab 3 |
|-------|-------|
| Dados em lista Python | Dados no MySQL |
| Dados somem ao reiniciar | Dados persistem para sempre |
| Sem banco, sem Docker | MySQL via Docker Compose |
| Sem `.env` | Credenciais protegidas com `.env` |

---

## Como funciona por dentro

```
Browser / curl
     ↓
FastAPI (main.py)          ← recebe a requisição HTTP
     ↓
database.py                ← abre conexão com MySQL
     ↓
MySQL (Docker)             ← executa o SQL e retorna dados
     ↓
FastAPI                    ← transforma em JSON e responde
     ↓
Browser / curl             ← recebe o JSON
```

---

## Parar o banco ao final

```bash
docker compose down
```

---

## Estrutura de arquivos

```
lab3-api-com-banco-mysql/
├── main.py            # API FastAPI com MySQL
├── database.py        # conexão e criação da tabela
├── docker-compose.yml # banco MySQL via Docker
├── .env.example       # template das credenciais (vai ao GitHub)
├── .env               # credenciais reais (NÃO vai ao GitHub)
├── .gitignore
└── requirements.txt
```

---

## Checklist

- [ ] `docker compose up -d` rodou e o status ficou `healthy`
- [ ] `.env` criado a partir do `.env.example`
- [ ] API subiu sem erro
- [ ] Criou um produto via Swagger ou curl e recebeu id=1
- [ ] Parou o servidor (`Ctrl+C`), reiniciou e o produto ainda estava lá
- [ ] Removeu o produto e confirmou que não aparece mais no GET
