"""
LAB Aula 2.D — Segurança Básica
VERSÃO INSEGURA: credenciais hardcoded no código

Este arquivo representa o "código legado" recebido para revisar.
O problema: a senha está escrita diretamente no código.
Se esse arquivo for para o GitHub, a senha vaza para sempre.

Tarefa: refatorar para a versão segura (veja main_seguro.py)
"""

import mysql.connector

# ❌ PROBLEMA: credenciais hardcoded — NUNCA faça isso
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="appuser",
    password="senha123",     # 😱 senha exposta no código
    database="carreirtech"
)

cursor = conn.cursor()

# Cria tabela de exemplo
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100)
    )
""")

# Insere um registro
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", ("João Senha no codigo", "joao@email.com"))
conn.commit()

# Lê os dados
cursor.execute("SELECT * FROM usuarios")
for row in cursor.fetchall():
    print(f"✅ Usuário encontrado: {row}")

cursor.close()
conn.close()
print("Conexão encerrada.")
