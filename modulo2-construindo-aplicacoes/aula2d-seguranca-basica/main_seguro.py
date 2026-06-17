"""
LAB Aula 2.D — Segurança Básica
VERSÃO SEGURA: credenciais lidas do arquivo .env

Diferenças em relação ao main_inseguro.py:
  1. Nenhuma senha escrita no código
  2. load_dotenv() carrega o .env automaticamente
  3. os.getenv() lê cada variável do ambiente
  4. O .env está no .gitignore — nunca vai ao GitHub
"""

# PASSO 3: instale a dependência antes de rodar
#   pip install -r requirements.txt

from dotenv import load_dotenv
import os
import mysql.connector

# Carrega as variáveis do arquivo .env
load_dotenv()

# ✅ Correto: lê do ambiente, sem senha no código
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "3307")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
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
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", ("Maria Arquivo Seguro", "maria@email.com"))
conn.commit()

# Lê os dados
cursor.execute("SELECT * FROM usuarios")
for row in cursor.fetchall():
    print(f"✅ Usuário encontrado: {row}")

cursor.close()
conn.close()
print("Conexão encerrada — credenciais nunca apareceram no código.")
