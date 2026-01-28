import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ContasAbertas (
        conta INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        senha INTEGER NOT NULL,
        saldo REAL DEFAULT 0
    );
""")