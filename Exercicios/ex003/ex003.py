#Simulador de caixa eletronico


"""
Conta:
atributos
    nome
    conta
    saldo
    data
    hora

metodos
    sacar
    transferir
    consultar_saldo

estado
    nome
    saldo

"""

class ContaBancaria:
    #DOCSTRING
    """ 
Cria uma conta bancária e permite fazer saques e depositos
    """
    def __init__(self, id, nome ,saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso! Saldo atual de R${self.saldo:,.2f}.')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito no valor de R${valor:,.2f} realizado com sucesso!')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque no valor de R${valor:,.2f} realizado com sucesso!')
        else:
            print('Saldo insuficiente para saque!')

c1 = ContaBancaria(112, "Fabio", 3000)
c1.depositar(500)
c1.saque(3600)
print(c1)