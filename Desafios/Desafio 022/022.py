from rich import print
from rich.panel import Panel

class Controle():
    
    def __init__(self, volume, canal):
        self.power = False
        self.volume = volume
        self.canal = canal
        self.on_off = "DESLIGADA"

    def ligar(self):

        if self.power == True:
            self.power = False
            self.on_off = f"[green]DESLIGADA"
        elif self.power == False: 
            self.on_off = f"[red]LIGADA"
            self.power = True

        return self.power, self.on_off


    def apresentacao(self):

        conteudo = Panel(
        self.on_off, 
        title= f" [ TV ]",
        width=30
        )

        print(conteudo)
        
        comando = input(int(f"  < CH >   - VAL +  "))

    def acoes():
        pass


c1 = Controle(1, 1)
c1.apresentacao()

