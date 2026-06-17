# Lab 1 — Consumindo uma API pública com requests

Neste lab você vai usar a biblioteca `requests` do Python para fazer chamadas HTTP a uma API pública real — sem precisar criar nenhum servidor.

---

## O que você vai aprender

- O que é uma requisição HTTP e como ela funciona
- Como fazer GET e POST com Python
- Como ler a resposta JSON e transformar em dados Python
- Como tratar erros de HTTP com `raise_for_status()`

---

## Pré-requisitos

- Python 3.10+
- Conexão com a internet

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

## Passo 3 — Rodar o script

```bash
python3 consumir_api.py
```

Você vai ver no terminal:
- A lista de 100 posts retornados pela API
- Um post específico buscado por ID
- A resposta de criar um novo post (status 201)
- Um erro HTTP tratado corretamente

---

## O que o código faz

```python
import requests

# GET — busca lista
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)   # 200
posts = response.json()        # lista de dicionários Python

# POST — cria recurso
resp = requests.post(url, json={"title": "...", "body": "...", "userId": 1})
print(resp.status_code)        # 201 Created

# Tratamento de erro
r.raise_for_status()           # lança exceção se status >= 400
```

---

## Estrutura de arquivos

```
lab1-consumindo-api/
├── consumir_api.py    # script principal
└── requirements.txt
```

---

## Checklist

- [ ] Script rodou sem erro
- [ ] Você viu o status 200 e 201 no terminal
- [ ] Entendeu a diferença entre GET (buscar) e POST (criar)
- [ ] O erro 404 foi capturado e tratado corretamente
