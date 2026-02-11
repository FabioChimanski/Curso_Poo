from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto:
    def __init__(self, nome, valor):
        self.produto = nome
        self.valor = valor

    def etiqueta(self):

        conteudo = f'{self.produto}\n -----------------------------------\n..........{self.valor}..........'
        
        conteudo_centralizado = (conteudo)
        caixa = Panel(
            conteudo_centralizado, 
            title="Produto", 
            width=40)
        
        print(caixa)



p1 = Produto("iPhone 17 Pro Max", 25_00.85)
p2 = Produto("Notebook Gamer", 8_000.00)

p1.etiqueta()
p2.etiqueta()