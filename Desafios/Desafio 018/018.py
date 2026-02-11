from rich import print
from rich import text
from rich.panel import Panel

class Churrasco():

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quantidade = quant
        self.valor_kg_carne = 82.40
        self.kg_total = 0
        self.valor_pessoa = 0
        self.total_pagar = 0
        self.soma()


    def soma(self, ):
        self.kg_total = self.quantidade * 0.4
        self.total_pagar = self.kg_total * self.valor_kg_carne
        self.valor_pessoa = self.total_pagar / self.quantidade
        return(self.valor_pessoa, self.kg_total)

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\nCada participante comerá 0.4 kg e cada kg custa R$ {self.valor_kg_carne}\nRecomendo comprar [blue]{self.kg_total:.3f} kg[/] de carne\nO custo total será de [green]R$ {self.total_pagar:.2f}[/]\nCada pessoa pagará R$ [red]{self.valor_pessoa:.2f}[/] para participar'

        caixa = Panel(
            conteudo,
            title = self.titulo,
            width=65
        )

        print(caixa)

c1 = Churrasco("Churras dos Amigos", 100)
c1.analisar()