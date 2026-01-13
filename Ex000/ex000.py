#Declaração de Classes
class Gafanhoto:
    def __init__(self):#metodo construtor

        #Atributos de instancia
        self.nome = ""
        self.idade = 0


        #Metedos de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} anos de idade."
    

#Declaração de Objetos

g1 = Gafanhoto()
g1.nome = "Fabio"
g1.idade = 27
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Renata"
g2.idade = 28
g1.aniversario()
print(g2.mensagem())