from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor):
        self.produto = nome
        self.valor = valor

    def __str__(self):
        return f"{self.produto} custa R${self.valor:,.2f}"

    def etiqueta(self):

        conteudo = f"{self.produto.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"{self.valor:,.2f}"
        conteudo += f"{precof.center(30, ".")}"
        caixa = Panel(
            conteudo,
            title="Produto", 
            width=34)
        
        print(caixa)



p1 = Produto("iPhone 17 Pro Max", 25_00.85)
p2 = Produto("Notebook Gamer", 8_000.00)

p1.etiqueta()
p2.etiqueta()