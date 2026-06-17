"""
Conexão com o MySQL e criação automática da tabela de produtos.
"""

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3308")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id       INT AUTO_INCREMENT PRIMARY KEY,
            nome     VARCHAR(100) NOT NULL,
            preco    DECIMAL(10, 2) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
