# Aula 2.D — Segurança Básica: Lab Prático

Refatoração de código inseguro (senha hardcoded) para seguro (`.env` + `os.getenv()`).

---

## Pré-requisitos

- Docker Desktop rodando
- Python 3.10+

---

## Passo 1 — Subir o banco com Docker

```bash
docker compose up -d
```

Aguarde o MySQL iniciar (uns 15 segundos). Você pode verificar:

```bash
docker compose ps
```

O status deve aparecer como `healthy`.

---

## Passo 2 — Criar ambiente virtual e instalar dependências

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## Passo 3 — Rodar o código INSEGURO (o problema)

```bash
python main_inseguro.py
```

Funciona — mas a senha `senha123` está escrita direto no código.  
Abra o arquivo `main_inseguro.py` e veja o problema na linha com `password=`.

---

## Passo 4 — Criar o arquivo .env (PASSO 1 da refatoração)

```bash
cp .env.example .env
```

O arquivo `.env` já tem os valores corretos para este lab.  
Verifique que ele **não aparece** no git:

```bash
git status
```

O `.env` deve estar **invisível** (listado em "ignored" ou ausente do status).

---

## Passo 5 — Rodar o código SEGURO (a solução)

```bash
python main_seguro.py
```

Agora a senha vem do `.env`, não do código.  
Abra `main_seguro.py` e compare com `main_inseguro.py` — as únicas diferenças são:

| Inseguro | Seguro |
|---|---|
| `password="senha123"` | `password=os.getenv("DB_PASSWORD")` |
| Sem imports extras | `from dotenv import load_dotenv` + `load_dotenv()` |

---

## Passo 6 — Verificar o checklist de segurança

```bash
# .env está no .gitignore?
cat .gitignore | grep ".env"

# Tem alguma senha hardcoded no código?
grep -r "password=" . --include="*.py"
```

O `main_inseguro.py` vai aparecer — é o problema.  
O `main_seguro.py` não deve aparecer — é a solução.

---

## Parar o banco ao final

```bash
docker compose down
```

---

## Estrutura do projeto

```
aula2d-seguranca-basica/
├── docker-compose.yml    # banco MySQL via Docker
├── main_inseguro.py      # ❌ versão com senha no código
├── main_seguro.py        # ✅ versão segura com .env
├── .env.example          # template — vai ao GitHub
├── .env                  # valores reais — NÃO vai ao GitHub
├── .gitignore            # protege o .env
└── requirements.txt      # dependências Python
```
