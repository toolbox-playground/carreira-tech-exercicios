"""
LAB 3 — API FastAPI com banco de dados MySQL (Aula 2.C)
Os dados agora ficam salvos no MySQL mesmo após reiniciar o servidor.

Para rodar:
    1. docker compose up -d
    2. cp .env.example .env
    3. uvicorn main:app --reload

Docs automáticas:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_connection, init_db

app = FastAPI(title="API de Produtos — Lab 3 (com MySQL)")


@app.on_event("startup")
def startup():
    init_db()


class Produto(BaseModel):
    nome: str
    preco: float


@app.get("/")
def home():
    return {"mensagem": "API com MySQL no ar! Acesse /docs para testar."}


@app.get("/produtos")
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
    produto = cursor.fetchone()
    cursor.close()
    conn.close()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/produtos", status_code=201)
def criar_produto(produto: Produto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s)",
        (produto.nome, produto.preco)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return {"id": novo_id, "nome": produto.nome, "preco": produto.preco}


@app.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
    conn.commit()
    afetados = cursor.rowcount
    cursor.close()
    conn.close()
    if afetados == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"mensagem": f"Produto {produto_id} removido com sucesso"}
