from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case  "amarelo":
                escolha = "[yellow]"
            case _:
                escolha = "[white]"
        
        self.cor = escolha
        self.tampada = False

    def destampar(self):
        self.tampada = True

    def quebrar_linha(self, quebrar):
        for i in range(quebrar):
            print("\n", end="")
    
    def escrever(self, msg):
        
        if self.tampada == True:
            print(f"{self.cor}{msg}", end="")
        else:
            print(f"A {self.cor}caneta [/] está tampada")


c1 = Caneta("amarelo")
c2 = Caneta("azul")
c3 = Caneta("vermelho")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá Fábio')
c1.quebrar_linha(1)
c2.escrever("Campo")
c2.quebrar_linha(2)
c3.escrever("Nês")