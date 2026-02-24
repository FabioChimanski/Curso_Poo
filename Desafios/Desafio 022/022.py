from rich import print
from rich.panel import Panel
from rich.console import Console

class Controle():
    
    def __init__(self, volume, canal):
        self.power = False
        self.volume = volume
        self.canal = canal
        self.on_off = "[red]DESLIGADA"

    def ligar(self):

            self.power = not self.power

            if self.power:
                self.on_off = f"[green]DESLIGADA"
            else:
                self.on_off = f"[red]LIGADA"


    def apresentacao(self):

        console = Console()
            
        while True:

            conteudo = Panel(
            self.on_off,
            title= f" [ TV ]",
            width=30
            )

            print(conteudo)
        
            comando = input(f"  < CH >   - VAL +  ")

            match comando:
                case "@":
                    self.ligar()
                    console.clear()
                case "0":
                    break
                case ">":
                    print(">")
                case "<":
                    print("<")
                case "+":
                    print("+")
                case "-":
                    print("-")

    def acoes():
        pass


c1 = Controle(1, 1)
c1.apresentacao()

