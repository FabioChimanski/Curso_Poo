
class Conta:

    def __init__(self,conta, nome, senha, saldo):#CRIAR CONTA
        self.conta = ""
        self.senha = ""
        self.saldo = 0
        self.nome = ""
        return f'{nome}, sua conta {conta} foi criada com sucesso!'
    
    def depositar(self, valor):
        self.saldo += valor
        return f'Seu deposito no de R${valor:,.2f} foi realizado com sucesso!'
    
    def saque(self, valor):
        if valor < self.saldo:
            print("Saque não realizado! Saldo insuficiente...")
        saldo -= valor
    
        