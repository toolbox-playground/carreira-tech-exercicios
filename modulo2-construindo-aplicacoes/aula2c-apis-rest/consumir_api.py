"""
LAB 1 — Consumindo uma API pública com requests (Aula 2.C)
API de teste: jsonplaceholder.typicode.com — sem autenticação necessária
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("=" * 50)
print("LAB 1 — Consumindo API pública com requests")
print("=" * 50)

# ── GET: buscar lista de posts ─────────────────────────────────────────────────
print("\n📋 Buscando lista de posts...")
response = requests.get(f"{BASE_URL}/posts")
print(f"Status: {response.status_code}")           # 200

posts = response.json()                             # lista de dicionários Python
print(f"Total de posts: {len(posts)}")              # 100
print(f"Primeiro post: {posts[0]['title']}")

# ── GET com ID: buscar item específico ────────────────────────────────────────
print("\n🔍 Buscando post por ID...")
post = requests.get(f"{BASE_URL}/posts/1").json()
print(f"Título: {post['title']}")
print(f"Corpo: {post['body'][:60]}...")

# ── POST: criar novo recurso ──────────────────────────────────────────────────
print("\n✉️  Criando novo post...")
novo_post = {
    "title": "Meu primeiro post via API",
    "body": "Aprendi a consumir APIs com Python e requests!",
    "userId": 1
}
resp = requests.post(f"{BASE_URL}/posts", json=novo_post)
print(f"Status: {resp.status_code}")               # 201 Created
print(f"Post criado: {resp.json()}")

# ── Tratamento de erro com raise_for_status() ─────────────────────────────────
print("\n⚠️  Testando endpoint inexistente...")
try:
    r = requests.get(f"{BASE_URL}/posts/9999")
    r.raise_for_status()                            # lança exceção se status >= 400
    print(r.json())
except requests.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.ConnectionError:
    print("Sem conexão com a internet")

print("\n✅ Lab 1 concluído!")
