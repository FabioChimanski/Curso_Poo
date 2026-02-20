from rich import print

class Caneta():
    def __init__(self, cor):
        self.cor = cor
        self.tampada = False
        self.cor_caneta = ""
        if self.cor == "azul":
            self.cor_caneta = "blue"
        elif self.cor =="vermelho":
            self.cor_caneta = "red"
        elif self.cor == "amarelo":
            self.cor_caneta = "yellow"


    def destampar(self):
        self.tampada = True

    def quebrar_linha(self, quebrar):
        for i in range(quebrar):
            print("\n", end="")

    
    def escrever(self, msg):
        
        if self.tampada == True:
            print(f'[{self.cor_caneta}]{msg}')
        else:
            print(f'A [{self.cor_caneta}]canetá[/] está tampada')


c1 = Caneta("amarelo")
c2 = Caneta("azul")
c3 = Caneta("vermelho")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá Fábio')
c1.quebrar_linha(1)
c2.escrever("Campo")
c3.escrever("Nês")