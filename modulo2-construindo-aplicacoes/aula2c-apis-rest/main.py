"""
LAB 2 — Criando uma API REST com FastAPI (Aula 2.C)
Endpoints: GET /produtos, GET /produtos/{id}, POST /produtos, DELETE /produtos/{id}
Docs automáticas: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Produtos — Carreira Tech")

# Banco em memória (lista Python) — suficiente para o lab
produtos_db: list[dict] = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00},
    {"id": 2, "nome": "Mouse", "preco": 89.90},
    {"id": 3, "nome": "Teclado", "preco": 149.90},
]
proximo_id = 4


class Produto(BaseModel):
    nome: str
    preco: float


# ── GET / ─────────────────────────────────────────────────────────────────────

@app.get("/")
def home():
    return {"mensagem": "API de Produtos está no ar! 🚀", "docs": "/docs"}


# ── GET /produtos ─────────────────────────────────────────────────────────────

@app.get("/produtos")
def listar_produtos():
    return produtos_db


# ── GET /produtos/{id} ────────────────────────────────────────────────────────

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos_db:
        if produto["id"] == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")


# ── POST /produtos ────────────────────────────────────────────────────────────

@app.post("/produtos", status_code=201)
def criar_produto(produto: Produto):
    global proximo_id
    novo = {"id": proximo_id, "nome": produto.nome, "preco": produto.preco}
    produtos_db.append(novo)
    proximo_id += 1
    return novo


# ── DELETE /produtos/{id} ─────────────────────────────────────────────────────

@app.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int):
    for i, produto in enumerate(produtos_db):
        if produto["id"] == produto_id:
            produtos_db.pop(i)
            return {"mensagem": f"Produto {produto_id} removido"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")
