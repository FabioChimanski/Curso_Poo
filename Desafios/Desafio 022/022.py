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
            self.on_off = "[green]LIGADA"
        else:
            self.on_off = "[red]DESLIGADA"

    def apresentacao(self):
        while True:
            if self.power:
                conteudo = Panel(
                    self.on_off,
                    title=" [ TV ]",
                    width=30
                )
                print(conteudo)
            else:
                conteudo = Panel(
                    f"{self.on_off}\n",
                    "CANAL  :  1  2  3  4  5 ",
                    "VOLUME :  ",
                    title=" [ TV ]",
                    width=30
                )
                print(conteudo)
                
            comando = input(f"  < CH >   - VAL +   ")

            match comando:
                case "@":
                    self.ligar()
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

    def canal(self):
        pass

c1 = Controle(1, 1)
c1.apresentacao()