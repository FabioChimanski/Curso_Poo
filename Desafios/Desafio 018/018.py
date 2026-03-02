from rich import print
from rich import text
from rich.panel import Panel

class Churrasco():

    consumo_padrao = 0.400
    preco_kg = 82.40

    def __init__(self, titulo, participantes):
        self.titulo = titulo
        self.participantes = participantes

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando"
        
    def analisar(self):
        conteudo = f"Analizando o [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg de carne custa R${Churrasco.preco_kg:.2f}"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_quantidade_carne():.3f}[/] Kg de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():.2f}[/]"
        conteudo += f"\nCada participanten deve pagar [yellow]R${self.calcular_custo_individual():.2f}[/]"


        painel = Panel(conteudo, title=self.titulo)
        print(painel)

    def calcular_quantidade_carne(self) -> float:
        return Churrasco.consumo_padrao * self.participantes

    def calcular_custo_total(self) -> float:
        return self.calcular_quantidade_carne() * self.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()