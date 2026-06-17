"""
LAB 2 — Testes de API FastAPI com TestClient (Aula 2.E)
Sem subir servidor real — TestClient simula as requisições HTTP
"""

import pytest
from fastapi.testclient import TestClient
from main import app, produtos

client = TestClient(app)


@pytest.fixture(autouse=True)
def limpar_produtos():
    """Garante que a lista está vazia antes de cada teste (independência total)."""
    produtos.clear()
    yield
    produtos.clear()


# ── GET /produtos ─────────────────────────────────────────────────────────────

def test_listar_produtos_vazio():
    resp = client.get("/produtos")
    assert resp.status_code == 200
    assert resp.json() == []

def test_listar_produtos_com_itens():
    client.post("/produtos", json={"nome": "Curso", "preco": 497})
    resp = client.get("/produtos")
    assert len(resp.json()) == 1
    assert resp.json()[0]["nome"] == "Curso"


# ── POST /produtos ────────────────────────────────────────────────────────────

def test_adicionar_produto():
    resp = client.post("/produtos", json={"nome": "Curso", "preco": 497})
    assert resp.status_code == 201
    assert resp.json()["nome"] == "Curso"

def test_adicionar_produto_sem_nome_retorna_erro():
    resp = client.post("/produtos", json={"preco": 100})
    assert resp.status_code == 422

def test_adicionar_produto_preco_negativo_retorna_erro():
    resp = client.post("/produtos", json={"nome": "Inválido", "preco": -10})
    assert resp.status_code == 422

def test_adicionar_dois_produtos():
    client.post("/produtos", json={"nome": "Produto A", "preco": 100})
    client.post("/produtos", json={"nome": "Produto B", "preco": 200})
    resp = client.get("/produtos")
    assert len(resp.json()) == 2
