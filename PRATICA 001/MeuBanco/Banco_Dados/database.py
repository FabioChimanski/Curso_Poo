import sqlite3


banco = sqlite3.connect('banco_sistema.db')

cursor = banco.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contas_bancarias (
        conta INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha INTEGER NOT NULL,
        saldo REAL DEFAULT 0
    );
""")


def criar_conta(nome_usuario, senha_usuario):
    cursor.execute("""
                   INSERT INTO Contas_bancarias (nome, senha, saldo) VALUES (?, ?, ?0 ,(nome_usuario, senha_usuario) """)
    banco.commit()
    banco.close()
    print(f'Bem vindo {nome_usuario}! Sua conta foi criada com sucesso')

    
def saldo():
    pass

def transferencia():
    pass

def saque():
    pass

def extrato():
    pass