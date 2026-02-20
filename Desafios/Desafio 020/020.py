from rich.console import Console
from rich.panel import Panel
from rich.console import Group
from rich.style import Style

console = Console()

class Gamer():
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogos):
        self.jogos_favoritos.append(jogos)
    
    def ficha(self):

        conteudo = Group(
            f"Nome real: {self.nome}",
            "",
            "Jogos Favoritos",
            *(f"{item}" for item in self.jogos_favoritos)
        )

        caixa = Panel(
            conteudo, 
            title = f"Jogador <{self.nick}>"
        )

        console.print(caixa)

j1 = Gamer("Fabio", "yLandemBerguer")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()