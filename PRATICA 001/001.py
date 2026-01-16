#Declaração de Classes
class Compra:
    def __init__(self):
        self.produto = ""
        self.valor = 0
        self.quantidade = 0
        self.frete = 0
        self.forma_pagamento = 0

    def calcular(self):
        total = self.valor * self.quantidade + self.frete
        return total
    
    def resumo_compra(self):
        return f"Resumo compra:\n    Produto: {self.produto}\n    Quantidade: {self.quantidade}\n    Valor: {self.valor}\n    Frente: {self.frete}\n\nTotal: {self.calcular()}\n\nForma pagamento: {self.forma_pagamento}"
    
#Declaração objetos

g1 = Compra()
g1.produto = "Caneta"
g1.valor = 1.5
g1.quantidade = 2
g1.frete = 10.5
g1.forma_pagamento = "Cartão"
print(g1.resumo_compra())