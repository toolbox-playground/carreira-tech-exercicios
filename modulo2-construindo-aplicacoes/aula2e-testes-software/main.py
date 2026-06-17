"""
LAB 2 — FastAPI: API com endpoint de produtos (Aula 2.E)
Usado para demonstrar testes de API com TestClient
"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

produtos = []


@app.get("/produtos")
def listar():
    return produtos


@app.post("/produtos", status_code=201)
def adicionar(produto: dict):
    if "nome" not in produto or "preco" not in produto:
        raise HTTPException(status_code=422, detail="Campos 'nome' e 'preco' são obrigatórios")
    if produto["preco"] < 0:
        raise HTTPException(status_code=422, detail="Preço não pode ser negativo")
    produtos.append(produto)
    return produto


@app.delete("/produtos")
def limpar():
    produtos.clear()
    return {"mensagem": "Lista limpa"}
